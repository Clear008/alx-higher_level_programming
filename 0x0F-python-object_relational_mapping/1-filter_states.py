#!/usr/bin/python3
"""script that lists all states with a name starting with N"""

import sys
import MySQLdb


def main():
    """ lists all states start with N """

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], host="localhost", port=3306,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%'
                ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1][0] == "N":
            print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
