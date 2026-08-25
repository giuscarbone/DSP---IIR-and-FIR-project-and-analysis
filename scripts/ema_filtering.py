import pandas as pd
import matplotlib.pyplot as plt

data = "data.csv" #defining the csv file which contains data
time_column = "time"
signal_column = "x"

alpha = 0.445 #defining EMA filter parameter

#using pandas ema filter function

df = pd.read_csv(data) #opening the csv file

#creates a new column called EMA signal which contains the filtered signal
df["ema_signal"] = df[signal_column].ewm(alpha = alpha, adjust = False).mean()

#ewm is in pandas environment, so i don't need to use .values method

df.to_csv(data, index = False)

#plotting the filtered signal

plt.figure(figsize=(10,5))
plt.plot(df[time_column], df[signal_column], label = "x(t)", alpha = 0.5)
plt.plot(df[time_column], df["ema_signal"], label = f"xe(t), a = {alpha}", linewidth = 2)
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("EMA applied")
plt.legend()
plt.grid(True)
plt.show()