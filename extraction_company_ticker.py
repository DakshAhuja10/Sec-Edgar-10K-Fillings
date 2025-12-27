# secapi-c50c6e84ff443d04ae4eae565e9bcf6804544b22d5128a4e481b1430243661f3

#https://www.youtube.com/watch?v=SU1L6f0N6iw
import pandas as pd
import requests

headers={'User-Agent':"xyz@gmail.com"}

company_tickers=requests.get(
    "https://www.sec.gov/files/company_tickers.json",
    headers=headers
)


# print(company_tickers.json().keys())
data=company_tickers.json()
df=pd.DataFrame.from_dict(data,orient="index")
df.rename(
    columns={
        "cik_str": "cik",
        "ticker": "ticker",
        "title": "company_name"
    },
    inplace=True
)


# Ensuring correct CIK formatting (zero-padded to 10 digits) as api needs 10digit cik 

df["cik"] = df["cik"].astype(str).str.zfill(10)

df.to_csv("16.SecEdgar/company_ticker_cik_mapping.csv", index=False)

print("Saved company_ticker_cik_mapping.csv")