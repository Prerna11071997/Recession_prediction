import pandas as pd
import numpy as np

final1 = pd.read_csv("./final_dataset/base.csv")
final2 = pd.read_csv("./final_dataset/final_part0.csv")

print(final1)
print(final2)

final1['DATE'] = pd.to_datetime(final1['DATE'])
final1['DATE'] = pd.to_datetime(final1["DATE"].dt.strftime('%d/%m/%Y'))

final2['DATE'] = pd.to_datetime(final2['DATE'])
final2['DATE'] = pd.to_datetime(final2["DATE"].dt.strftime('%d/%m/%Y'))



res1 = pd.merge( final2.assign(grouper=final2['DATE'].dt.to_period('W')),
    final1.assign(grouper=final1['DATE'].dt.to_period('W')),
                on='grouper', how = "inner")

# res = pd.merge(final2, final1, on = 'DATE')

res1 = res1[['DATE_x','EXCH','STOCK','GOLD','SP500 (Percent change from a year ago)','10Y Rate - 3M TBill',
            '10Y Rate (Percent change from a year ago','3M TBill (Percent Change from a year ago)',
            '6M TBill - FF','1Y Rate - FF','5Y Rate - FF','10Y Rate - FF','Composite Leading Indicator','Recession State']]

res1 = res1.rename(columns= {'DATE_x':'DATE'})

print(res1)

print(res1.head())

print(res1)

res1.to_csv("./final_dataset/final_part3.csv")