import pandas as pd
import datetime as dt
import numpy as np

#gdp conversion

GDP = pd.read_csv("./modified_dataset/GDP.csv")
print("GDP :",GDP.shape)
print(GDP)
print("################")

GDP['DATE'] = pd.to_datetime(GDP['DATE'])

print(GDP['DATE'].dtype)
GDP['DATE'] = pd.to_datetime(GDP["DATE"].dt.strftime('%d/%m/%Y'))


res1 = GDP

print(res1)
res1.to_csv("./final_dataset/final_part1.csv")

####################################################################

#part 2 merging with final

res2 = pd.read_csv("./final_dataset/final_part0.csv")

res2['DATE'] = pd.to_datetime(res2['DATE'])
res2['DATE'] = pd.to_datetime(res2["DATE"].dt.strftime('%d/%m/%Y'))

# print(res1)
# print(res2)

res = pd.merge( res1.assign(grouper=res1['DATE'].dt.to_period('M')),
    res2.assign(grouper=res2['DATE'].dt.to_period('M')),
                on='grouper')

print(res.head())
#res = pd.merge(res1, res2, on= 'DATE', how= "inner")
print(res.shape)

res = res[['DATE_x','GDP','EXCH','STOCK','GOLD']]

res = res.rename(columns= {'DATE_x':'DATE'})

print(res)


res.to_csv("./final_dataset/final_part2.csv")

#difference between dates
#
# # GDP['diff'] = 0
# #
# # print(GDP['DATE'].dtype)
# # for i in range(GDP.shape[0] - 1):
# #     GDP['diff'][i+1] = ((GDP['DATE'][i+1]) - (GDP['DATE'][i]))
# #
# # print(GDP.set_index('DATE').diff())
#
# GDP['DATE'] = pd.to_datetime(GDP['DATE'])
# print(GDP.info())
#
# GDP['diff'] = GDP.groupby('ind')['DATE'].apply(lambda x: x.sort_values())
#
# GDP['diff'] = GDP.groupby('ind')['DATE'].diff() / np.timedelta64(1, 'D')
#
# print(GDP)