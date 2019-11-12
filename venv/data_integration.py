#libraries
import csv
import pandas as pd
import datetime

#load the data

#leading indicatora
data1 = pd.read_csv("./data/leading_indicators.csv")
#recession state
data2 = pd.read_csv("./data/recession_state.csv")
#loading up the GDP growth
GDP_growth = pd.read_csv("./data/GDP_growth.csv")
#loading up Dollar Exchange Rate
DollarExchangeR = pd.read_csv("./data/DollarExchangeRate.csv")
#GOld Pricce
GoldPrice = pd.read_csv("./data/GoldPMPrice.csv")
#NASDAQ enteries
NASDAQEnteries = pd.read_csv("./data/NASDAQ_indice.csv")
#UnemploymentRate
Unemployment = pd.read_csv("./data/unemp_rate.csv")

dictionary ={'GOLDPMGBD228NLBM':'GOLD','UNRATE':'UNRATE','DEXUSUK':'EXCH',
    'NASDAQCOM':'STOCK','DTB3':'3M','DGS1':'1Y',
    'A191RL1Q225SBEA':'GDP','CPICPIAUCSL':'CPI','CPIAUCSL':'CPI'}


#get info
def get_info(data):
    print(data.info())
    print()

#getting some enteries
def print_head(data):
    print(data.head())
    print()


#get the size of all the data
def size(data):
    print(data.shape)
    print()


#getting info
data_frames = [GDP_growth, DollarExchangeR, GoldPrice, NASDAQEnteries, Unemployment]
for i in data_frames:
    get_info(i)
    print_head(i)
    size(i)

recession_indicator = pd.merge(data1, data2, on="Date")
recession_indicator = recession_indicator.rename(columns = {"Date": "DATE" })
data_frames.append(recession_indicator)



for i in range(len(data_frames)):
    data_frames[i]= data_frames[i].rename(columns=dictionary)


for i in range(len(data_frames)):
    data_frames[i]['DATE']= pd.to_datetime(data_frames[i]['DATE'])

for i in range(len(data_frames)):
    data_frames[i]['DATE']= data_frames[i]['DATE'].dt.strftime('%d-%m-%Y')

print("#####################################")

print(DollarExchangeR.head())