from bs4 import BeautifulSoup

import os

import pandas as pd
INPUT_PATH = os.path.join(os.getcwd(), 'INPUT1')

df_final = pd.DataFrame(columns=['State', 'Centre', 'Commodity', 'Variety', 'Unit', 'Category', 'Date', 'Retail Price'])
# State	Centre	Variety	Unit	Commodity	Date	Retail Price

STATE_LIST = [
    'Andhra Pradesh',
    'Arunachal Pradesh',
    'Assam',
    'Bihar',
    'Goa',
    'Gujarat',
    'Haryana',
    'Himachal Pradesh',
    'Jammu Kashmir',
    'Jharkhand',
    'Karnataka',
    'Kerala',
    'Madhya Pradesh',
    'Maharashtra',
    'Manipur',
    'Meghalaya',
    'Mizoram',
    'Nagaland',
    'National Capital',
    'Orissa',
    'Punjab',
    'Rajasthan',
    'Sikkim',
    'Tamil Nadu',
    'Telangana',
    'Tripura',
    'Union Territories',
    'Uttar Pradesh',
    'Uttarakhand',
    'West Bengal'
]


def transform_table(table, category):
    header = table.iloc[0]
    table = table[1:]
    table.columns = header
    commodity_list = list(table[(~table.State.isin(STATE_LIST))]['State'])
    commodity_list_index = list(table[(~table.State.isin(STATE_LIST))].index)
    commodity_list_index.append(len(table) + 1)
    table['Commodity'] = ''
    table['Category'] = category
    for i, item in zip(range(len(commodity_list_index) - 1), commodity_list):
        start = commodity_list_index[i]
        end = commodity_list_index[i + 1] - 1
        table.iloc[start:end]['Commodity'] = item
        # print(start, end, item)
        # print(commodity_list_index[i])
    # Remove the rows with commodity names
    table = table[(table.State.isin(STATE_LIST))]
    table = table.melt(id_vars=['State', 'Centre',	'Variety', 'Category', 'Unit', 'Commodity'],
            var_name="Date",
            value_name="Retail Price")
    return table


for file in os.listdir(INPUT_PATH):
    table = pd.read_html(os.path.join(INPUT_PATH, file))[0]
    print(table)
    # if 'Non_Food' in file:
    #     transformed_table = transform_table(table, category='Non Food')
    # else:
    #     transformed_table = transform_table(table, category='Food')
    # commodity_list = list(transformed_table[(~transformed_table.State.isin(STATE_LIST))]['State'])
    # commodity_list_index = transformed_table[(~transformed_table.State.isin(STATE_LIST))].index
    # print(transformed_table)
    # transformed_table.to_csv("test.csv", index=False)
    print(file)
    # df_final = pd.concat([df_final, transformed_table])

    # print(table)


# df_final.to_csv('Final.csv', index=False)
