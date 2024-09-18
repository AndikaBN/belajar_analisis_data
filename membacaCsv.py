import pandas as pd

# print(pd.read_csv('us-counties-2020.csv', delimiter=","))

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
df = pd.read_html(url)[0]

print(df)