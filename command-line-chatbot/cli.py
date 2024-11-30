"""

This file will include all command line outputs/inputs

"""

import os
import argparse
from rag_system import rag, extract_keywords, run_llm
import time
import ollama

def cli_output(text):
    output = rag(text) 

    # Simulate typing the command
    for char in output:
        print(char, end='', flush=True)
        time.sleep(0.05)  
        print()
    os.system(output)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A command-line interface for interacting with the RAG system."
    )

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
            help="Path to the database file."
    )

    args = parser.parse_args()

    cli_output(args.text)
