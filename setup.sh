
# # filesystem setup - run if you're in a VM to update everything and expand root size to max
# sudo apt update && sudo apt upgrade -y
# sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
# sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
# sudo apt install python3.12-venv


# Requirements and groq setup
# first- make a .env file and put your api key in it
# Then- execute these shell commands
# python3 -m venv env
# source env/bin/activate
# pip3 install -r requirements.txt 
# sudo apt install sqlite3


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

# python3 manpages_to_sqlite.py
