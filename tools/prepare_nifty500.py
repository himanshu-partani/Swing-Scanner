import pandas as pd
from pathlib import Path

SOURCE = Path("data/official_nifty500.csv")
OUTPUT = Path("data/nifty500.csv")

df = pd.read_csv(SOURCE)

required_columns = {"Symbol"}
missing = required_columns - set(df.columns)

if missing:
    raise ValueError(f"Missing required column(s): {missing}")

scanner_df = pd.DataFrame({
    "Ticker": df["Symbol"].astype(str).str.strip() + ".NS"
})

scanner_df.to_csv(OUTPUT, index=False)

print(f"✅ Created {OUTPUT}")
print(f"📈 Total stocks: {len(scanner_df)}")