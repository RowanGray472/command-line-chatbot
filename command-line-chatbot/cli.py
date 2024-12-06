"""

This file will include all command line outputs/inputs

"""

import os
import argparse
from rag_system import rag, extract_keywords, run_llm, ManpagesDB
import time
import logging
import groq
from groq import Groq

def cli_output(text, db):
    output = rag(text, db) 
    # Simulate typing the command
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.05)  
    # Move to a new line after the command is typed
    print()
    system_output = output[1:-1].strip()
    print(system_output)
    os.system(f'osascript -e \'tell application "Terminal" to do script "{system_output}"\'')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A command-line interface for interacting with the RAG system."
    )

    parser.add_argument('--loglevel', default='warning')

    parser.add_argument(
        "--text", 
        type=str, 
        required=True, 
        help="Input text to process with the RAG system."
    )

    parser.add_argument(
            "--db",
            type=str,
            required=False,
            default='manpages.db',
            help="Path to the database file."
    )

    args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=args.loglevel.upper(),
        )

    db = ManpagesDB(args.db)

    cli_output(args.text, db)
