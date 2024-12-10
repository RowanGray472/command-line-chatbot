# command-line-chatbot

![Tests](https://github.com/RowanGray472/cs181hw1/actions/workflows/tests.yml/badge.svg)
 
This repo contains a chatbot that can interact with your command line and help you with system administration.

By [Rowan](https://github.com/RowanGray472) and [Ainslee](https://github.com/ains-arch)


## Quick Demo

Here's a short demo to give you an idea of what this sytsem can do when it's fully functional.
Say you wanted to go to your home directory, but you forgot the unix command for how to do that.
Sure, you *could* go plug it into google, or you could use this product to just do it directly.

Here's how that workflow goes.
You go to your terminal, type `whatever you type` to turn on the bot, and enter your natural-language instruction.
Then, the machine cooks, and runs the command for you.

Here's what that might look like for our home directory example.

```
paste example here
```

    > **NOTE:**
    > This system, since it relies on llms, is nondeterministic. 
    > You *will not* get the same results every time from the same command. 


## More Technical Explanation

Here's a more technical explanation of what's going on than what we gave up top.
We're using a RAG setup to augment the abilities of the llama model as called by the groq api.
Our setup script creates a database on your computer that contains all the manpages for whatever functions you have installed.
Once you call the bot, it analyzes your request to search for keywords with which to query the database.
It gets the top two most relevant pages from the database (where relevance is defined by the FTS5 algorithm)
Then it uses those two pages, your input, and our engineered prompt to generate a short shell script.
    > PUT REST OF EXPLANATION HERE ONCE AINSLEE FINISHES STUFF


## Full Setup Instructions

Setting this up is pretty easy, and even easier if you trust us enough to run a shell script we made.
Once you pull the repo, make a .env file and store your free groq api key in it.
You can get that key [here](https://console.groq.com/keys).
Get into that environment by running

```
python3 -m venv env
source env/bin/activate
```

Then, make setup.sh executable and run it using

```
chmod +x setup.sh
./setup.sh
```

This will setup your manpages database.
Now you're all ready to go! Make queries using
    > PUT REST HERE ONCE AINLEE FINISHES

4. more full demo



5. tests/results



