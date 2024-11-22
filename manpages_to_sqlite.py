import os
import sqlite3
import re

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

def extract_command_name(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.search(r"4m([A-Za-z0-_-]+)24m", line)
            if match:
                return match.group(1).lower()
        f.seek(0)
        first_30 = f.read(30).strip()
        return f"DEBUG: {first_30}" if first_30 else "DEBUG: EMPTY_FILE"

for root, dirs, files in os.walk(MANPAGES_DIR):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)
            command_name = extract_command_name(file_path)
            with open(file_path, "r", encoding="utf-8") as f:
                manpage_text = f.read()

            cursor.execute("""
            INSERT OR REPLACE INTO manpages (command_name, manpage_text)
            VALUES (?, ?)
            """, (command_name, manpage_text))

conn.commit()
conn.close()

print(f"manpages inserted into {DATABASE_FILE}.")
