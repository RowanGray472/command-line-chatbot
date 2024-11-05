# command-line-chatbot
 
This repo will contain a chatbot that can interact with your command line and help you with system administration.

1. In which we pipe an LLM into /bin/bash and see what happens
1. [Rowan](https://github.com/RowanGray472) and [Ainslee](https://github.com/ains-arch)
1. Outline
    1. LLaMa model (run locally! don't give an LLM free reign over your computer AND connect it to
       someone else's cloud; you gotta pick one bad decision at a time)
    1. RAG system with man pages (either something we download from somewhere or something that
       can query the place where man pages live on the os)
    1. whisper for verbal interface
    1. grammar to help the summary engine work better
    1. something that can be queried from the command line for text interface
    1. system/user prompt fiddling to make it less likely to break your computer
    1. finetuning to make it less likely to break your computer
1. Sources/inspiration
[initial X thread](https://x.com/bshlgrs/status/1840577720465645960),
[log](https://gist.github.com/bshlgrs/57323269dce828545a7edeafd9afa7e8),
[demo](https://www.dropbox.com/scl/fi/a3ellhrgmbn9r8ximrbcd/buck-scaffold-demo.mov?rlkey=4cb2ws4xtlpezlh0q7sxa9gcy&e=2&st=fdxpp422&dl=0),
[news coverage](https://www.theregister.com/2024/10/02/ai_agent_trashes_pc/)
