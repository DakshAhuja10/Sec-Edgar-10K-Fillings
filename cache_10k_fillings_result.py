from sec_api import ExtractorApi
import pandas as pd
from pathlib import Path

from extraction_10k_fillings import get_url_for_10k
from sections_map import ITEMS_MAP

extractor=ExtractorApi(api_key="c50c6e84ff443d04ae4eae565e9bcf6804544b22d5128a4e481b1430243661f3")

cache_path=Path("16.SecEdgar/10k_sections_cache.parquet")
cache_path.parent.mkdir(parents=True, exist_ok=True)



def get_section_of_10k_on_demand(ticker:str,year:int,item_code:str):
        
        if cache_path.exists():
            cache_df=pd.read_parquet(cache_path)
        else :
            cache_df=pd.DataFrame(
                columns=['ticker','year','item_code','item_name','text']
            )
            
            
        cache_hit = cache_df[
        (cache_df["ticker"] == ticker) &
        (cache_df["year"] == year) &
        (cache_df["item_code"] == item_code)
        ]

        
        if not cache_hit.empty:
            print("cache results")
            return cache_hit.iloc[0]['text']
        
        #cache miss
        urls=get_url_for_10k(ticker,year)
        
        if urls==0 :
            raise ValueError("No 10-K Fillings found")

        filing_url = urls[0]

        text = extractor.get_section(filing_url,item_code,"text")

        # ---- Save to cache ----
        new_row = {
            "ticker": ticker,
            "year": year,
            "item_code": item_code,
            "item_name": ITEMS_MAP[item_code],
            "text": text
        }

        cache_df = pd.concat([cache_df, pd.DataFrame([new_row])], ignore_index=True)
        
        cache_df.to_parquet(cache_path, index=False)
        return text

print(len(get_section_of_10k_on_demand("JPM",2024,"8")))