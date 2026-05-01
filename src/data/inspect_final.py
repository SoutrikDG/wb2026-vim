import pandas as pd
df = pd.read_csv('data/external/wb-acwise-elector-2026.csv')
print('Shape:', df.shape)
print('Columns:')
for c in df.columns: print(' ', c)
print()
print(df.head(3).to_string())
