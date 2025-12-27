from financial_statements_extract2 import * 

def get_label_dictionary(ticker,headers):
    facts=get_facts(ticker,headers)
    us_gaap_data=facts["facts"]["us-gaap"]
    labels_dict={fact:details['label'] for fact,details in us_gaap_data.items()}
    return labels_dict



def rename_statement(statement,label_dictionary):
    #extracts the part after the first underscore and then maps it using the label dictionary
    statement.index=statement.index.map(
        lambda x:label_dictionary.get(x.split("_",1)[-1],x)
    )
    
    return statement


label_dict = get_label_dictionary(ticker, headers)
# print(label_dict)


accn = get_filtered_filings(
    ticker, ten_k=True, just_accession_numbers=False, headers=headers
)
acc_num = accn["accessionNumber"].iloc[2].replace("-", "")
soup = get_statement_soup(
    ticker,
    acc_num,
    "balance_sheet",
    headers=headers,
    statement_keys_map=statement_keys_map,
)
statement = process_one_statement(ticker, acc_num, "balance_sheet")

print(rename_statement(statement, label_dict))