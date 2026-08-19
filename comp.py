import pandas as pd
import matplotlib.pyplot as plt

#small script that generates the graph which compares the 3 signals acquired:
#1) raw signal
#2) ema filtered signal
#3) firwin filtered signal

time_column = "time"
raw_column = "x"
ema_column = "ema_signal"
fir_column = "fir_signal"

df = pd.read_csv("data.csv")

plt.figure(figsize=(10,5))
plt.plot(df[time_column], df[raw_column], label = "x[t]", alpha = 0.5)
plt.plot(df[time_column], df[ema_column], label = "emax[t]")
plt.plot(df[time_column], df[fir_column], label = "firx[t]")
plt.xlabel("time (s)")
plt.ylabel("Value")
plt.title("Signal comparison")
plt.legend()
plt.grid(True)
plt.show()