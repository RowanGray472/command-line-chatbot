# CLIFF

![Tests](https://github.com/RowanGray472/cs181hw1/actions/workflows/tests.yml/badge.svg)
 
This repo contains a chatbot that can interact with your command line and help you with system administration.
It's named CLIFF- which stands for Command Line Interface Friendly Facilitator.
CLIFF uses RAG to familiarize the `llama-3.3-70b-versatile` model with Unix commands.

By [Rowan](https://github.com/RowanGray472) and [Ainslee](https://github.com/ains-arch)


## Quick Demo

Here's a short demo to give you an idea of what CLIFF can do when it's fully functional.
Say you wanted to go to your home directory, but you forgot the command for how to do that.
Sure, you *could* go plug it into google, or you could use CLIFF  to just do it directly.

Here's how that workflow goes for our home directory example.

```
$ source env/bin/activate
$ source ./wrapper.sh -p "go to the root directory"
$ 
```

> **NOTE:**
> CLIFF, since it relies on llms, is nondeterministic. 
> You *will not* get the same results every time from the same command. 


## Full Setup Instructions/Demo

Setting this up is pretty easy, and even easier if you trust us enough to run a shell script we made.
Once you pull the repo, make a .env file and store your free groq api key in it.
You can get that key [here](https://console.groq.com/keys).
Get into that environment by running

```
$ python3 -m venv env
$ source env/bin/activate
```

Then, make setup.sh executable and run it using

```
$ chmod +x setup.sh
$ ./setup.sh
```

This will setup your manpages database.

> **NOTE**:
> If you want to directly query the manpage database you made you'll need to sudo apt install sqlite

Now make sure our wrapper script is executable using

```
$ chmod +x wrapper.sh
```

Now you're all ready to go! 
Make queries using one of our three modes- kiddie, normie and pro.

On kiddie mode, CLIFF won't enter into your command line, it'll just print a line you copy into your command line if you want to run it.
On normie mode, CLIFF opens a new rbash shell where it can access the command line, but can only read files, not analyze them.
It also has pretty limited capabilities to move around your computer.
On pro mode the model can do anything. 
Be careful!

Here's what implementing the three modes looks like- the flags correspond to the modes.

```
$ source ./wrapper.sh -k "your query"
$ source ./wrapper.sh -n "your query"
$ sudo ./wrapper.sh -p "your query"
```

## Tests and Results

Here, we'll show off some of CLIFF's capabilities.



## More Technical Explanation

Here's a more technical explanation of what's going on than what we gave up top.
We're using a RAG setup to augment the abilities of the llama model as called by the groq api.
Our setup script creates a database on your computer that contains all the manpages for whatever functions you have installed.

Once you call the bot, it analyzes your request to search for keywords with which to query the database.
It gets the top two most relevant pages from the database (where relevance is defined by the FTS5 algorithm)
Then it uses those two pages, your input, and our engineered prompt to generate a short shell script.

Then, our wrapper extract that generated script and checks what mode we're in—if we're in kiddie mode it just prints the statement, if we're in normie mode it opens a new rbash terminal and runs it, if we're in pro mode it just runs the statement in your current terminal with all permissions.


