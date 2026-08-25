import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, lfilter_zi

data = "data.csv"
time_column = "time"
signal_column = "x"
df = pd.read_csv(data)
x = df[signal_column].values #taking the values from the column 

#i need values cause i'm gonna use firwin function, which is not part of
#pandas environment

fs = 32 #sampling frequency (Hz)
N = 19 #taps number
ft = 3 #cutoff frequency (Hz)

k = firwin(N, cutoff = ft, fs = fs, pass_zero= True, window = 'hann')

#at this point, i decide to apply the filter sample by sample, in order to visualize
#the delay caused by the filtering operation

zi = lfilter_zi(k, [1.0]) * x[0] #adjusting filter's starting state
y, zf = lfilter(k , [1.0], x, zi = zi)

#defining a new column in the csv file called fit_signal
df["fir_signal"] = y
df.to_csv(data, index = False)

plt.figure(figsize=(10,5))
plt.plot(df[time_column], df[signal_column], label = "x(t)", alpha = 0.5)
plt.plot(df[time_column], df["fir_signal"], label = "fir_x(t)")
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("FIR applied")
plt.grid(True)
plt.legend()
plt.show()