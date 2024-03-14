#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb


def main():
    """ main function"""

    conn = MySQLdb.connect(mysql_username="root", mysql_password="root",
                           database_name="my_db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
