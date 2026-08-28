# =========================================
# STOCK MARKET ANALYSIS 
# =========================================

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# -----------------------------------------
# 1. Load Stock Dataset
# -----------------------------------------

# your csv file path

file_path = r"C:\Users\Armin Khareghat\OneDrive\Desktop\AI ML data science\Python\python-projects\stock market analysis\stock_data.csv"

# load csv file 
try:
     df = pd.read_csv(file_path)
     print("\n File Loaded Successfully!")
     print("stock_data:", os.path.basename(file_path))
     print("Total Rows:", df.shape[0])
     print("Total Columns:", df.shape[1])

     print("\n ----- STOCK DATASET -----")
     print(df.head())

except FileNotFoundError:
    print("\n File Not Found!")
    print("Please check the complete CSV file path.")

except PermissionError:
    print("\n Permission Denied!")
    print("\n please make sure you selected the CSV file, not the folder.")

    

except Exception as e:
    print("\n Error while loading file:",e)


#  Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Set Date as index
df.set_index("Date", inplace=True)
    
# Display first 5 records
print("----- Historical Stock Data -----")
print(df.head())

# -----------------------------------------
# 2. Dataset Information
# -----------------------------------------

print("\n----- Dataset Information -----")
df.info()

print("\n----- Statistical Summary -----")
print(df.describe())

# -----------------------------------------
# 3. Calculate Moving Averages
# -----------------------------------------

df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

print("\n----- Moving Average Data -----")
print(df[["Close", "MA20", "MA50"]].tail())

# -----------------------------------------
# 4. Calculate Daily Returns
# -----------------------------------------

df["Daily Return"] = df["Close"].pct_change() * 100

print("\n----- Daily Returns -----")
print(df["Daily Return"].tail())

# -----------------------------------------
# 5. Calculate Average Return
# -----------------------------------------

average_return = df["Daily Return"].mean()

print("\nAverage Daily Return:", round(average_return, 2), "%")

# -----------------------------------------
# 6. Highest and Lowest Stock Price
# -----------------------------------------

highest_price = df["High"].max()
lowest_price = df["Low"].min()

print("\nHighest Stock Price:", round(highest_price, 2))
print("Lowest Stock Price:", round(lowest_price, 2))

# -----------------------------------------
# 7. Stock Price with Moving Averages
# -----------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(df.index, df["Close"], label="Closing Price")
plt.plot(df.index, df["MA20"], label="20-Day Moving Average")
plt.plot(df.index, df["MA50"], label="50-Day Moving Average")

plt.title("Stock Price and Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid()

plt.show()

# -----------------------------------------
# 8. Trading Volume Analysis
# -----------------------------------------

plt.figure(figsize=(12, 5))

plt.bar(df.index, df["Volume"])

plt.title("Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")

plt.show()

# -----------------------------------------
# 9. Daily Return Distribution
# -----------------------------------------

plt.figure(figsize=(10, 5))

sns.histplot(
    df["Daily Return"].dropna(),
    kde=True
)

plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return (%)")
plt.ylabel("Frequency")

plt.show()

# -----------------------------------------
# 10. Final Message
# -----------------------------------------

print("\n--------------------------------")
print("Stock Market Analysis Completed!")
print("--------------------------------")
