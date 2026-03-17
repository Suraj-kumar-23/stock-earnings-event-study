# 📊 Earnings Event Study: Stock Price Reaction Analysis

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![Visualization](https://img.shields.io/badge/Visualization-Matplotlib%20%7C%20Seaborn-green)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## 📌 Project Overview

This project analyzes how a company's stock price reacts to **quarterly earnings announcements**. Financial markets often respond strongly to earnings releases because they provide critical information about a company's financial performance.

Using historical stock price data and earnings announcement dates, this project performs an **event study analysis** to measure stock price changes before and after earnings announcements.

The objective is to determine whether earnings announcements systematically influence stock price movements.

---

# 🎯 Objectives

The main objectives of this project are:

* Collect historical stock price data using an API
* Collect quarterly earnings announcement data
* Analyze stock price movements around earnings dates
* Measure stock price reactions within a defined event window
* Visualize the distribution of market reactions

---

# 🗂 Project Structure

```
earnings-event-study/
│
├── notebooks/
│   └── earnings_event_analysis.ipynb
│
├── src/
│   └── fetch_data.py
│
├── images/
│   └── earnings_distribution.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

### Folder Description

| Folder           | Description                                            |
| ---------------- | ------------------------------------------------------ |
| notebooks        | Jupyter notebook containing analysis and visualization |
| src              | Python scripts for fetching data from APIs             |
| images           | Saved charts used in analysis                          |
| README.md        | Project documentation                                  |
| requirements.txt | Python dependencies                                    |

---

# 📊 Data Sources

The project uses the **Financial Modeling Prep API** to retrieve financial data.

### APIs Used

1. **Historical Stock Price API**

Used to collect daily stock price data.

```
https://financialmodelingprep.com/stable/historical-price-eod/full
```

2. **Earnings Calendar API**

Used to collect earnings announcement dates.

```
https://financialmodelingprep.com/stable/earnings-calendar
```

### Stock Analyzed

```
Apple Inc. (AAPL)
```

---

# ⚙️ Methodology

The analysis follows these steps:

## 1️⃣ Data Collection

Stock price data and earnings announcement dates are retrieved using API requests.

The data is converted into pandas DataFrames for further analysis.

---

## 2️⃣ Data Cleaning

The following preprocessing steps are performed:

* Convert date columns to datetime format
* Handle missing values
* Sort stock prices chronologically

---

## 3️⃣ Feature Engineering

Additional features are created to support analysis.

### Daily Return

Daily return measures the percentage change in stock price between consecutive trading days.

```
daily_return = close_price.pct_change()
```

### Volatility

Rolling volatility is calculated using the standard deviation of daily returns.

```
volatility = rolling_std(daily_return)
```

### Earnings Surprise

Earnings surprise measures the difference between actual earnings and analyst expectations.

```
earnings_surprise = epsActual − epsEstimated
```

---

## 4️⃣ Event Window Analysis

An **event window** is defined to measure stock price reaction around earnings announcements.

Event Window:

```
-5 days before earnings
+5 days after earnings
```

For each earnings date:

1. Extract stock prices within the event window
2. Calculate price before earnings
3. Calculate price after earnings
4. Measure percentage change

```
price_change = (price_after − price_before) / price_before
```

This allows us to quantify how the market reacts to earnings releases.

---

# 📈 Visualization

Several visualizations are created to interpret the results.

### Distribution of Stock Price Reaction

The histogram below shows how stock prices typically react after earnings announcements.

Most reactions are concentrated around small price changes, while some earnings announcements cause larger market movements.

*(Example Visualization)*

![Distribution](images/earnings_distribution.png)

---
### Sample Event Study Results

| Earnings Date | Price Before | Price After | Price Change |
|---------------|-------------|-------------|--------------|
| 2023-05-04 | 169.59 | 171.77 | 0.0128 |
| 2023-08-03 | 196.45 | 179.80 | -0.0847 |
| 2023-11-02 | 170.29 | 181.82 | 0.0677 |

# 📊 Key Insights

From the analysis we observe:

* Earnings announcements often lead to noticeable stock price movements.
* Most earnings reactions fall within a moderate range of price changes.
* Some quarters trigger larger positive or negative reactions, indicating strong market sentiment.

This demonstrates the importance of earnings announcements as major **market-moving events**.

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Requests
* Jupyter Notebook

---

# 🚀 How to Run This Project

### 1️⃣ Clone the Repository

```
git clone https://github.com/yourusername/earnings-event-study.git
```

### 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the Notebook

Open:

```
notebooks/earnings_event_analysis.ipynb
```

Run the cells to reproduce the analysis.

---

# 🔑 API Key Setup

This project requires an API key from **Financial Modeling Prep**.

Replace the placeholder in:

```
src/fetch_data.py
```

```
API_KEY = "YOUR_API_KEY"
```

You can obtain a free API key here:

[https://financialmodelingprep.com/](https://financialmodelingprep.com/)

---

# 📚 Future Improvements

Possible extensions to this project include:

* Calculating **Cumulative Abnormal Returns (CAR)**
* Comparing results with a **market index (S&P 500)**
* Expanding analysis to multiple companies
* Applying statistical significance tests

---

# 👨‍💻 Author

**Suraj Kumar**

Practitioner Data Analyst | Python | SQL | Data Analytics
