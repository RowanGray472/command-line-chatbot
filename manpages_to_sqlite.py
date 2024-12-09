import os
import sqlite3

MANPAGES_DIR = "manpages"
DATABASE_FILE = "manpages.db"

conn = sqlite3.connect(DATABASE_FILE)
cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS manpages (
               command_name TEXT PRIMARY KEY,
               manpage_text TEXT
               )
""")
conn.commit()

for root, _, files in os.walk(MANPAGES_DIR):
    for file in files:
        if file.endswith(".txt"):
            txt_path = os.path.join(root, file)
            meta_path = os.path.splitext(txt_path)[0] + ".meta"
            with open(txt_path, "r") as txt_file:
                manpage_text = txt_file.read()

            if os.path.exists(meta_path):
                with open(meta_path, "r") as meta_file:
                    command_name = meta_file.read().strip()
            else:
                command_name = os.path.splitext(file)[0]  # Fallback to file name

            cursor.execute("""
            INSERT INTO manpages (command_name, manpage_text)
            VALUES (?, ?)
            """, (command_name, manpage_text))
conn.commit()
conn.close()

print(f"manpages inserted into {DATABASE_FILE}.")
