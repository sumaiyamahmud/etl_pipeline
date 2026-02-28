import pandas as pd
from sqlalchemy import create_engine

# STEP 1: Read Parquet file
file_path = r"C:\Projects\insurance_etl\data\processed\claims\claims_cleaned.parquet"
df = pd.read_parquet(file_path)

# STEP 2: PostgreSQL credentials
username = "postgres"
password = "wizzard"
host = "localhost"
port = "5432"
database = "postgres"

# STEP 3: Create SQLAlchemy engine
connection_string = f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_string)

# STEP 4: Write DataFrame to PostgreSQL table
df.to_sql(
    "claims",        # Table name in PostgreSQL
    engine,
    if_exists="replace",  # Replace table if it exists
    index=False
)

print("✅ ETL output loaded into PostgreSQL successfully!")
