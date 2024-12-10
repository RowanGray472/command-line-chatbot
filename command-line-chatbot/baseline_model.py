from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()

"""
This file will contain a baseline model to generate these unix commands. 
No RAG or any other fancy tricks allowed!
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


def command(text):
    system = """
    ## ROLE
    You are a computer program tasked with translating user-entered natural language 
    commands into a Unix machine.
    ## INPUT
    You will be given an instruction from a user in natural language.
    ## PROCESS
    You will analyze the user's instruction and generate a Unix command that you think 
    most matches the user's query.
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
    return run_llm(system, text)

