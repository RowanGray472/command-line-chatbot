## Goals for this project

We aim to construct a voice-assisted chatbot for command-line interface. This bot will take user voice input and will type and submit its output directly in the command line. 

The goals of this system are to

1. Enable users who are new to unix commands to get a better understanding of how they work
2. Enable experienced users to automate annoying administrative tasks

In light of those goals, the system should be both easy to interact with and highly functional.

## Structure of the project

### Database

We will construct the database in SQLite3 from online databases of unix commands. We'll take inspiration from those databases on structure.

### RAG System

We will then build a RAG system that will give our LLM access to the parts of the unix command database most relevant for the user query. We'll just use SQL queries and LLM summarization for this, and we'll build that entirely in-house.

### LLM

Haven't decided on model choice yet or provider. Probably will go with groq because it's fast and cheap but our requirements for reliable output formatting might make chatgpt inevitable.

### Whisper System

We'll build a voice recognition using whisper.cpp to establish a (partial) unix command grammar that will take user voice input and parse it as a quasi-unix command.

### Integration

The output from the whisper system will get passed to the RAG system. Then, that query and the output of the RAG system will go to our LLM, whose output we might constrict using LMQL to ensure it's something at least close to valid query.

### Deployment

The output will be entered directly into the command line by the program. In order to make sure we don't actually delete our operating systems while doing this we'll have to set up a virtual machine and test the program in there.

We also plan on enabling text input for users who don't have microphones, find voice input annoying, or work in crowded or noisy spaces.
