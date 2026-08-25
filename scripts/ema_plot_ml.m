% small script that computes Bode's diagrams for the EMA filter designed

s = tf('s');

num = 1 + 0.015625*s; % defines numerator
den = 1 + 0.054598*s; % defines denominator

G = num / den;

% computes frequency response
omega = logspace(-2, 4, 100000); % frequency range from 1e-2 to 1e4 rad/s

[mag, phase, omega] = bode(G, omega);

% Remove singleton dimensions
mag = squeeze(mag);
phase = squeeze(phase);

% convert magnitude to dB
mag_dB = 20*log10(mag);

figure('Position',[100 100 1000 600]);

% Magnitude plot
subplot(2,1,1);
semilogx(omega, mag_dB);
ylabel('Magnitude [dB]');
grid on;
title('Bode Diagrams');

% Phase plot
subplot(2,1,2);
semilogx(omega, phase);
xlabel('Frequency [rad/s]');
ylabel('Phase [deg]');
grid on;