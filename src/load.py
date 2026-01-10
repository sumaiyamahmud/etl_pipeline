import os
import pandas as pd
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def load(df, output_folder="../data/processed/claims/"):
    try:
        if df.empty:
            logging.warning("Empty DataFrame. Nothing to save.")
            return

        os.makedirs(output_folder, exist_ok=True)

        csv_path = os.path.join(output_folder, "claims_cleaned.csv")
        parquet_path = os.path.join(output_folder, "claims_cleaned.parquet")

        df.to_csv(csv_path, index=False)
        df.to_parquet(parquet_path, index=False)

        logging.info(f"Saved cleaned CSV to {csv_path}")
        logging.info(f"Saved cleaned Parquet to {parquet_path}")

    except Exception as e:
        logging.error(f"Error in load(): {e}")

# Main block to run ETL
if __name__ == "__main__":
    try:
        from extract import extract
        from transform import transform

        logging.info("Starting ETL process...")

        df_raw = extract()
        logging.info("Extraction step completed.")

        df_clean = transform(df_raw)
        logging.info("Transformation step completed.")

        load(df_clean)
        logging.info("Load step completed. ETL finished successfully.")

    except Exception as e:
        logging.error(f"ETL process failed: {e}")
