#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states table
   of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb

def main():
    """Searches for states in the database that match the given state name"""

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], host="localhost", port=3306,
                           charset="utf8")
    cur = conn.cursor()
    state_name = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
