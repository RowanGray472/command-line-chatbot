## Goals for this project

We aim to construct a voice-assisted chatbot for command-line interface. This bot will take user
voice and text input and will be enabled to take action on the computer directly via bash.

The goals of this system are to

1. Enable users who are new to unix commands to get a better understanding of how they work
1. Enable experienced users to automate annoying administrative tasks
1. Most likely, serve as a cautionary tale for why one should not do this

In light of those goals, the system should be both easy to interact with and highly functional.
In the likely outcome that it isn't, it should come with sufficient warning labels.

## Structure of the project

### Database

We will construct the database in SQLite3 from online databases of unix commands. We'll take
inspiration from those databases on structure.

Alternatively, we can set it up so it can directly query the man pages on your machine. This will
require a few more steps - manpages are stored in `nroff`, so we'd need to [convert them to
text](https://stackoverflow.com/questions/13433903/convert-all-linux-man-pages-to-text-html-or-markdown)
I suspect it'd be better to store these textfiles in database of some kind, but I'd be curious to
try [using grep on the directory we store the text files
in](https://stackoverflow.com/questions/16956810/find-all-files-containing-a-specific-text-string-on-linux).
I suspect it'd take longer, but it's possible with this little data the difference would be
negligible and we could save ourselves a database project.

### RAG System

We will then build a RAG system that will give our LLM access to the parts of the unix command
database most relevant for the user query. We'll just use SQL queries and LLM summarization for
this, and we'll build that entirely in-house.

We'll need to be careful that any summarization steps preserve syntax aspects of the manpage. It may
be better to instead be stricter on which manpages match the query and provide all of those pages,
rather than providing more pages via summary.

### LLM

Haven't decided on model choice yet or provider. Probably will go with groq because it's fast and
cheap but our requirements for reliable output formatting might make chatgpt inevitable.

I'd like to pitch using LLaMa so this can all be done locally. I think that would be a real
improvement on the Claude-based inspiration - I personally would be willing to take a hit on
accuracy in order to not be sending potentially sensitive information about my computer to an AI
company's data center.

### Whisper System

We'll build voice integration using whisper.cpp to establish a (partial) unix command grammar that
will take user voice input and parse it as a quasi-unix command. We'll start with just doing voice
recognition without grammar, then build from there as necessary to improve the query text. Our goal
is for the user to be able to describe the command they want in natural language, not to have to
already have memorized syntax.

### Text System

We'll set up our program so that, when run with different flags, the user can sidestep the Whisper
integration and just directly enter a prompt to be passed to the summarization and RAG system. From
there it will continue the same.

### Integration

The output from the whisper system will get passed to the RAG system, potentially with a
summarization step in order to distill the keywords for querying. Then, the original user request
and the output of the RAG system will go to our LLM. Initially, we will start with including in the
system prompt instructions on how to interact with the command line (i.e., "Anything within \` \`
will be run."). If necessary, we will further constrain responses using LMQL. We will provide the
output of any commands run back to the LLM, so it can take further action as necessary.

### Deployment

The output will be entered directly into the command line by the program. In order to make sure we
don't actually delete our operating systems while doing this we'll have to set up a virtual machine
and test the program in there.
