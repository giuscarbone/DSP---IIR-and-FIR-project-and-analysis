import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

fs = 32 #sampling frequency
N = 21 #taps
ft = 3 #cutoff frequency (Hz)
wt = 2 * np.pi * ft #cutoff angular frequency (rad/s)

k = firwin(N, cutoff=ft, fs=fs, pass_zero=True, window='hann')

#calculating frequency response in Z domain
#function freqz computes the filter's transfer function and evaluates it on the
#unitary circle, computing the frequency response
w, h = freqz(k, [1.0], worN=2048, fs=fs)

#w frequency array
#h complex numbers array, each value contains both the phase and module information

#converting frequency axis from Hz to rad/s
w = 2 * np.pi * w

#module in dB
mag_db = 20 * np.log10(np.abs(h))

# phase in degrees: unwrap avoid jumps around 360°
phase_deg = np.unwrap(np.angle(h)) * 180 / np.pi

#creates 2 subplots for bode diagrams
fig, (magnitude, phase) = plt.subplots(2, 1, figsize=(9, 7), sharex=True)

#assigning parameters for the plot
magnitude.plot(w, mag_db)
magnitude.axvline(wt, color='r', linestyle='--', alpha=0.6, label=f'wt = {wt:.2f} rad/s') #wt line
magnitude.axhline(-3, color='gray', linestyle=':', alpha=0.6, label='-3 dB') #-3dB line
magnitude.set_ylabel('Modulo (dB)')
magnitude.set_title(f'Bode Diagram FIR (Hann, N={N})')
magnitude.grid(True, which='both')
magnitude.legend()

phase.plot(w, phase_deg)
phase.axvline(wt, color='r', linestyle='--', alpha=0.6)
phase.set_xlabel('Angular frequency (rad/s)')
phase.set_ylabel('Phase (gradi)')
phase.grid(True, which='both')

plt.tight_layout()
plt.show()