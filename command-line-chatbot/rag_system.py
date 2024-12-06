"""
Stuff that will go in this file

All the rag stuff

All the chatbot interface stuff (except install stuff)


Stuff to have for all llm prompts

## ROLE

## INPUT

## PROCESS

## OUTPUT CHARACTERISTICS

## OUTPUT FORMAT

## DO NOT

## EXAMPLES

"""


import groq
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
import logging
import sqlite3
import re

# TODO: Add something here that imports the database
# TODO: Make all the prompts good

#################
# LLM FUNCTIONS #
#################

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def run_llm(system, user, model='llama3-8b-8192', seed=None):
    '''
    This is a helper function for all the uses of LLMs in this file.
    '''
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'system',
                'content': system,
            },
            {
                "role": "user",
                "content": user,
            }
        ],
        model=model,
        seed=seed,
    )
    return chat_completion.choices[0].message.content
def extract_keywords(text):
    system = '''
    
    You are a professional journalist assigned with extracting keywor
    ds from the following text.  

    The keywords should be relevant to the text and will be used to s
    earch for related articles. 

    Only return the keywords. Separate each keyword with a space when
    the word ends. Do not place the spaces between each letter—put th
    em at the end of each word. Only provide 5 keywords. 

    Do not provide more than 5 keywords. Do not provide any additional
    characters. Do not provide any punctuation marks

    ## ROLE

    You are a senior Unix developer with years of coding experience.

    ## INPUT

    You will be given an input for a user who wants to know what unix command would best execute their instruction.

    ## PROCESS

    You will analyze the users' input and pull out keywords from that input that will be sent to a huge database of Unix commands. Pick the keywords that will lead to the best results from that database—so the keywords that are the most important to the functioning of a relevant command. Output as many keywords as you think are necessary to capture the user input, but no more. If you aren't sure what keywords are best, just output a list of keywords that would search for the most common and useful unix commands.

    ## OUTPUT CHARACTERISTICS

    You should output all of the keywords formatted like a python list without any other words, context, or characters. Output as many keywords as you think are necessary to capture the user input, but no more.

    ## OUTPUT FORMAT

    Your output will be in this format:

    ['keyword1', 'keyword2', 'keyword3']

    ## DO NOT

    Return anything aside from the list of keywords

    Provide any context or explanations about the list of keywords

    Return a list of keywords in any other list format except the python format specified in ## OUTPUT FORMAT

    ## EXAMPLES

    INPUT: "navigate to my home directory"
    OUTPUT: ['~', 'cd', 'home', 'directory']

    INPUT: "pull all files with the word 'cat' in them"
    OUTPUT: ['grep', 'find', 'cat', 'files', 'word', 'search']

    INPUT: "list all files in a directory"
    OUTPUT: ['ls', 'list', 'directory', 'files']

    INPUT: "find the size of a directory"
    OUTPUT: ['du', 'directory', 'size']

    INPUT: "copy a file from one directory to another"
    OUTPUT: ['cp', 'copy', 'file', 'directory', 'move']

    INPUT: "move a file to a new location"
    OUTPUT: ['mv', 'move', 'file', 'location']

    INPUT: "delete a file"
    OUTPUT: ['rm', 'remove', 'file', 'delete']

    INPUT: "search for a file in the filesystem"
    OUTPUT: ['find', 'search', 'file', 'filesystem']

    '''
    print("extracting keywords", flush=True)
    response = run_llm(system, text)
    print(f"DEBUG: response: {response}", flush=True)
    cleaned_response = re.sub(r"[\[\]']", "", text)
    print(f"DEBUG: cleaned_response: {cleaned_response}")
    return cleaned_response

####################
# HELPER FUNCTIONS #
####################

def _logsql(sql):
    rex = re.compile(r'\W+')
    sql_dewhite = rex.sub(' ', sql)
    logging.debug("SQL: %s", sql_dewhite)

#######
# RAG #
#######

def rag(text, db):
    keywords = extract_keywords(text)
    print("querying database", flush=True)
    manpages = db.find_manpages(query = keywords)
    print("database queried", flush=True)
    
    system = """
    
    ## ROLE

    You are a computer program tasked with entering commands into a Unix machine.

    ## INPUT

    You will be given an instruction from a user and a list of relevant Unix Commands with explanations for how each command works.

    ## PROCESS

    You will analyze the user's instruction and the provided relevant commands and generate a Unix command that you think most matches the user's query.

    ## OUTPUT CHARACTERISTICS

    Because your output is a command, it needs to be precise and exactly accurate. It should only include the command.

    ## OUTPUT FORMAT

    Your output should be formatted like this.

    {output}

    ## DO NOT

    DO NOT Include anything in your output that isn't the command you think best matches the users query.

    DO NOT Explain why you chose the query you chose.

    DO NOT Include anything in your output that isn't a Unix command.

    DO NOT Explain what the command you selected does.

    ## EXAMPLES

    INPUT: 'go too the root directory'

    OUTPUT: {cd /}

    INPUT: 'list all files including hidden ones'
    OUTPUT: {ls -a}

    INPUT: 'move up one directory'
    OUTPUT: {cd ..}

    INPUT: 'create a new directory called "projects"'
    OUTPUT: {mkdir projects}

    INPUT: 'remove a file named "old_file.txt"'
    OUTPUT: {rm old_file.txt}

    INPUT: 'show the current working directory'
    OUTPUT: {pwd}

    """ 
    print("building llm query", flush=True)
    user = f"Text: {text}\n\nManpages:\n\n" + '\n\n'.join([f"{manpage['command']}\n{manpage['text']}" for manpage in manpages]) 
    print("running llm (final)", flush=True)
    return run_llm(system, user)

class ManpagesDB:
    '''
    This class represents a database of manpages.

    >>> db = ManpagesDB()
    >>> len(db)
    0
    '''
    def __init__(self, filename=':memory:'):
        self.db = sqlite3.connect(filename)
        self.db.row_factory=sqlite3.Row
        self.logger = logging
        self._create_schema()
        self._add_manpages()

    def _create_schema(self):
        '''
        Create the DB schema if it doesn't already exist.

        The test below demonstrates that creating a schema on a database that already has the schema
        will not generate errors.

        >>> db = ManpagesDB()
        >>> db._create_schema()
        >>> db._create_schema()
        '''
        print("creating schema", flush=True)
        try:
            sql = '''
            CREATE VIRTUAL TABLE manpages
            USING FTS5 (
               command,
               text
               );
            '''
            self.db.execute(sql)
            self.db.commit()

        # if the database already exists,
        # then do nothing
        except sqlite3.OperationalError:
            self.logger.debug('CREATE TABLE failed')
        print("schema created", flush=True)

    def _add_manpages(self, directory='manpages'):
        '''
        Adds the manpages in the system memory.
        '''
        print("adding manpages to database", flush=True)
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".txt"):
                    txt_path = os.path.join(root, file)
                    meta_path = os.path.splitext(txt_path)[0] + ".meta"
                    with open(txt_path, "r") as txt_file:
                        manpage_text = txt_file.read()
        
                    if os.path.exists(meta_path):
                        with open(meta_path, "r") as meta_file:
                            command_name = meta_file.read().strip()
                    else:
                        command_name = os.path.splitext(file)[0] # Fallback to file name
        
                    sql = f'''
                    INSERT INTO manpages (command, text)
                    VALUES (?, ?)
                    '''
                    _logsql(sql)
                    cursor = self.db.cursor()
                    cursor.execute(sql, (command_name, manpage_text))
        print("database complete", flush=True)

    def __len__(self):
        sql = '''
        SELECT count(*)
        FROM manpages
        WHERE text IS NOT NULL;
        '''
        _logsql(sql)
        cursor = self.db.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0]
    
    def find_manpages(self, query, limit=2):
        '''
        Return a list of manpages in the database that match the specified query.
        '''
        print("finding manpages", flush=True)
        sql = '''
        SELECT command, text
        FROM manpages
        WHERE manpages MATCH ?
        ORDER BY rank
        LIMIT ?;
        '''
        _logsql(sql)
        cursor = self.db.cursor()
        cursor.execute(sql, (query, limit))
        rows = cursor.fetchall()

        # Get column names from cursor description
        columns = [column[0] for column in cursor.description]
        # Convert rows to a list of dictionaries
        row_dict = [dict(zip(columns, row)) for row in rows]
        print("returning manpages", flush=True)
        return row_dict

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--loglevel', default='warning')
    parser.add_argument('--db', default='manpages.db')
    m_args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=m_args.loglevel.upper(),
        )

    m_db = ManpagesDB(m_args.db)

    while True:
        user_text = input('rag> ')
        if len(user_text.strip()) > 0:
            output = rag(user_text, m_db)
            print(output)
