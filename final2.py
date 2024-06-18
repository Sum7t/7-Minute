import yfinance as yf
from datetime import datetime
import pandas as pd

res=list()
stockN=["AARTIIND","ABBOTINDIA","ABCAPITAL","ABFRL","ACC","ADANIENT","ADANIPORTS","ALKEM","AMARAJABAT","AMBUJACEM","APLLTD",
"APOLLOHOSP",
"APOLLOTYRE","ASHOKLEY","ASIANPAINT","ASTRAL","ATUL","AUBANK","AUROPHARMA","AXISBANK","BAJAJ-AUTO","BAJAJFINSV","BAJFINANCE",
"BALKRISIND","BALRAMCHIN","BANDHANBNK","BANKBARODA","BATAINDIA","BEL","BERGEPAINT","BHARATFORG","BHARTIARTL","BHEL","BIOCON","BOSCHLTD",
"BPCL","BRITANNIA","BSOFT","ZYDUSLIFE","CANBK","CHAMBLFERT","CHOLAFIN","CIPLA","COALINDIA","COFORGE","COLPAL","CONCOR","COROMANDEL",
"CROMPTON","CUB","CUMMINSIND","DABUR","DALBHARAT","DEEPAKNTR","DELTACORP","DIVISLAB","DIXON","DLF","DRREDDY","EICHERMOT","ESCORTS",
"EXIDEIND","FEDERALBNK","FSL","GAIL","GLENMARK","GMRINFRA","GNFC","GODREJCP","GODREJPROP","GRANULES","GRASIM","GSPL","GUJGASLTD","HAL",
"HAVELLS","HCLTECH","HDFC","HDFCAMC","HDFCBANK","HDFCLIFE","HEROMOTOCO","HINDALCO","HINDCOPPER","HINDPETRO","HINDUNILVR","HONAUT",
"IBULHSGFIN","ICICIBANK","ICICIGI","ICICIPRULI","IDEA","IDFC","IDFCFIRSTB","IEX","IGL","INDHOTEL","INDIACEM","INDIAMART","INDIGO",
"INDUSINDBK","INDUSTOWER","INFY","IOC","IPCALAB","IRCTC","ITC","JINDALSTEL","JKCEMENT","JSWSTEEL","JUBLFOOD","KOTAKBANK","L&TFH",
"LALPATHLAB","LAURUSLABS","LICHSGFIN","LT","LTI","LTTS","LUPIN","M&M","M&MFIN","MANAPPURAM","MARICO","MARUTI","MCDOWELL-N","MCX",
"METROPOLIS","MFSL","MGL","MINDTREE","MOTHERSUMI","MPHASIS","MRF","MUTHOOTFIN","NAM-INDIA","NATIONALUM","NAUKRI","NAVINFLUOR",
"NBCC","NESTLEIND","NMDC","NTPC","OBEROIRLTY","OFSS","ONGC","PAGEIND","PEL","PERSISTENT","PETRONET","PFC","PFIZER","PIDILITIND",
"PIIND","PNB","POLYCAB","POWERGRID","PVR","RAIN","RAMCOCEM","RBLBANK","RECLTD","RELIANCE","SAIL","SBICARD","SBILIFE","SBIN",
"SHREECEM","SIEMENS","SRF","SRTRANSFIN","STAR","SUNPHARMA","SUNTV","SYNGENE","TATACHEM","TATACOMM","TATACONSUM","TATAMOTORS",
"TATAPOWER","TATASTEEL","TCS","TECHM","TITAN","TORNTPHARM","TORNTPOWER","TRENT","TVSMOTOR","UBL","ULTRACEMCO","UPL","VEDL",
"VOLTAS","WHIRLPOOL","WIPRO","ZEEL","ABB","INTELLECT"]
names=stockN
for i in stockN:
  sum=0.0
  df = pd.read_excel (r'demo.xlsx',i) #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
  # print (df)
  # print("--------------------------")
  # total=df['Open'].sum
  # res.append(total)

  # for col in df.columns:
  #   print(col)

  # cols=['Open']
  # df['sum_stats'] = df[cols].sum(axis=1)
  total=df["Open"].std()
  total=round(total,4)
  res.append(total)
  # print(total/48)



for j in range(len(res)):
  for k in range(len(res)-1):
    if(res[k]>res[k+1]):
      res[k], res[k + 1] = res[k+ 1], res[k]
      names[k],names[k+1] = names[k+1], names[k]

print("Worst 5 companies: ")
for j in range(0,5):
  print(names[j])
print("\n")
names1=list()
print("Top 5 companies: ")
for j in range(len(names)-1,len(names)-6,-1):
  print(names[j])
  names1.append(names[j])



# def top(list1):
#   best=list()
#   worst=list()
#   for i in list1:
#     data1=yf.download(tickers=i+'.NS',start=datetime(2022, 5, 24, 14, 25, 0),end=datetime(2022, 5, 24, 14, 26, 0),interval='1m')
#     data1.drop(['High','Low','Adj Close','Close','Volume'],axis=1, inplace=True)
#     data2 = yf.download(tickers=i+'.NS',start=datetime(2022, 5, 24, 15, 9, 0),end=datetime(2022, 5, 24, 15, 10, 0),interval='1m')
#     data2.drop(['High','Low','Adj Close','Close','Volume'],axis=1, inplace=True)
#     temp=data2-data1
#     if(temp>0):
#       best.append(i)
#     else:
#       worst.append(i)
#   print(best)
#   print(worst)  
# top(names1)