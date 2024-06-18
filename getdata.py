import pandas as pd
import yfinance as yf
from datetime import datetime
writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
writer.save()
stockN=["AARTIIND","ABBOTINDIA","ABCAPITAL","ABFRL","ACC","ADANIENT","ADANIPORTS","ALKEM","AMARAJABAT","AMBUJACEM","APLLTD",
"APOLLOHOSP","APOLLOTYRE"]
# "ASHOKLEY","ASIANPAINT","ASTRAL","ATUL","AUBANK","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE",
# "BALKRISIND","BALRAMCHIN","BANDHANBNK","BANKBARODA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD",
# "BPCL","BRITANNIA","BSOFT","ZYDUSLIFE","CANBK","CHAMBLFERT","CHOLAFIN","CIPLA","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL",
# "CROMPTON","CUB","CUMMINSIND","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP","DIVISLAB","DIXON","DLF","DRREDDY","EICHERMOT","ESCORTS",
# "EXIDEIND","FEDERALBNK","FSL","GAIL","GLENMARK","GMRINFRA","GNFC","GODREJCP","GODREJPROP","GRANULES","GRASIM","GSPL","GUJGASLTD","HAL",
# "HAVELLS","HCLTECH","HDFC","HDFCAMC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDCOPPER","HINDPETRO","HINDUNILVR","HONAUT",
# "IBULHSGFIN","ICICIBANK","ICICIGI","ICICIPRULI","IDEA","IDFC","IDFCFIRSTB","IEX","IGL","INDHOTEL","INDIACEM","INDIAMART","INDIGO",
# "INDUSINDBK","INDUSTOWER","INFY","IOC","IPCALAB","IRCTC","ITC","JINDALSTEL","JKCEMENT","JSWSTEEL","JUBLFOOD","KOTAKBANK","L&TFH",
# "LALPATHLAB","LAURUSLABS","LICHSGFIN","LT","LTI","LTTS","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MCX",
# "METROPOLIS","MFSL","MGL","MINDTREE","MOTHERSUMI","MPHASIS","MRF","MUTHOOTFIN","NAM-INDIA","NATIONALUM","NAUKRI","NAVINFLUOR",
# "NBCC","NESTLEIND","NMDC","NTPC","OBEROIRLTY","OFSS","ONGC","PAGEIND","PEL","PERSISTENT","PETRONET","PFC","PFIZER","PIDILITIND",
# "PIIND","PNB","POLYCAB","POWERGRID","PVR","RAIN","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBICARD","SBILIFE","SBIN",
# "SHREECEM","SIEMENS","SRF","SRTRANSFIN","STAR","SUNPHARMA","SUNTV","SYNGENE","TATACHEM","TATACOMM","TATACONSUM","TATAMOTORS",
# "TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","UBL","ULTRACEMCO","UPL","VEDL",
# "VOLTAS","WHIRLPOOL","WIPRO","ZEEL","ABB","INTELLECT"


# writer = pd.ExcelWriter('demo.xlsx', engine='xlsxwriter')
# for i in stockN:
#     data = yf.download(tickers=i+'.NS',start=datetime(2022, 4, 29, 14, 25, 0),end=datetime(2022, 4, 29, 14, 26, 0),interval='1m')
#     data.drop(['High','Low','Adj Close','Close','Volume'],axis=1, inplace=True)
#     for j in range(1,len(stockN)+1):
#         data.to_excel(writer, sheet_name="Prices", index=False, startcol=j)

# writer.save()

time1=list()
for i in stockN:
    data = yf.download(tickers=i+'.NS',start=datetime(2022, 4, 29, 14, 25, 0),end=datetime(2022, 4, 29, 14, 26, 0),interval='1m')
    data.drop(['High','Low','Adj Close','Close','Volume'],axis=1, inplace=True)
    time1.append(data)
print(time1)

time2=list()
for i in stockN:
    data = yf.download(tickers=i+'.NS',start=datetime(2022, 4, 29, 15, 9, 0),end=datetime(2022, 4, 29, 15, 10, 0),interval='1m')
    data.drop(['High','Low','Adj Close','Close','Volume'],axis=1, inplace=True)
    time2.append(data)
print(time2)

# print(time2)
# print(time2[[1]])
# time3=list()
# for i in range(0,len(time1)):
#     temp=time1[i]-time2[i]
#     time3.append(temp)
# print(time3)
# print(time2[2][1])
# print(type(time2))

# sum=(time1[1]+time2[1])
# print(time1[1])
# print("-----------")
# print(time2[1])
# print("-----------")
# print(sum)

# for i in time1:
#     print(i)
# print(type(time1))

