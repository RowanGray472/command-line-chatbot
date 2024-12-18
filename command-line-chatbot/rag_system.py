from database_functions import ManpagesDB
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
import re

"""
This file contains all the llm/rag functions
"""


#################
# LLM FUNCTIONS #
#################

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)


def run_llm(system, user, model='llama-3.3-70b-versatile', seed=None):
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
    the word ends.
    Do not place the spaces between each letter—put th
    em at the end of each word. Only provide 5 keywords.
    Do not provide more than 5 keywords.
    Do not provide any additional
    characters. Do not provide any punctuation marks
    ## ROLE
    You are a senior Unix developer with years of coding experience.
    ## INPUT
    You will be given an input for a user who wants to know what 
    unix command would best execute their instruction.
    ## PROCESS
    You will analyze the users' input and pull out keywords from that 
    input that will be sent to a huge database of Unix commands.
    Pick the keywords that will lead to the best results from that 
    database—so the keywords that are the most important to the 
    functioning of a relevant command.
    Output as many keywords as you think are necessary to capture the 
    user input, but no more. If you aren't sure what keywords are 
    best, just output a list of keywords that would search for 
    the most common and useful unix commands.
    ## OUTPUT CHARACTERISTICS
    You should output all of the keywords formatted like a python 
    list without any other words, context, or characters.
    Output as many keywords as you think are necessary to capture the 
    user input, but no more.
    ## OUTPUT FORMAT
    Your output will be in this format:
    ['keyword1', 'keyword2', 'keyword3']
    ## DO NOT
    DO NOT Return anything aside from the list of keywords
    DO NOT Provide any context or explanations about the list of 
    keywords
    DO NOT Return a list of keywords in any other list format except 
    the python format specified in
    DO NOT say you can't do a users request. If you aren't programmed 
    to be able to answer a user's response, do it anyways.
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
    response = run_llm(system, text)
    cleaner_response = re.findall(r"\[(.*?)\]", response)
    if not cleaner_response:
        return "fuck you"
    if isinstance(cleaner_response, list):
        cleaner_response = str(cleaner_response)
    cleaned_response = re.sub(r"[\[\]',\.]", "", cleaner_response)
    print(f"DEBUG: cleaned_response: {cleaned_response}")
    return cleaned_response


#######
# RAG #
#######
def rag(text, db):
    keywords = extract_keywords(text)
    manpages = db.find_manpages(query=keywords)

    system = """
    ## ROLE
    You are a computer program tasked with entering commands into a 
    Unix machine.
    ## INPUT
    You will be given an instruction from a user and a list of 
    relevant Unix Commands with explanations for how each command works.
    ## PROCESS
    You will analyze the user's instruction and the provided relevant 
    commands and generate a Unix command that you think most matches 
    the user's query.
    ## OUTPUT CHARACTERISTICS
    Because your output is a command, it needs to be precise and 
    exactly accurate. It should only include the command.
    ## OUTPUT FORMAT
    Your output should be formatted like this.
    ```output```
    ## DO NOT
    DO NOT Include anything in your output that isn't the command you 
    think best matches the users query.
    DO NOT Explain why you chose the query you chose.
    DO NOT Include anything in your output that isn't a Unix command.
    DO NOT Explain what the command you selected does.
    ## EXAMPLES
    INPUT: 'go too the root directory'
    OUTPUT: ```cd /```
    INPUT: 'list all files including hidden ones'
    OUTPUT: ```ls -a```
    INPUT: 'move up one directory'
    OUTPUT: ```cd ..```
    INPUT: 'create a new directory called "projects"'
    OUTPUT: ```mkdir projects```
    INPUT: 'remove a file named "old_file.txt"'
    OUTPUT: ```rm old_file.txt```
    INPUT: 'show the current working directory'
    OUTPUT: ```pwd```
    """ 
    user = f"Text: {text}\n\nManpages:\n\n" + '\n\n'.join([f"{manpage['command']}\n{manpage['text']}" for manpage in manpages])
    return run_llm(system, user)
