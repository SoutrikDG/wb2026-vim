import pandas as pd

draft = pd.read_csv('data/external/wb-sir-draft-rolls-2026.csv')
final = pd.read_csv('data/external/wb-acwise-elector-2026.csv')

# Normalise AC number to integer for join key
draft = draft.dropna(subset=['AC NO'])
draft['ac_no'] = draft['AC NO'].astype(float).astype(int)
final = final.dropna(subset=['AC No.'])
final['ac_no'] = final['AC No.'].astype(float).astype(int)

# Merge on ac_no
df = draft.merge(final, on='ac_no', suffixes=('_draft','_final'))

# Compute SIR delta
df['sir_net_deletion'] = df['Total electors'] - df['Total']
df['sir_net_deletion_pct'] = (df['sir_net_deletion'] / df['Total electors'] * 100).round(2)
df['sir_male_deletion'] = df['Male electors'] - df['Male']
df['sir_female_deletion'] = df['Female electors'] - df['Female']

# Clean output
out = df[['ac_no','Name of District','AC name','Phase',
          'Total electors','Total',
          'sir_net_deletion','sir_net_deletion_pct',
          'sir_male_deletion','sir_female_deletion']].copy()
out.columns = ['ac_no','district','ac_name','phase',
               'electors_draft','electors_final',
               'sir_net_deletion','sir_deletion_pct',
               'sir_male_deletion','sir_female_deletion']

out.to_parquet('data/processed/sir_ac_delta.parquet', index=False)
out.to_csv('data/processed/sir_ac_delta.csv', index=False)

print('Saved. Shape:', out.shape)
print()
print('Top 10 ACs by deletion rate:')
print(out.nlargest(10,'sir_deletion_pct')[['ac_no','district','ac_name','sir_deletion_pct','sir_net_deletion']].to_string())
print()
print('Total state-wide deletion:', f"{out['sir_net_deletion'].sum():,}")
print('State deletion pct:', round(out['sir_net_deletion'].sum()/out['electors_draft'].sum()*100,2))
