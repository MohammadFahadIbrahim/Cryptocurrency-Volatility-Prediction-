import pandas as pd

def load_and_clean(file_path):
    df = pd.read_csv(file_path)
    df.columns = [c.strip().lower() for c in df.columns]
    df = df.rename(columns={'crypto_name':'symbol','marketcap':'market_cap'})
    if 'unnamed: 0' in df.columns:
        df = df.drop(columns=['unnamed: 0'])
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df = df.dropna(subset=['date'])
    df = df.sort_values(['symbol','date']).reset_index(drop=True)
    df = df.groupby('symbol').apply(lambda g: g.ffill().bfill()).reset_index(drop=True)
    return df
