import pandas as pd
import yfinance as yf


def stocks_returns(assets, weights, from_date, to_date):
    stock_data = pd.Series()
    asset_number = 0
    arr_of_day_price = []

    date_history = 0
    price_history = 0
    for asset in assets:
        history = yf.Ticker(asset).history(start=pd.to_datetime(from_date) - pd.DateOffset(1),
                                           end=pd.to_datetime(to_date) + pd.DateOffset(1))
        date_history = history.index
        price_history = history["Close"]

        for price in range(0, len(price_history)):
            if len(arr_of_day_price) - 1 < price:
                arr_of_day_price.append(price_history[price] * weights[asset_number % len(assets)])
            else:
                arr_of_day_price[price] += price_history[price] * weights[asset_number % len(assets)]
        asset_number += 1

    for day in range(1, len(price_history)):
        if date_history[day].date() in stock_data:
            stock_data[date_history[day].date()] += \
                (arr_of_day_price[day] - arr_of_day_price[day - 1]) / arr_of_day_price[day - 1]
        else:
            stock_data[date_history[day].date()] = \
                (arr_of_day_price[day] - arr_of_day_price[day - 1]) / arr_of_day_price[day - 1]

    stock_data.to_csv("Data/stocks_returns.csv")


def get_more_info(table):
    data = pd.read_csv(table)
    info = data.describe()
    info.to_csv("Data/more_info.csv")
