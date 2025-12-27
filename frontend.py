



import pandas as pd

df = pd.read_parquet("16.SecEdgar/10k_sections_cache.parquet")

# print(df.columns)
# print(len(df))
# print(df.iloc[0]["item_code"])
# print(len(df.iloc[0]["text"]))
# print(df.iloc[0]['text'][:150])
print(df[df['item_code']=='8']['text'])
