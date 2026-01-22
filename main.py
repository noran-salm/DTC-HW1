import pandas as pd

# Read the parquet file
df = pd.read_parquet('green_tripdata_2025-11.parquet')
print(df.head())
print(df.info())