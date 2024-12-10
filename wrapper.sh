#!/bin/bash

# Export environment
source env/bin/activate
export $(cat .env)

# Usage function
usage() {
    echo "Usage: $0 [-k | --kiddie | -n | --normie | -p | --pro] \"command text\""
    echo "  -k, --kiddie    : Echo the command to run but do not execute it."
    echo "  -n, --normie    : Run the command in a restricted bash (rbash) subshell (default)."
    echo "  -p, --pro       : Run the command with sudo privileges (requires sudo access)."
    echo "  -b, --baseline  : Run the model without RAG."
}

# Function to echo text with a typing effect
typing_echo() {
    local text="$1"
    local delay=0.05  # Adjust this delay as needed
    while IFS= read -r -n1 char; do
        echo -n "$char"
        sleep "$delay"
    done <<< "$text"
    echo  # Move to a new line after the text
}

# Default mode
mode="normie"
cli_mode="rag"

# Parse flags
while [[ $# -gt 0 ]]; do
    case $1 in
        -k|--kiddie)
            mode="kiddie"
            shift
            ;;
        -n|--normie)
            mode="normie"
            shift
            ;;
        -p|--pro)
            mode="pro"
            shift
            ;;
        -b|--baseline)
            mode="baseline"
            cli_mode="baseline"
            shift
            ;;
        --)
            shift
            break
            ;;
        -*)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
        *)
            break
            ;;
    esac
done

# Check if a command text argument is provided
if [ -z "$1" ]; then
    usage
fi

command_text="$1"

# Run the Python script and capture its output
output=$(python3 command-line-chatbot/cli.py --text "$command_text" --mode "$cli_mode")

# Extract the command marked with "!runme:"
command_to_run=$(echo "$output" | perl -nle'print $& while m{(?<=!runme: ).*}g')

# Check if a command was found
if [ -z "$command_to_run" ]; then
    echo "No command found in the Python script output."
    if [ "$BASH_SUBSHELL" -gt 0 ]; then
    echo "Exiting with error in subshell..."
    exit 1
else
    echo "Error encountered, but not exiting main shell."
    return 1
fi

fi

# Execute based on mode
case $mode in
    "kiddie")
        echo "Kiddie mode: Not executing the command."
        typing_echo "$command_to_run"
        ;;
    "normie")
        echo "Normie mode: Running the command in a restricted shell."
        typing_echo "$command_to_run"
        rbash -c "$command_to_run"
        ;;
    "pro")
        echo "Pro mode: Running the command with sudo privileges."
        if ! sudo -n true 2>/dev/null; then
            echo "Error: Sudo privileges are required but not available."
            if [ "$BASH_SUBSHELL" -gt 0 ]; then
                echo "Exiting with error in subshell..."
                exit 1
            else
                echo "Error encountered, but not exiting main shell."
                return 1
            fi

        fi
        typing_echo "$command_to_run"
        sudo bash -c "$command_to_run"
        ;;
    "baseline")
        echo "Baseline model: Not executing command."
        typing_echo "$command_to_run"
        ;;
    *)
        echo "Unknown mode: $mode"
        usage
        ;;
esac
