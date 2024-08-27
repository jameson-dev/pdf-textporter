import sqlite3
import sys
import time
import os
from loguru import logger
from config import read_config
from generate_pdf import create_temp_pdf


def monitor_db(table):
    last_id = 0

    config_values = read_config()

    db_path = config_values['db_path']
    db_file = config_values['db_file']
    full_path = os.path.join(db_path, db_file)

    if os.path.isfile(full_path):
        logger.info(f"Database file found.")
        con = sqlite3.connect(full_path)
        cur = con.cursor()
    else:
        logger.error(f"Database file not found: {full_path}. Exiting.")
        sys.exit()

    # Grab the latest entry in the DB
    cur.execute(f"SELECT id FROM {table} ORDER BY ID DESC LIMIT 1")
    for row in cur:
        last_id = int(row[0])
        logger.debug(f"Latest ID in db_file: {last_id}.")

    # Retrieve path for saved pager messages from config
    msgs_path = config_values['msgs_path']

    # Loop to check for new entries
    while True:
        cur.execute(f"SELECT id, message, timestamp FROM {table} WHERE ID > ?",(last_id,))

        # Capture all new rows
        rows = cur.fetchall()
        logger.info("Checking for new rows.")

        if rows:
            # Log new entries to individual files
            for row in rows:
                logger.info(f"ID: {row[0]}, Message: {row[1]}, Timestamp: {row[2]}")
                # Grab timestamp of pager message
                timestamp = row[2]

                # Write each pager message to new file
                msgs_path = os.path.join(msgs_path, f'pager_msg-{timestamp}.log')
                with open(msgs_path, "x") as file:
                    file.write(row[1])
                    logger.info("File written ", print(row))
                last_id = row[0]
                logger.debug("Updated last_id: ", last_id)

        # Loop every second
        time.sleep(1)
