import pandas as pd
import math
import openpyxl

url = 'https://ciffc-node-api.azurewebsites.net/v1/historical/yearly'
history = pd.read_json(url)
#removed the first 3 entries for years : 1980-1982 as they were empty
history = history.iloc[3:]
l=[]
#dict ={}
newlist =[]
for index,row in history.iterrows():
    (l.append(row.tolist()))
#print(l[0])
for i in range(0, len(l)):
    #print(f'{l[i][0]} {len(l[i])}')
    for j in range(1, len(l[i])):
        if(l[i][j]==None):
            continue
        newlist.append([l[i][0],l[i][j]])
#print(newlist)
removed_nan =[]
for i in newlist:
    #check to see if the second element is a dictionary or not
    if(isinstance(i[1],dict)):
        removed_nan.append(i)


historical_data = pd.DataFrame(removed_nan, columns=["year", "agency_info"])
#print(historical_data.head(5))
historical_data[["agency", "avg_fires", "avg_hectares"]] = historical_data["agency_info"].apply(pd.Series)
historical_data = historical_data.drop(columns=["agency_info"])
print(historical_data.head())
historical_data.to_excel(r"C:\Users\prith\OneDrive\Desktop\Canadian_wildfire\history.xlsx", index =False)


