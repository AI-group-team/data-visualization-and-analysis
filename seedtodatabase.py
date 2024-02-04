# import_and_use_data.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Retrieve PostgreSQL connection parameters from environment variables
db_name = os.getenv("DB_NAME")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
table_name = os.getenv("TABLE_NAME")

# Create a connection string for SQLAlchemy
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

# Replace 'your_data.csv' with the actual CSV file path
csv_file_path = 'trial.csv'

# Read CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Write the DataFrame to the PostgreSQL database
df.to_sql(table_name, engine, if_exists='replace', index=False)

print(f'Data from {csv_file_path} successfully saved to {table_name} in the {db_name} database.')
