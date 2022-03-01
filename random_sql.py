print("hello!")

# connect to the database
# test the connection! run `SELECT 1`

# execute a few SQL commands:
# create table called 'game' with 3 columns: id, game_name, result
# insert 3 games into table
# select and print the game names of the games which have a result 'won'

import psycopg2

conn = psycopg2.connect("dbname=postgres user=postgres host=0.0.0.0 password=postgres")
cur = conn.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS game (id serial PRIMARY KEY, game_name varchar, result varchar);"
)

cur.execute(
    "INSERT INTO game (game_name, result) VALUES (%s, %s)",
    ("game100", "won"),
)

cur.execute(
    "INSERT INTO game (game_name, result) VALUES (%s, %s)",
    ("game102", "won"),
)

cur.execute("SELECT * FROM game WHERE result = 'won'")
fin = cur.fetchall()
print(fin)
conn.commit()
cur.close()
conn.close()
