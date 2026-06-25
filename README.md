<div align="center">

# 📈 Yahoo Stocks

**A PyQt6 desktop app for tracking weighted investment portfolios via Yahoo Finance**

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.x-41CD52?style=flat-square&logo=qt&logoColor=white)](https://pypi.org/project/PyQt6/)
[![yfinance](https://img.shields.io/badge/yfinance-data-8A2BE2?style=flat-square)](https://pypi.org/project/yfinance/)
[![pandas](https://img.shields.io/badge/pandas-analysis-150458?style=flat-square&logo=pandas)](https://pandas.pydata.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE.md)

</div>

---

## How it works

```
┌─────────────────────────────────────────────┐
│              MainWindow                     │
│                                             │
│  Stock names:   AAPL, MSFT, GOOGL           │
│  Weights:       0.5, 0.3, 0.2               │
│  Separator:     ,                           │
│  Buy date:      [📅 2023-01-01]             │
│  Sell date:     [📅 2024-01-01]             │
│                                             │
│  [ Get Data ]       [ History ]             │
└──────────────────┬──────────────────────────┘
                   │
          ┌────────▼────────┐
          │   StocksWindow  │  ← daily % returns table (CSV)
          │                 │
          │ [Build Chart]   │──────► GraphWindow
          │ [Stats Table]   │──────► MoreInfoWindow
          └─────────────────┘
```

### Chart options (GraphWindow)

| Button | Output |
|---|---|
| Portfolio line chart | Cumulative value from a base of 100 over time |
| Profit / Loss pie | Days portfolio gained vs days it lost |
| Box & Whisker | Median, IQR, and outliers of daily returns |

---

## Data output

**`Data/stocks_returns.csv`** — one row per trading day:
```
date,return
2022-11-08, 0.00418
2022-11-09,-0.03319
2022-11-10, 0.08897
...
```

**`Data/more_info.csv`** — pandas `.describe()` of returns:
```
stat,   value
count,  7.0
mean,  -0.01776
std,    0.02012
min,   -0.04240
25%,   -0.03525
50%,   -0.01754
75%,    0.00098
max,    0.00418
```

---

## Installation

```bash
git clone https://github.com/whoIsClownHere/Yahoo-Stocks-QT6-app.git
cd "Yahoo-Stocks-QT6-app/Qt project"

pip install PyQt6 pandas yfinance matplotlib

python MainWindow.py
```

> `sqlite3` ships with Python — no extra install needed.

---

## Project structure

```
Qt project/
├── MainWindow.py        # Entry point — input form
├── CalendarWindow.py    # Date picker dialog
├── BackEnd.py           # yfinance fetch + weighted returns calc
├── BuildGraphs.py       # matplotlib: line, pie, boxplot
├── StockWindow.py       # Returns table + navigation
├── GraphWindow.py       # Chart selector
├── MoreInfoWindow.py    # Descriptive stats table
├── HistoryWindow.py     # Session history (SQLite)
├── WorkWithHistory.py   # SQLite CRUD (History.sqlite)
└── Data/
    ├── stocks_returns.csv
    └── more_info.csv
```

---

## Stack

| | |
|---|---|
| **PyQt6** | Desktop UI — windows, layouts, tables, calendar picker |
| **yfinance** | Historical OHLCV data from Yahoo Finance |
| **pandas** | Weighted return computation, CSV I/O, descriptive stats |
| **matplotlib** | Line chart, pie chart, box plot |
| **sqlite3** | Persistent query history (`History.sqlite`) |

---

<div align="center">
MIT License · Data via <a href="https://finance.yahoo.com">Yahoo Finance</a>
</div>
