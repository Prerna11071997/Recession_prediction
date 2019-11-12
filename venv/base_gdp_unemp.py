import pandas as pd
import numpy as np
import datetime


base = pd.read_csv("base.csv")


import os

print(os.listdir("./dataset"))
files = ['GOLDPMGBD228NLBM.csv', 'UNRATE.csv', 'DEXUSUK.csv', 'NASDAQCOM.csv', 'A191RL1Q225SBEA.csv']
output = ['GOLD.csv','UnempRate.csv', 'DollarExchange.csv', 'NASDAQ.csv', 'GDP.csv']

#creating a dictionary
di = {'GOLDPMGBD228NLBM': 'GOLD',
      'UNRATE': 'UNRATE',
      'DEXUSUK': 'EXCH',
      'NASDAQCOM': 'STOCK',
      'A191RL1Q225SBEA': 'GDP'}

# renaming into easily understandable Names
p = []
pdi = {}
for i in range(len(output)):
    p.append(pd.read_csv("./dataset/" + files[i]))

#rename DATE
for i in range(len(p)):
    p[i].rename(columns={"DATE": "Date"})


for i in range(len(p)):
    p[i]['DATE'] = pd.to_datetime(p[i]['DATE'])
    p[i]['DATE'] = p[i]['DATE'].dt.strftime('%d-%m-%Y')

for i in range(len(p)):
    p[i] = p[i].set_index('DATE')

for i in range(len(p)):
    p[i]=p[i].rename(columns=di)
    p[i]=p[i].replace(".",np.nan).astype('float')

# for i in range(len(p)):
#     p[i] = p[i].rename(columns=di);p[i] = p[i].replace(".", np.nan).astype('float');


for i in range(len(p)):
    p[i] = p[i].interpolate();p[i] = p[i].fillna(method='bfill');

j = 0

for i in range (len(output)):
    p[i].to_csv("./modified_dataset/"+output[i])


