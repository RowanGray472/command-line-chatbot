## Todos for us

1. ainslee- do all the rights management stuff and make the bash wrapper (pls be functional)
2. rowan/ainslee- fuck around with code org
3. get chatgpt to give us a list of 20 tasks- audit it
4. input all these tasks and make sure they work- also make the files to make this possible
5. document this
6. freestyle mode
7. rowan/ainslee- work on readme
8. whisper integration
9. social media post


## Todos for the computer
```
Input: "Show me all files in the current folder"
Expected: ls
Input: "Show me where I am right now"
Expected: pwd
Input: "Make a folder called projects"
Expected: mkdir projects
Input: "Show all hidden files"
Expected: ls -a
Input: "Copy homework.txt to backup.txt"
Expected: cp homework.txt backup.txt
Input: "Show the first 10 lines of log.txt"
Expected: head -n 10 log.txt
Input: "Find all png files in this directory"
Expected: find . -name "*.png"
Input: "Show me how much disk space I'm using in human readable format"
Expected: df -h
Input: "Search for the word error in all log files"
Expected: grep "error" *.log
Input: "Give everyone execute permissions on script.sh"
Expected: chmod a+x script.sh
Input: "Show me all processes containing the word python"
Expected: ps aux | grep python
Input: "Delete all files ending in .tmp"
Expected: rm *.tmp
Input: "Count how many lines are in data.csv"
Expected: wc -l data.csv
Input: "Show me the last 100 lines of the file and keep updating"
Expected: tail -n 100 -f
Input: "Create a symbolic link from source.txt to link.txt"
Expected: ln -s source.txt link.txt
Input: "Find all files larger than 100MB in the current directory and subdirectories"
Expected: find . -type f -size +100M
Input: "Sort file.txt alphabetically and remove duplicate lines"
Expected: sort file.txt | uniq
Input: "Find all empty directories under current path"
Expected: find . -type d -empty
Input: "Compress all jpg files into archive.tar.gz"
Expected: tar -czf archive.tar.gz *.jpg
Input: "Replace all occurrences of foo with bar in all text files recursively"
Expected: find . -type f -name "*.txt" -exec sed -i 's/foo/bar/g' {} +
```
citations:

claude <3
