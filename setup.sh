# This file will contain all of our setup.
# Specifically-
# Code that creates the database automatically based on your man pages
# Code that installs a llama model and gets it ready to go on your computer


# ollama setup

curl -fsSL https://ollama.com/install.sh | sh
ollama pull llama2

# database setup

OUT_DIR=./manpages
rm -rf $OUT_DIR
mkdir $OUT_DIR

for cmd in $(compgen -c | sort -u); do
    if man "$cmd" &>/dev/null; then # if manpage exists
        # Create manpage text, remove backspace/underscores, remove line numbers
        man "$cmd" | col -bx | sed 's/^ *[0-9]* *//' > "$OUT_DIR/$cmd.txt"

        # Store command name in meta file
        echo "$cmd" > "$OUT_DIR/$cmd.meta"
    else
        echo "No manpage for $cmd" >> "$OUT_DIR/missing_commands.log"
    fi
done
OUT_DIR=./manpages

python3 manpages_to_sqlite.py
