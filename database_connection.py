# create_env_file.py

import os

# Set up your PostgreSQL connection parameters
db_name = 'big_data'
user = 'postgres'
password = '1234'
host = 'localhost'
port = '5432'  # Default PostgreSQL port
table_name = 'raw_flight_data'

# Create or update .env file
with open('.env', 'w') as env_file:
    env_file.write(f"DB_NAME={db_name}\n")
    env_file.write(f"DB_USER={user}\n")
    env_file.write(f"DB_PASSWORD={password}\n")
    env_file.write(f"DB_HOST={host}\n")
    env_file.write(f"DB_PORT={port}\n")
    env_file.write(f"TABLE_NAME={table_name}\n")

print(".env file created successfully.")
