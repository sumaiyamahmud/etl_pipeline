import os
import pandas as pd
import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def transform(df):
    """Clean the DataFrame: remove duplicates, fix types, fill missing"""
    try:
        if df.empty:
            logging.warning("Received empty DataFrame. Nothing to transform.")
            return df

        # Remove duplicates based on claim_id
        df = df.drop_duplicates(subset="claim_id")
        logging.info(f"Removed duplicates. DataFrame shape now: {df.shape}")

        # Convert numeric columns safely
        df.loc[:, "claim_id"] = pd.to_numeric(df["claim_id"], errors="coerce")
        df.loc[:, "member_id"] = pd.to_numeric(df["member_id"], errors="coerce")
        df.loc[:, "claim_amount"] = pd.to_numeric(df["claim_amount"], errors="coerce").fillna(0)
        logging.info("Converted numeric columns safely and filled missing claim_amount with 0.")

        # Fill missing dates
        df.loc[:, "claim_date"] = df["claim_date"].fillna("1900-01-01")
        logging.info("Filled missing claim_date values with '1900-01-01'.")

        # Reset index
        df = df.reset_index(drop=True)
        logging.info(f"Reset index. Final DataFrame shape: {df.shape}")

        return df

    except Exception as e:
        logging.error(f"Error in transform(): {e}")
        return df  # Return as-is if error occurs
