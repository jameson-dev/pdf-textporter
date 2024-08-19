import sqlite3
import time


def monitor_db(table):
    last_id = 0
    database = "messages.db"

    con = sqlite3.connect(database)
    cur = con.cursor()

    # Grab the latest entry in the DB
    cur.execute(f"SELECT id FROM {table} ORDER BY ID DESC LIMIT 1")
    for row in cur:
        last_id = int(row[0])
        print(f"Latest ID in database: {last_id}.")

    # Loop to check for new entries
    while True:
        cur.execute(f"SELECT id, message, timestamp FROM {table} WHERE ID > ?",(last_id,))

        # Capture all new rows
        rows = cur.fetchall()
        print("Checking for new rows.")

        if rows:
            # Log new entries to individual files
            for row in rows:
                print(f"ID: {row[0]}, Message: {row[1]}, Timestamp: {row[2]}")
                # Grab timestamp of pager message
                timestamp = row[2]

                # Write each pager message to new file
                with open(f"pager_msg-{timestamp}.log", "x") as file:
                    file.write(row[1])
                    print("File written ", print(row))
                last_id = row[0]
                print("Update last_id: ", last_id)
        # Loop every second

        time.sleep(1)
