# Insurance ETL Pipeline

## Overview
End-to-end data engineering pipeline that extracts, transforms, and loads 
insurance claims data from raw CSV files into PostgreSQL for analytics.

## Project Flow
Raw CSV Files → Python ETL → Parquet → PostgreSQL

## Tech Stack
- Python 3
- pandas
- SQLAlchemy
- psycopg2
- PostgreSQL
- Git / GitHub

## Prerequisites
Before running this project make sure you have the following installed:
- Python 3.9+
- PostgreSQL
- pgAdmin (to view your database)
- Git

## Installation

### 1. Clone the repo
```
git clone https://github.com/yourusername/insurance_etl.git
cd insurance_etl
```

### 2. Install required Python packages
```
pip install pandas sqlalchemy psycopg2-binary pyarrow
```

### 3. Set up config.ini
Open `config.ini` and update the paths to match your local machine:
```
[PATHS]
raw_folder = C:/Projects/insurance_etl/data/raw/claims
clean_folder = C:/Projects/insurance_etl/data/clean/claims
```

### 4. Add raw CSV files
Place your raw claims CSV files inside:
```
data/raw/claims/
```
Each CSV file should have these columns:
```
claim_id, member_id, claim_amount, claim_date
```

## Project Structure
```
insurance_etl/
├── data/
│   ├── raw/claims/        # Raw CSV input files
│   └── clean/claims/      # Cleaned output files
├── src/
│   ├── extract.py         # Reads and combines raw CSV files
│   ├── transform.py       # Cleans and validates data
│   ├── load.py            # Saves cleaned data as CSV and Parquet
│   └── load_claims_to_postgres.py  # Loads cleaned data into PostgreSQL
├── config.ini             # Folder path configuration
├── .gitignore
└── README.md
```

## Pipeline Steps

### Extract
- Reads all CSV files from raw claims folder
- Combines multiple files into one dataset
- Handles missing or unreadable files gracefully

### Transform
- Removes duplicate claim records
- Converts columns to correct data types
- Handles missing values
- Applies data quality checks

### Load
- Saves cleaned data as CSV and Parquet
- Loads Parquet into PostgreSQL using SQLAlchemy
- Pipeline is idempotent — safe to rerun multiple times

## How to Run

### Step 1 — Run ETL Pipeline
```
cd src
python load.py
```
Output files will appear in `data/clean/claims/`

### Step 2 — Load into PostgreSQL
1. Open `src/load_claims_to_postgres.py`
2. Update your PostgreSQL credentials:
```python
username = "postgres"
password = "your_password"
database = "postgres"
```
3. Run:
```
python load_claims_to_postgres.py
```
4. Verify in pgAdmin:
```
Databases → postgres → Schemas → public → Tables → claims
```

## Logging
All pipeline steps include logging. When you run the pipeline you will see 
timestamped logs like:
```
2025-01-30 10:23:01 - INFO - Extracted claims_2025_01_01.csv successfully
2025-01-30 10:23:01 - INFO - Load step completed. ETL finished successfully
```
```

---

Save (`Ctrl + S`) then push:
```
git add .
git commit -m "Updated README - full replication instructions added"
git push