import pandas as pd
import requests

file_path = r"C:\Users\ramanneg\OneDrive - Diageo\Desktop\Practice\DIAGEO_CA-CAN_DDH_STOCK_2026_03_03_AB.csv"

df = pd.read_csv(file_path, sep="|")

print(df.head())