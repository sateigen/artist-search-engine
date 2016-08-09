import psycopg2
import csv

conn = psycopg2.connect("dbname=artists user=shannon")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS artists(id serial PRIMARY KEY, Artist varchar(30), Title varchar(90), Year integer, Medium varchar(30), Subject varchar(15), Collection varchar(15))")


with open("artwork.csv", 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        cur.execute("INSERT INTO artists (Artist, Title, Year, Medium, Subject, Collection) VALUES(%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))
    conn.commit()
    cur.close()
