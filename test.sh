#!/bin/bash

# Tests!

python3 command-line-chatbot/cli.py --text "Go to the root directory"
python3 command-line-chatbot/cli.py --text "List all the files, including hidden files, in the current directory"
python3 command-line-chatbot/cli.py --text "Go to the directory {directory} and display the name of the directory"
python3 command-line-chatbot/cli.py --text "Create a new directory named \`test_dir\` in the current directory"
python3 command-line-chatbot/cli.py --text "Delete the directory named \`test_dir\`"
python3 command-line-chatbot/cli.py --text "Create a text file named \`test_file.txt\` in the current directory"
python3 command-line-chatbot/cli.py --text "Write the text \"Hello, World!\" into \`test_file.txt\`"
python3 command-line-chatbot/cli.py --text "Append the text \"Goodbye, World!\" to \`test_file.txt\`"
python3 command-line-chatbot/cli.py --text "Read and display the contents of \`test_file.txt\`"
python3 command-line-chatbot/cli.py --text "Rename \`test_file.txt\` to \`renamed_file.txt\`"
python3 command-line-chatbot/cli.py --text "Copy \`renamed_file.txt\` to \`copied_file.txt\`"
python3 command-line-chatbot/cli.py --text "Move \`copied_file.txt\` to the directory {directory}"
python3 command-line-chatbot/cli.py --text "Delete \`renamed_file.txt\`"
python3 command-line-chatbot/cli.py --text "Display the total number of files in the current directory"
python3 command-line-chatbot/cli.py --text "Display the size of a specific file {filename} in bytes"
python3 command-line-chatbot/cli.py --text "Find all files in the current directory with the \`.txt\` extension"
python3 command-line-chatbot/cli.py --text "Search for the word \"Hello\" in all \`.txt\` files in the current directory"
python3 command-line-chatbot/cli.py --text "Count the number of lines in \`test_file.txt\`"
python3 command-line-chatbot/cli.py --text "Display the most recently modified file in the current directory"
python3 command-line-chatbot/cli.py --text "Display the current working directory path"
python3 command-line-chatbot/cli.py --text "Create a tar archive named \`backup.tar\` containing all \`.txt\` files in the current directory"
python3 command-line-chatbot/cli.py --text "Extract the \`backup.tar\` archive into a new directory named \`extracted_backup\`"
python3 command-line-chatbot/cli.py --text "Find the file named \`bee_movie.txt\` on this computer and search for all the times the word 'bee' appears in it"

