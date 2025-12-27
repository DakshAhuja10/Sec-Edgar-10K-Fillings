from sec_api import QueryApi

queryApi = QueryApi(
    api_key="c50c6e84ff443d04ae4eae565e9bcf6804544b22d5128a4e481b1430243661f3"
)

#create url for 10-k fillings a particular ticker
def get_url_for_10k(ticker,year):
    i=0
    url_lists=[]
    p=2025-year
    query = {
        "query": {
            "query_string": {
                "query": (
                    f'formType:"10-K" '
                    f'AND ticker:{ticker} '
                    f'AND filedAt:[{year}-01-01 TO {year}-12-31]'
                )
            }
        },
        "sort": [{ "filedAt": { "order": "desc" } }],#if there are multiple results,return the most recent ones
        "size": 1
    }

    response = queryApi.get_filings(query)

    #if no 10k for that year
    if response['filings']==[]:
        return 0

    url_lists.append(response['filings'][0]["linkToFilingDetails"])
    
    return url_lists


# print(get_url_for_10k("NVDA",2023))



# import pandas as pd
# import requests

# headers = {
#     "User-Agent": "LangChain-SEC-Research/1.0 (xyz@gmail.com)",
#     "Accept-Encoding": "gzip, deflate"
# }

# df = pd.read_csv("16.SecEdgar/company_ticker_cik_mapping.csv")

# def get_submission_data_for_ticker(ticker: str):
#     row = df.loc[df["ticker"] == ticker]

#     if row.empty:
#         raise ValueError(f"Ticker {ticker} not found in CSV")

#     # 🔥 FORCE zero-padding
#     cik = str(row.iloc[0]["cik"]).zfill(10)

#     url = f"https://data.sec.gov/submissions/CIK{cik}.json"

#     response = requests.get(url, headers=headers, timeout=30)

#     print("URL:", url)
#     print("Status:", response.status_code)
#     print("Content-Type:", response.headers.get("Content-Type"))

#     response.raise_for_status()

#     return response.json()


# data = get_submission_data_for_ticker("NVDA")
# print(data.keys())
# print(data['filings']['recent'].keys())


# # recent = data["filings"]["recent"]

# # for i, form in enumerate(recent["form"]):
# #     if form == "10-K":
# #         print(
# #             "Year:", recent["filingDate"][i],
# #             "Accession:", recent["accessionNumber"][i],
# #             "Primary doc:", recent["primaryDocument"][i]
# #         )
