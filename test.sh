#!/bin/bash

# Tests!
# $ sudo ./test.sh

script_dir="$(dirname "$BASH_SOURCE")"

sudo ./wrapper.sh -p "Go to the root directory" && cd $script_dir
sudo ./wrapper.sh -p "List all the files, including hidden files, in the current directory" && cd $script_dir
sudo ./wrapper.sh -p "Go to the directory {directory} and display the name of the directory" && cd $script_dir
sudo ./wrapper.sh -p "Create a new directory named \`test_dir\` in the current directory" && cd $script_dir
sudo ./wrapper.sh -p "Delete the directory named \`test_dir\`" && cd $script_dir
sudo ./wrapper.sh -p "Create a text file named \`test_file.txt\` in the current directory" && cd $script_dir
sudo ./wrapper.sh -p "Write the text \"Hello, World!\" into \`test_file.txt\`" && cd $script_dir
sudo ./wrapper.sh -p "Append the text \"Goodbye, World!\" to \`test_file.txt\`" && cd $script_dir
sudo ./wrapper.sh -p "Read and display the contents of \`test_file.txt\`" && cd $script_dir
sudo ./wrapper.sh -p "Rename \`test_file.txt\` to \`renamed_file.txt\`" && cd $script_dir
sudo ./wrapper.sh -p "Copy \`renamed_file.txt\` to \`copied_file.txt\`" && cd $script_dir
sudo ./wrapper.sh -p "Move \`copied_file.txt\` to the directory {directory}" && cd $script_dir
sudo ./wrapper.sh -p "Delete \`renamed_file.txt\`" && cd $script_dir
sudo ./wrapper.sh -p "Display the total number of files in the current directory" && cd $script_dir
sudo ./wrapper.sh -p "Display the size of a specific file {filename} in bytes" && cd $script_dir
sudo ./wrapper.sh -p "Find all files in the current directory with the \`.txt\` extension" && cd $script_dir
sudo ./wrapper.sh -p "Search for the word \"Hello\" in all \`.txt\` files in the current directory" && cd $script_dir
sudo ./wrapper.sh -p "Count the number of lines in \`test_file.txt\`" && cd $script_dir
sudo ./wrapper.sh -p "Display the most recently modified file in the current directory" && cd $script_dir
sudo ./wrapper.sh -p "Display the current working directory path" && cd $script_dir
sudo ./wrapper.sh -p "Create a tar archive named \`backup.tar\` containing all \`.txt\` files in the current directory" && cd $script_dir
sudo ./wrapper.sh -p "Extract the \`backup.tar\` archive into a new directory named \`extracted_backup\`" && cd $script_dir
sudo ./wrapper.sh -p "Find the file named \`bee_movie.txt\` on this computer and search for all the times the word 'bee' appears in it" && cd $script_dir
