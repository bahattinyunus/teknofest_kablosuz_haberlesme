# 📐 Wireless Communication Mathematical Models

This document provides the theoretical foundation for the wireless communication systems implemented in this repository.

## 1. Friis Transmission Equation
The Friis transmission equation is used to calculate the power received by one antenna under ideal conditions, given another antenna some distance away transmitting a known amount of power.

$$P_r = P_t + G_t + G_r + 20\log_{10}\left(\frac{\lambda}{4\pi d}\right)$$

Where:
*   $P_r$: Received power (dBm)
*   $P_t$: Transmitted power (dBm)
*   $G_t$: Transmitting antenna gain (dBi)
*   $G_r$: Receiving antenna gain (dBi)
*   $\lambda$: Wavelength (m)
*   $d$: Distance (m)

## 2. Shannon-Hartley Theorem
The Shannon–Hartley theorem tells us the maximum rate at which information can be transmitted over a communications channel of a specified bandwidth in the presence of noise.

$$C = B \log_2(1 + SNR)$$

Where:
*   $C$: Channel capacity (bits per second)
*   $B$: Bandwidth (Hz)
*   $SNR$: Signal-to-Noise Ratio (linear)

### LoRa & SNR
In LoRa systems, communication is possible even when $SNR < 0$ (under the noise floor) thanks to Chirp Spread Spectrum (CSS) and the Spreading Factor (SF).

## 3. Link Budget Analysis
A link budget is a summary of all power gains and losses from a transmitter to a receiver.

$$Link\ Budget = P_{out} - L_c + G_t - L_p - L_s + G_r - L_f$$

*   $L_c$: Connector losses (dB)
*   $L_p$: Path loss (dB)
*   $L_s$: Miscellaneous losses (fading, body loss) (dB)
*   $L_f$: Feed line losses (dB)

---
*Prepared by Bahattin Yunus Çetin*
