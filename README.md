# Insurance ETL Pipeline

## Project Overview
This project simulates a real-world insurance ETL (Extract, Transform, Load) pipeline.

Raw insurance claims data arrives daily as messy CSV files from multiple systems.
The goal of this pipeline is to clean, validate, and convert that raw data into
trusted, analytics-ready datasets.

This project reflects the responsibilities of a junior data engineer.

---

## Tech Stack
- Python 3
- pandas
- CSV files (raw input)
- Parquet files (clean output)
- Logging for monitoring and error handling

---

## Project Structure
insurance_etl/
│
├── data/
│ ├── raw/
│ │ └── claims/ # Raw CSV input files
│ └── clean/
│ └── claims/ # Cleaned output files
│
├── src/
│ ├── extract.py # Reads raw CSV files
│ ├── transform.py # Cleans and validates data
│ └── load.py # Saves cleaned data
│
└── README.md


---

## ETL Pipeline Steps

### Extract
- Reads all CSV files from the raw claims folder
- Handles missing or unreadable files gracefully
- Combines multiple files into one dataset

### Transform
- Removes duplicate claim records
- Converts columns to correct data types
- Handles missing values
- Applies basic data quality checks

### Load
- Saves cleaned data as CSV and Parquet
- Pipeline is idempotent (safe to run multiple times)

---

## How to Run the Pipeline

1. Open a terminal
2. Navigate to the `src` folder
3. Run:

```bash
python load.py
