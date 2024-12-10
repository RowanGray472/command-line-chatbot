#!/bin/bash

# Tests!
# $ sudo ./test.sh

script_dir="$(dirname "$BASH_SOURCE")"

echo "KIDDIE MODE"
echo "Go to the root directory" 
source ./wrapper.sh -k "Go to the root directory"
echo "List all the files, including hidden files, in the current directory" 
source ./wrapper.sh -k "List all the files, including hidden files, in the current directory"
echo "Go to the directory /usr/share and display the name of the directory" 
source ./wrapper.sh -k "Go to the directory /usr/share and display the name of the directory"
echo "Create a new directory named \`test_dir\` in the current directory" 
source ./wrapper.sh -k "Create a new directory named \`test_dir\` in the current directory"
echo "Delete the directory named \`test_dir\`" 
source ./wrapper.sh -k "Delete the directory named \`test_dir\`"
echo "Create a text file named \`test_file.txt\` in the current directory" 
source ./wrapper.sh -k "Create a text file named \`test_file.txt\` in the current directory"
echo "Write the text \"Hello, World!\" into \`test_file.txt\`" 
source ./wrapper.sh -k "Write the text \"Hello, World!\" into \`test_file.txt\`"
echo "Append the text \"Goodbye, World!\" to \`test_file.txt\`" 
source ./wrapper.sh -k "Append the text \"Goodbye, World!\" to \`test_file.txt\`"
echo "Read and display the contents of \`test_file.txt\`" 
source ./wrapper.sh -k "Read and display the contents of \`test_file.txt\`"
echo "Rename \`test_file.txt\` to \`renamed_file.txt\`" 
source ./wrapper.sh -k "Rename \`test_file.txt\` to \`renamed_file.txt\`"
echo "Copy \`renamed_file.txt\` to \`copied_file.txt\`" 
source ./wrapper.sh -k "Copy \`renamed_file.txt\` to \`copied_file.txt\`"
echo "Move \`copied_file.txt\` to the directory {directory}" 
source ./wrapper.sh -k "Move \`copied_file.txt\` to the directory {directory}"
echo "Delete \`renamed_file.txt\`" 
source ./wrapper.sh -k "Delete \`renamed_file.txt\`"
echo "Display the total number of files in the current directory" 
source ./wrapper.sh -k "Display the total number of files in the current directory"
echo "Display the size of a specific file setup.sh in bytes" 
source ./wrapper.sh -k "Display the size of a specific file setup.sh in bytes"
echo "Find all files in the current directory with the \`.txt\` extension" 
source ./wrapper.sh -k "Find all files in the current directory with the \`.txt\` extension"
echo "Search for the word \"Hello\" in all \`.txt\` files in the current directory" 
source ./wrapper.sh -k "Search for the word \"Hello\" in all \`.txt\` files in the current directory"
echo "Count the number of lines in \`test_file.txt\`" 
source ./wrapper.sh -k "Count the number of lines in \`test_file.txt\`"
echo "Display the most recently modified file in the current directory" 
source ./wrapper.sh -k "Display the most recently modified file in the current directory"
echo "Display the current working directory path" 
source ./wrapper.sh -k "Display the current working directory path"
echo "Create a tar archive named \`backup.tar\` containing all \`.txt\` files in the current directory" 
source ./wrapper.sh -k "Create a tar archive named \`backup.tar\` containing all \`.txt\` files in the current directory"
echo "Extract the \`backup.tar\` archive into a new directory named \`extracted_backup\`" 
source ./wrapper.sh -k "Extract the \`backup.tar\` archive into a new directory named \`extracted_backup\`"
echo "Find the file named \`bee_movie.txt\` on this computer and search for all the times the word 'bee' appears in it" 
source ./wrapper.sh -k "Find the file named \`bee_movie.txt\` on this computer and search for all the times the word 'bee' appears in it"

echo "NORMIE MODE"
echo "Go to the root directory" 
source ./wrapper.sh "Go to the root directory" && cd $script_dir
echo "List all the files, including hidden files, in the current directory" 
source ./wrapper.sh "List all the files, including hidden files, in the current directory" && cd $script_dir
echo "Go to the directory /usr/share and display the name of the directory" 
source ./wrapper.sh "Go to the directory /usr/share and display the name of the directory" && cd $script_dir
echo "Create a new directory named \`test_dir\` in the current directory" 
source ./wrapper.sh "Create a new directory named \`test_dir\` in the current directory" && cd $script_dir
echo "Delete the directory named \`test_dir\`" 
source ./wrapper.sh "Delete the directory named \`test_dir\`" && cd $script_dir
echo "Create a text file named \`test_file.txt\` in the current directory" 
source ./wrapper.sh "Create a text file named \`test_file.txt\` in the current directory" && cd $script_dir
echo "Write the text \"Hello, World!\" into \`test_file.txt\`" 
source ./wrapper.sh "Write the text \"Hello, World!\" into \`test_file.txt\`" && cd $script_dir
echo "Append the text \"Goodbye, World!\" to \`test_file.txt\`" 
source ./wrapper.sh "Append the text \"Goodbye, World!\" to \`test_file.txt\`" && cd $script_dir
echo "Read and display the contents of \`test_file.txt\`" 
source ./wrapper.sh "Read and display the contents of \`test_file.txt\`" && cd $script_dir
echo "Rename \`test_file.txt\` to \`renamed_file.txt\`" 
source ./wrapper.sh "Rename \`test_file.txt\` to \`renamed_file.txt\`" && cd $script_dir
echo "Copy \`renamed_file.txt\` to \`copied_file.txt\`" 
source ./wrapper.sh "Copy \`renamed_file.txt\` to \`copied_file.txt\`" && cd $script_dir
echo "Move \`copied_file.txt\` to the directory {directory}" 
source ./wrapper.sh "Move \`copied_file.txt\` to the directory {directory}" && cd $script_dir
echo "Delete \`renamed_file.txt\`" 
source ./wrapper.sh "Delete \`renamed_file.txt\`" && cd $script_dir
echo "Display the total number of files in the current directory" 
source ./wrapper.sh "Display the total number of files in the current directory" && cd $script_dir
echo "Display the size of a specific file setup.sh in bytes" 
source ./wrapper.sh "Display the size of a specific file setup.sh in bytes" && cd $script_dir
echo "Find all files in the current directory with the \`.txt\` extension" 
source ./wrapper.sh "Find all files in the current directory with the \`.txt\` extension" && cd $script_dir
echo "Search for the word \"Hello\" in all \`.txt\` files in the current directory" 
source ./wrapper.sh "Search for the word \"Hello\" in all \`.txt\` files in the current directory" && cd $script_dir
echo "Count the number of lines in \`test_file.txt\`" 
source ./wrapper.sh "Count the number of lines in \`test_file.txt\`" && cd $script_dir
echo "Display the most recently modified file in the current directory" 
source ./wrapper.sh "Display the most recently modified file in the current directory" && cd $script_dir
echo "Display the current working directory path" 
source ./wrapper.sh "Display the current working directory path" && cd $script_dir
echo "Create a tar archive named \`backup.tar\` containing all \`.txt\` files in the current directory" 
source ./wrapper.sh "Create a tar archive named \`backup.tar\` containing all \`.txt\` files in the current directory" && cd $script_dir
echo "Extract the \`backup.tar\` archive into a new directory named \`extracted_backup\`" 
source ./wrapper.sh "Extract the \`backup.tar\` archive into a new directory named \`extracted_backup\`" && cd $script_dir
echo "Find the file named \`bee_movie.txt\` on this computer and search for all the times the word 'bee' appears in it" 
source ./wrapper.sh "Find the file named \`bee_movie.txt\` on this computer and search for all the times the word 'bee' appears in it" && cd $script_dir

echo "PRO MODE"
echo "Go to the root directory" 
sudo ./wrapper.sh -p "Go to the root directory" && cd $script_dir
echo "List all the files, including hidden files, in the current directory" 
sudo ./wrapper.sh -p "List all the files, including hidden files, in the current directory" && cd $script_dir
echo "Go to the directory /usr/share and display the name of the directory" 
sudo ./wrapper.sh -p "Go to the directory /usr/share and display the name of the directory" && cd $script_dir
echo "Create a new directory named \`test_dir\` in the current directory" 
sudo ./wrapper.sh -p "Create a new directory named \`test_dir\` in the current directory" && cd $script_dir
echo "Delete the directory named \`test_dir\`" 
sudo ./wrapper.sh -p "Delete the directory named \`test_dir\`" && cd $script_dir
echo "Create a text file named \`test_file.txt\` in the current directory" 
sudo ./wrapper.sh -p "Create a text file named \`test_file.txt\` in the current directory" && cd $script_dir
echo "Write the text \"Hello, World!\" into \`test_file.txt\`" 
sudo ./wrapper.sh -p "Write the text \"Hello, World!\" into \`test_file.txt\`" && cd $script_dir
echo "Append the text \"Goodbye, World!\" to \`test_file.txt\`" 
sudo ./wrapper.sh -p "Append the text \"Goodbye, World!\" to \`test_file.txt\`" && cd $script_dir
echo "Read and display the contents of \`test_file.txt\`" 
sudo ./wrapper.sh -p "Read and display the contents of \`test_file.txt\`" && cd $script_dir
echo "Rename \`test_file.txt\` to \`renamed_file.txt\`" 
sudo ./wrapper.sh -p "Rename \`test_file.txt\` to \`renamed_file.txt\`" && cd $script_dir
echo "Copy \`renamed_file.txt\` to \`copied_file.txt\`" 
sudo ./wrapper.sh -p "Copy \`renamed_file.txt\` to \`copied_file.txt\`" && cd $script_dir
echo "Move \`copied_file.txt\` to the directory {directory}" 
sudo ./wrapper.sh -p "Move \`copied_file.txt\` to the directory {directory}" && cd $script_dir
echo "Delete \`renamed_file.txt\`" 
sudo ./wrapper.sh -p "Delete \`renamed_file.txt\`" && cd $script_dir
echo "Display the total number of files in the current directory" 
sudo ./wrapper.sh -p "Display the total number of files in the current directory" && cd $script_dir
echo "Display the size of a specific file setup.sh in bytes" 
sudo ./wrapper.sh -p "Display the size of a specific file setup.sh in bytes" && cd $script_dir
echo "Find all files in the current directory with the \`.txt\` extension" 
sudo ./wrapper.sh -p "Find all files in the current directory with the \`.txt\` extension" && cd $script_dir
echo "Search for the word \"Hello\" in all \`.txt\` files in the current directory" 
sudo ./wrapper.sh -p "Search for the word \"Hello\" in all \`.txt\` files in the current directory" && cd $script_dir
echo "Count the number of lines in \`test_file.txt\`" 
sudo ./wrapper.sh -p "Count the number of lines in \`test_file.txt\`" && cd $script_dir
echo "Display the most recently modified file in the current directory" 
sudo ./wrapper.sh -p "Display the most recently modified file in the current directory" && cd $script_dir
echo "Display the current working directory path" 
sudo ./wrapper.sh -p "Display the current working directory path" && cd $script_dir
echo "Create a tar archive named \`backup.tar\` containing all \`.txt\` files in the current directory" 
sudo ./wrapper.sh -p "Create a tar archive named \`backup.tar\` containing all \`.txt\` files in the current directory" && cd $script_dir
echo "Extract the \`backup.tar\` archive into a new directory named \`extracted_backup\`" 
sudo ./wrapper.sh -p "Extract the \`backup.tar\` archive into a new directory named \`extracted_backup\`" && cd $script_dir
echo "Find the file named \`bee_movie.txt\` on this computer and search for all the times the word 'bee' appears in it" 
sudo ./wrapper.sh -p "Find the file named \`bee_movie.txt\` on this computer and search for all the times the word 'bee' appears in it" && cd $script_dir
