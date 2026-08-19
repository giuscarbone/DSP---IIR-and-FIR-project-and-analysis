import control as ct
import numpy as np
import matplotlib.pyplot as plt

#small script that computes Bode's diagrams for the EMA filter designed
s = ct.TransferFunction.s #Laplace operator

num = 1 + 0.015625*s #defines numerator
den = 1 + 0.054598*s #defines denominator

G = num / den

#computes frequency response
omega = np.logspace(-2, 4, 100000) #frequency range from 1e-2 to 1e4 rad/s

#Note: i'm plotting at frequencies we don't care about in the context of this project
#just to have a complete look on the filter's transfer function

mag, phase, omega = ct.frequency_response(G, omega)

#convert magnitude to dB
mag_dB = 20 * np.log10(mag)

#convert phase to degrees
phase_deg = np.degrees(phase)

plt.figure(figsize=(10,6))

#defining plots

#magnitude plot
plt.subplot(2,1,1)
plt.semilogx(omega, mag_dB) #log scale
plt.ylabel("Magnitude [dB]")
plt.grid(True, which="both")
plt.title("Bode Diagrams")

#phase plot
plt.subplot(2,1,2)
plt.semilogx(omega, phase_deg) #log scale
plt.xlabel("Frequency [rad/s]")
plt.ylabel("Phase [deg]")
plt.grid(True, which="both")

plt.tight_layout() #adjusts the padding
plt.show()