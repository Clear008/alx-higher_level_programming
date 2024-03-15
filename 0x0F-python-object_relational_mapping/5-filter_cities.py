#!/usr/bin/python3
""" Takes in the name of a state as an argument and lists all cities of that state """

import sys
import MySQLdb


def main():
    """ lists all cities of a state """

    conn = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3], host="localhost", port=3306,
                           charset="utf8")
    cur = conn.cursor()
    state_name = sys.argv[4]
    cur.execute("""SELECT cities.name FROM cities
                   JOIN states ON cities.state_id=states.id WHERE states.name=%s
                   ORDER BY cities.id ASC""", (state_name,))
    query_rows = cur.fetchall()
    cities = [row[0] for row in query_rows]
    print(", ".join(cities))
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
