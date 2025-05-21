import sqlite3

db_path = 'db.sqlite3'

conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

for table_name in tables:
    table_name = table_name[0]
    if table_name != "sqlite_sequence":
        cursor.execute(f"DROP TABLE {table_name};")
        print(f"Dropped table {table_name}")

conn.commit()
conn.close()

print("All tables dropped successfully.")