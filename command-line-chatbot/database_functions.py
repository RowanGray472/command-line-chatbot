import logging
import sqlite3
import re
import os
from dotenv import load_dotenv
load_dotenv()

####################
# HELPER FUNCTIONS #
####################


def _logsql(sql):
    rex = re.compile(r'\W+')
    sql_dewhite = rex.sub(' ', sql)
    logging.debug("SQL: %s", sql_dewhite)

######################
# DATABASE FUNCTIONS #
######################


class ManpagesDB:
    '''
    This class represents a database of manpages.

    >>> db = ManpagesDB()
    >>> len(db)
    0
    '''
    def __init__(self, filename=':memory:'):
        self.db = sqlite3.connect(filename)
        self.db.row_factory = sqlite3.Row
        self.logger = logging
        self._create_schema()
        self._add_manpages()

    def _create_schema(self):
        '''
        Create the DB schema if it doesn't already exist.

        The test below demonstrates that creating a schema on a database that already has the schema
        will not generate errors.

        >>> db = ManpagesDB()
        >>> db._create_schema()
        >>> db._create_schema()
        '''
        try:
            sql = '''
            CREATE VIRTUAL TABLE manpages
            USING FTS5 (
               command,
               text
               );
            '''
            self.db.execute(sql)
            self.db.commit()

        # if the database already exists,
        # then do nothing
        except sqlite3.OperationalError:
            self.logger.debug('CREATE TABLE failed')

    def _add_manpages(self, directory='manpages'):
        '''
        Adds the manpages in the system memory.
        '''
        for root, _, files in os.walk(directory):
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

                    sql = '''
                    INSERT INTO manpages (command, text)
                    VALUES (?, ?)
                    '''
                    _logsql(sql)
                    cursor = self.db.cursor()
                    cursor.execute(sql, (command_name, manpage_text))

    def __len__(self):
        sql = '''
        SELECT count(*)
        FROM manpages
        WHERE text IS NOT NULL;
        '''
        _logsql(sql)
        cursor = self.db.cursor()
        cursor.execute(sql)
        row = cursor.fetchone()
        return row[0]

    def find_manpages(self, query, limit=2):
        '''
        Return a list of manpages in the database that match the specified query.
        '''
        sql = '''
        SELECT command, text
        FROM manpages
        WHERE manpages MATCH ?
        ORDER BY rank
        LIMIT ?;
        '''
        _logsql(sql)
        cursor = self.db.cursor()
        cursor.execute(sql, (query, limit))
        rows = cursor.fetchall()

        # Get column names from cursor description
        columns = [column[0] for column in cursor.description]
        # Convert rows to a list of dictionaries
        row_dict = [dict(zip(columns, row)) for row in rows]
        return row_dict


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--loglevel', default='warning')
    parser.add_argument('--db', default='manpages.db')
    m_args = parser.parse_args()

    logging.basicConfig(
        format='%(asctime)s %(levelname)-8s %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        level=m_args.loglevel.upper(),
        )

    m_db = ManpagesDB(m_args.db)

    while True:
        user_text = input('rag> ')
        if len(user_text.strip()) > 0:
            output = rag(user_text, m_db)
