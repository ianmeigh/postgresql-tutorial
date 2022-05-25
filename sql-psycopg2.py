import psycopg2

DB_NAME = "chinook"

try:
    # Connect to the "chinook" database
    connection = psycopg2.connect(database=DB_NAME)
    print("Connection successful")
except:
    print("Connection failed")

# Build a cursor object of the database
cursor = connection.cursor()

# Query 1 - Select all records from the "Artist" table
# cursor.execute('SELECT * FROM "Artist"')

# Query 2 - select only the "Name" colum from the "Artist" table
# cursor.execute('SELECT "Name" FROM "Artist"')

# Query 3 - select only "Queen" from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "Name"=%s', ["Queen"])

# Query 3.1 - select matching artists ("Queen" and "AC/DC") from the "Artist"
# table

# sql = 'SELECT * FROM "Artist" WHERE "Name" IN %s'
# data = ("Queen", "AC/DC")
# cursor.execute(sql, (data,))

# Query 4 - select only by "ArtistId" #51 from the "Artist" table
# cursor.execute('SELECT * FROM "Artist" WHERE "ArtistId" = %s', [51])

# Query 5 - select only the albums with "ArtistId" #51 on the "Album" table
# cursor.execute('SELECT * FROM "Album" WHERE "ArtistId" = %s', [51])

# Query 5 - select all tracks where the composer is "Queen" from the "Track"
#  table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["Queen"])

# Challenge 1 - select all tracks where the composer is "Queen" from the
# "Track" table
# cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["AC/DC"])

# Challenge 1 - select all tracks where the composer is "Queen" from the
# "Track" table
cursor.execute('SELECT * FROM "Track" WHERE "Composer" = %s', ["test"])

# Fetch the results (multiple)
results = cursor.fetchall()

# Fetch the result (single)
# results = cursor.fetchone()

# Close the connection
connection.close()

# Print the results
for result in results:
    print(result)

print(len(results))

# Enumerate practice
# for index, value in enumerate(results):
#     print(index, value)
