import pandas as pd
import matplotlib.pyplot as plt


def build_pie():
    data = pd.read_csv('Data/stocks_returns.csv', names=["date", "price"])
    data['date'] = data.date
    data['plus'] = data["price"] > 0

    data = data.groupby('plus').apply(lambda x: x.count())

    plt.pie(data['price'], labels=["количество потерь портфеля", "количество приростов портфеля"],
            colors=['#FF6770', "#0D82FF"])
    plt.title("Соотношение количества приростов и потерь портфеля")
    plt.legend()
    plt.show()


def build_boxplot():
    data = pd.read_csv('Data/stocks_returns.csv', names=["date", "price"])
    plt.boxplot(data['price'])
    plt.grid()
    plt.show()


def build_portfolio_chart():
    data = pd.read_csv('Data/stocks_returns.csv', names=["date", "price"])
    data['date'] = data.date

    li = [100]
    for index, value in enumerate(data['price']):
        new_value = li[index - 1] - value
        li.append(new_value)

    new_data = pd.DataFrame()
    new_data['date'] = data['date']
    new_data['briefcase'] = li[1:]

    new_data.plot(x='date', y='briefcase').grid()
    plt.show()
