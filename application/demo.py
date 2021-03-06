import psycopg2
import os

# Connect to an existing database.
conn = psycopg2.connect(
    user=os.environ.get('POSTGRESQL_USERNAME'),
    password=os.environ.get('POSTGRESQL_PASSWORD'),
    dbname=os.environ.get('POSTGRESQL_DATABASE'),
    host='postgresql',
    port='5432'
)

# Open a cursor to perform database operations.
cur = conn.cursor()

# Execute a command: this creates a new table.
cur.execute("CREATE TABLE IF NOT EXISTS test (id serial PRIMARY KEY, num integer, data varchar);")

# Pass data to fill a query placeholders and let Psycopg perform
# the correct conversion (no more SQL injections!)
cur.execute("INSERT INTO test (num, data) VALUES (%s, %s)", (100, "abc'def"))

# Query the database and obtain data as Python objects.
cur.execute("SELECT * FROM test;")
print(cur.fetchone())

# Make the changes to the database persistent.
conn.commit()

# Close communication with the database.
cur.close()
conn.close()
