import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fft import rfft, rfftfreq
from scipy.signal import detrend, get_window

#program that computes FFT on data acquired 
#computes SNR and MSE

#defining a function that computes SNR: in this case
def compute_snr(freq, amplitude, cutoff):
    #snr is defined as a ratio of powers
    #power is defined as the square of amplitude

    power = amplitude ** 2

    #signal_mask and noise_mask are boolean array 
    #they are used in order to sum correctly the components

    signal_mask = freq <= cutoff 
    noise_mask = freq > cutoff

    signal_power = np.sum(power[signal_mask]) #sum of every signal component
    noise_power = np.sum(power[noise_mask]) #sum of every noise component

    snr_linear = signal_power / noise_power
    snr_db = 10 * np.log10(snr_linear) #multiplying by 10 cause we're working with power

    return snr_db

data = "data.csv"

df = pd.read_csv(data) #reading csv
time = df["time"].values
raw_x = df["x"].values #raw signal
ema_x = df["ema_signal"].values #ema filtered signal
fir_x = df["fir_signal"].values #fir filtered signal

fs = 32 #defining sampling frequency
ft = 3 #cutoff frequency

#removing mean value to avoid spikes on f = 0Hz

raw_x = raw_x - np.mean(raw_x)
ema_x = ema_x - np.mean(ema_x)
fir_x = fir_x - np.mean(fir_x)

#removing trends

raw_x = detrend(raw_x)
ema_x = detrend(ema_x)
fir_x = detrend(fir_x)

#computing fft on real data (real signal)

#raw signal:

nr = len(raw_x)

#applying hann window in order to reduce spectral leakage

win = get_window('hann', nr)

raw_wx = raw_x * win
ema_wx = ema_x * win
fir_wx = fir_x * win


raw_y = rfft(raw_wx)
raw_f = rfftfreq(nr, d = 1/fs)

raw_amp = np.abs(raw_y) / (np.sum(win) / 2) #normalizing amplitude not considering negative frequency
raw_amp[0] = raw_amp[0] / 2 #used in order not to double DC component (mean value)

#ema signal:

ne = len(ema_wx)
ema_y = rfft(ema_wx)
ema_f = rfftfreq(ne, d = 1/fs)

ema_amp = np.abs(ema_y) / (np.sum(win) / 2) #normalizing amplitude not considering negative frequency
ema_amp[0] = ema_amp[0] / 2 #used in order not to double DC component (mean value)

#fir signal

nf = len(fir_wx)
fir_y = rfft(fir_wx)
fir_f = rfftfreq(nf, d = 1/fs)

fir_amp = np.abs(fir_y) / (np.sum(win) / 2) #normalizing amplitude not considering negative frequency
fir_amp[0] = fir_amp[0] / 2 #used in order not to double DC component (mean value)

#plotting:

plt.plot(raw_f, raw_amp, label = "raw")
plt.plot(ema_f, ema_amp, label = "ema")
plt.plot(fir_f, fir_amp, label = "fir")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show()

#computing MSE in respect to both the filtered signals

#mse is defined as mean squared error

mse_ema = np.mean((raw_x-ema_x) ** 2)
mse_fir = np.mean((raw_x - fir_x) ** 2)

print("EMA MSE: ", mse_ema)
print("\nFIR MSE: ", mse_fir)

raw_snr = compute_snr(raw_f, raw_amp, ft)
ema_snr = compute_snr(ema_f, ema_amp, ft)
fir_snr = compute_snr(fir_f, fir_amp, ft)

print("RAW SNR: ", raw_snr)
print("EMA SNR: ", ema_snr)
print("FIR SNR: ", fir_snr)