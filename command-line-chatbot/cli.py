import argparse
import time
import re

# Import your RAG and Baseline modules
from rag_system import rag, ManpagesDB
from baseline_model import command

def cli_output(text, db, mode):
    if mode == "rag":
        output = rag(text, db)
    elif mode == "baseline":
        output = command(text)
    else:
        raise ValueError(f"Unknown mode: {mode}")

    if "```" in output:
        system_output = re.findall(r"```(.*?)```", output, re.DOTALL)
        system_output = str(system_output[0])
    else:
        system_output = output
    print(f"!runme: {system_output}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A command-line interface for interacting with the RAG system."
    )

    parser.add_argument('--loglevel', default='warning')

    parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="Input text to process with the RAG or Baseline system."
    )

    parser.add_argument(
        "--mode",
        type=str,
        default="rag",
        choices=["rag", "baseline"],
        help="Mode to run the system: 'rag' or 'baseline'."
    )

    parser.add_argument(
        "--db",
        type=str,
        required=False,
        default='manpages.db',
        help="Path to the database file."
    )

    args = parser.parse_args()

    db = ManpagesDB(args.db)

    cli_output(args.text, db, args.mode)
