import pandas as pd
df = pd.read_csv('data/external/wb-acwise-elector-2026.csv')
df.columns = [c.strip().lower().replace(' ','_').replace('.','').replace('(','').replace(')','') for c in df.columns]
print('Cleaned columns:', df.columns.tolist())
df.to_csv('data/external/wb-acwise-elector-2026-clean.csv', index=False)
