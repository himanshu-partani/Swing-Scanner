import pandas as pd

stocks = pd.read_csv("data/stocks.csv")

min_price = int(input("Enter minimum price: "))
min_score = int(input("Enter minimum score: "))

buy = stocks[
    (stocks["Price"] > min_price) &
    (stocks["Score"] > min_score)
]

print(buy)