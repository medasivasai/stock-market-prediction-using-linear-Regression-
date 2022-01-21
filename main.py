import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from yahoofinancials import YahooFinancials
import mplfinance
import matplotlib.pyplot as plt
import yahoofinancials

stock = input("enter stock : ")

highs = []
opens = []
closes = []
lows = []

yahoofinancials = YahooFinancials(str(stock))
stats = (yahoofinancials.get_historical_price_data("2000-01-10","2021-10-19","daily"))

i = 0
for date in stats[str(stock)]["prices"] :
    if i == 0 :
        i += 1
        continue
    highs.append(date['high'])
    lows.append(date['low'])
    opens.append(date['open'])
    closes.append(date['close']) 
    i += 1
print("no of data points :",i)

total = []
totalopens = []
for j in range(4):
    opens.append(0)

for i in range(i-1):
    total.append([opens[i],lows[i],highs[i],closes[i]])
#     row = []
#     for p in range(4) :
#         row.append(opens(i-p))
#     totalopens.append(row)

# for totalopen in totalopens :
#     print(totalopens) 

# months = int(input("how many months for validation"))               

def Predictor(lst,months):
    total_training = lst[0:i-months]
    total_validation = lst[i-months:]

    df = pd.DataFrame(total_training, dtype = float)
    XTrain = df.iloc[: , :-1]
    yTrain = df.iloc[: , [-1]]

    clf = LinearRegression()
    clf.fit(XTrain, yTrain)

    print("\n\n")

    dfP = pd.DataFrame(total_validation, dtype = float)
    XValidation = dfP.iloc[: , :-1]
    YValidation = dfP.iloc[: , [-1]]

    print("\n prediction")

    YPrediction = clf.predict(XValidation)

    print("\n original")
    print(YValidation)

    print("\n predictor")
    print(YPrediction)

Predictor(total,1)    

