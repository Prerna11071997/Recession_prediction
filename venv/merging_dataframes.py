import pandas as pd

data_dict = [
    "GDP.csv" ,
    "GOLD.csv",
    "DollarExchange.csv",
    "NASDAQ.csv",
    "UnempRate.csv"
]

GDP = pd.read_csv("./modified_dataset/GDP.csv")
print("GDP :",GDP.shape)
print(GDP)

GOLD = pd.read_csv("./modified_dataset/GOLD.csv")
print("GOLD :" , GOLD.shape)
DExch = pd.read_csv("./modified_dataset/DollarExchange.csv")
print("DEXCH :",DExch.shape)
NASDAQ = pd.read_csv("./modified_dataset/NASDAQ.csv")
print("NASDAQ :" , NASDAQ.shape)
UnempRate = pd.read_csv("./modified_dataset/UnempRate.csv")
print("Unem :", UnempRate.shape)

DExch_rate = pd.merge(DExch, NASDAQ, on="DATE")
print("DExchange + NASDAQ", DExch_rate.shape)

#lets add GOLD
DExch_rate_gold = pd.merge(DExch_rate, GOLD, on = "DATE")
print("DExchange + NASADQ + GOLD", DExch_rate_gold.shape)


p = []
pdi = {}
for i in range(len(data_dict)):
    p.append(pd.read_csv("./modified_dataset/" + data_dict[i]))


#     df_merge_col[j] =  pd.merge(p[i-1], p[i], on = 'DATE')

DExch_rate_gold.to_csv("./final_dataset/final_part0.csv")