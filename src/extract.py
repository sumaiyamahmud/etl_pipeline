import pandas as pd
import logging
import os
import configparser

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# -------------------------
# Read raw folder from config
# -------------------------
config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), "../config.ini"))
raw_folder = config["PATHS"]["raw_folder"]

def extract(input_folder=raw_folder):
    try:
        # For example, read all CSV files in the folder
        files = [f for f in os.listdir(input_folder) if f.endswith(".csv")]
        if not files:
            logging.warning("No CSV files found in input folder.")
            return pd.DataFrame()  # return empty dataframe

        # Read all CSVs and concatenate
        dfs = []
        for file in files:
            path = os.path.join(input_folder, file)
            df = pd.read_csv(path)
            logging.info(f"Extracted {file} successfully.")
            dfs.append(df)

        combined_df = pd.concat(dfs, ignore_index=True)
        logging.info(f"Combined {len(files)} files successfully.")
        return combined_df

    except Exception as e:
        logging.error(f"Error in extract(): {e}")
        return pd.DataFrame()  # return empty dataframe if error
