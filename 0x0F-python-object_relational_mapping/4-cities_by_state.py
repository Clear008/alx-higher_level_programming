#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """

import sys
import MySQLdb


def main():
    """ lists all cities """

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], host="localhost", port=3306,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities
                   JOIN states ON cities.state_id=states.id
                   ORDER BY cities.id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
