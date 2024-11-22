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
for i in `find /usr/share/man -name '*.gz'`; do
    dname=$(dirname $i)
    mkdir -p "$OUT_DIR/$dname"
    zcat "$i" | soelim | tbl | groff -mandoc -Tutf8 | col -b > "$OUT_DIR/$i.txt"
done

python3 manpages_to_sqlite.py
