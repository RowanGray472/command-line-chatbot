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


import os
import ollama

# TODO: Add something here that imports the database
# TODO: Make all the prompts good

#################
# LLM FUNCTIONS #
#################

def run_llm(system, user):
    response = ollama.chat(model='llama2', 
                           messages=[
                {
                    'role': 'system',
                    'content': system,
                },
                {
                    "role": "user",
                    "content": user,
                }])
    return(response['message']['content'])



def extract_keywords(text, seed=None):
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

    INPUT: "see the first 10 lines of a file"
    OUTPUT: ['head', 'file', 'lines', 'view']

    INPUT: "see the last 10 lines of a file"
    OUTPUT: ['tail', 'file', 'lines', 'view']

    INPUT: "check which shell I'm using"
    OUTPUT: ['echo', '$SHELL', 'shell', 'current']

    INPUT: "make a new directory"
    OUTPUT: ['mkdir', 'make', 'directory']

    INPUT: "see the current working directory"
    OUTPUT: ['pwd', 'current', 'working', 'directory']

    INPUT: "create an empty file"
    OUTPUT: ['touch', 'create', 'file', 'empty']

    INPUT: "concatenate two files"
    OUTPUT: ['cat', 'concatenate', 'files']

    INPUT: "check running processes"
    OUTPUT: ['ps', 'process', 'running', 'status']

    INPUT: "terminate a process by its ID"
    OUTPUT: ['kill', 'process', 'terminate', 'ID']

    INPUT: "download a file from a URL"
    OUTPUT: ['wget', 'curl', 'download', 'file', 'URL']

    INPUT: "change permissions on a file"
    OUTPUT: ['chmod', 'file', 'permissions', 'change']

    INPUT: "check disk space usage"
    OUTPUT: ['df', 'disk', 'space', 'usage']

    INPUT: "switch to another user"
    OUTPUT: ['su', 'sudo', 'user', 'switch']

    INPUT: "schedule a task to run later"
    OUTPUT: ['cron', 'at', 'schedule', 'task']

    INPUT: "see the history of commands I've used"
    OUTPUT: ['history', 'commands', 'log']

    INPUT: "compare two files for differences"
    OUTPUT: ['diff', 'cmp', 'compare', 'files', 'differences']

    INPUT: "archive files into a single file"
    OUTPUT: ['tar', 'archive', 'file', 'compression']

    INPUT: "extract files from a compressed archive"
    OUTPUT: ['unzip', 'tar', 'gunzip', 'extract', 'archive']

    INPUT: "redirect output of a command to a file"
    OUTPUT: ['>', 'redirect', 'output', 'file']

    INPUT: "pipe output from one command to another"
    OUTPUT: ['|', 'pipe', 'output', 'command']

    INPUT: "check for updates in the package manager"
    OUTPUT: ['apt', 'yum', 'update', 'package', 'manager']

    INPUT: "install a package using a package manager"
    OUTPUT: ['apt-get', 'yum', 'install', 'package', 'manager']

    INPUT: "list all running services"
    OUTPUT: ['systemctl', 'service', 'status', 'running']

    INPUT: "view log files"
    OUTPUT: ['tail', 'log', 'view', 'logs']

    INPUT: "find all files that are larger than 1GB"
    OUTPUT: ['find', 'size', 'greater', '1GB', 'files']

    INPUT: "compress a directory into a .zip file"
    OUTPUT: ['zip', 'compress', 'directory', '.zip', 'file']

    INPUT: "change the owner of a file"
    OUTPUT: ['chown', 'owner', 'file', 'change']

    INPUT: "create a symbolic link to a file"
    OUTPUT: ['ln', 'symbolic', 'link', 'file']

    INPUT: "view the manual for a command"
    OUTPUT: ['man', 'command', 'manual', 'help']

    INPUT: "search through a file for a specific string"
    OUTPUT: ['grep', 'search', 'file', 'string']

    INPUT: "count the number of lines in a file"
    OUTPUT: ['wc', 'count', 'lines', 'file']

    INPUT: "show the first 100 lines of a file"
    OUTPUT: ['head', 'file', 'lines', 'view', '100']

    INPUT: "check the current system time"
    OUTPUT: ['date', 'time', 'current']

    INPUT: "see the usage of a command"
    OUTPUT: ['man', 'help', 'usage', 'command']

    INPUT: "count the number of files in a directory"
    OUTPUT: ['ls', 'count', 'files', 'directory']

    INPUT: "check the available memory on the system"
    OUTPUT: ['free', 'memory', 'system']

    INPUT: "change the group of a file"
    OUTPUT: ['chgrp', 'group', 'file', 'change']

    INPUT: "run a command with superuser privileges"
    OUTPUT: ['sudo', 'superuser', 'privileges', 'command']


    '''

    text = run_llm(system, text)
    return text

def rag(text, db):
    keywords = extract_keywords(text)
    articles = db.find_articles(query = keywords)
    
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

    Include anything in your output that isn't the command you think best matches the users query.

    Explain why you chose the query you chose.

    Include anything in your output that isn't a Unix command.

    ## EXAMPLES



    """ 
    user = f"Text: {text}\n\nArticles:\n\n" + '\n\n'.join([f"{article['command_name']}\n{article['manpage_text']}" for article in articles]) 
    return run_llm(system, user)
