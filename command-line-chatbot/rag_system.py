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

from dotenv import load_dotenv
load_dotenv()
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

def summarize_text(text):
    system = '''

    Summarize the input text below.  Limit the summary to 1 paragraph
    Use an advanced reading level similar to the input text, and ensu
    re that all people, places, and other proper and dates nouns are i
    ncluded in the summary.  The summary should be in English.

    '''
    return run_llm(system, text)


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



    """ # TODO: Fill in examples
    user = f"Text: {text}\n\nArticles:\n\n" + '\n\n'.join([f"{article['title']}\n{article['en_summary']}" for article in articles]) # TODO: make this work with our database
    return run_llm(system, user)
