"""

This file will include all command line outputs/inputs

"""

import os
import argparse
from rag_system import rag, extract_keywords, summarize_text, run_llm

def cli_output(text):
    output = rag(text)
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

    args = parser.parse_args()

    cli_output(args.text)

