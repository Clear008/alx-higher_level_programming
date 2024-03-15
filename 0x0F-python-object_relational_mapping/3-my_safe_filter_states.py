#!/usr/bin/python3
""" write a script that is safe from MySQL injections """

import sys
import MySQLdb


def main():
    """script that is safe from MySQL injections"""

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], host="localhost", port=3306,
                           charset="utf8")
    cur = conn.cursor()
    state_name = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (state_name,))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
