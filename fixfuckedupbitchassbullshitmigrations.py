import sqlite3

# Path to your SQLite database file
db_path = 'db.sqlite3'

# Connect to the database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Fetch all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Drop all tables
for table_name in tables:
    table_name = table_name[0]
    if table_name != "sqlite_sequence":  # Skip SQLite's internal table
        cursor.execute(f"DROP TABLE {table_name};")
        print(f"Dropped table {table_name}")

# Commit changes and close the connection
conn.commit()
conn.close()

print("All tables dropped successfully.")