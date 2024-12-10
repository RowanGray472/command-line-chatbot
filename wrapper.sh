#!/bin/bash

# Check if an argument was passed
if [ -z "$1" ]; then
    echo "Usage: $0 \"command text\""
fi

# Run the Python script and capture its output
output=$(python3 command-line-chatbot/cli.py --text "$1")

# Debug: print the full output for verification
echo "Full Python script output:"
echo "$output"

# Extract the command marked with "!runme:"
command_to_run=$(echo "$output" | perl -nle'print $& while m{(?<=!runme: ).*}g')

# Check if a command was found
if [ -z "$command_to_run" ]; then
    echo "No command found in the Python script output."
    exit 1
fi

# Debug: print the extracted command for verification
echo "Command to run: $command_to_run"

# Execute the extracted command in the current shell
eval "$command_to_run"
