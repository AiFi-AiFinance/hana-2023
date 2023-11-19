
import psycopg2
connection = psycopg2.connect(host="34.42.241.68", dbname="hana-2023-database", user="postgres", password="1234", port=5432)
cur = connection.cursor()
cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
connection.commit()
cur.execute("INSERT INTO test (id, num, data) VALUES (%s, %s, %s);",
        (1, 100, "data01")
        )
cur.execute("SELECT * FROM test")
(id, num, data) = cur.fetchone()
print(f"{id}, {num}, {data}")
cur.close()
connection.close()