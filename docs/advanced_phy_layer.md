# 📡 Advanced PHY Layer Guide

Deep dive into the physical layer technologies that make modern high-performance wireless communication possible.

## 1. OFDM (Orthogonal Frequency Division Multiplexing)
OFDM is used in high-bandwidth systems like Wi-Fi and 5G. It splits a single high-speed data stream into many lower-speed subcarriers.
*   **Key Advantage**: Resilience against multipath fading and inter-symbol interference (ISI).
*   **Cycle Prefix**: Adding a guard interval to ensure signals don't overlap.

## 2. MIMO (Multiple Input, Multiple Output)
Using multiple antennas at both the transmitter and receiver to improve communication performance.
*   **Spatial Multiplexing**: Sending different data streams over different antennas.
*   **Beamforming**: Focusing the signal towards a specific receiver to increase gain and reduce interference.

## 3. CSS (Chirp Spread Spectrum) - The Heart of LoRa
LoRa uses frequency chirps (up-chirps and down-chirps) to represent bits.
*   **Spreading Factor (SF)**: Controls the duration of each chirp. Higher SF = longer range but lower data rate.
*   **Processing Gain**: The ability to recover signals below the noise floor.

## 4. LPI (Low Probability of Intercept)
Techniques to hide the presence of the signal from unauthorized listeners.
*   **Direct Sequence Spread Spectrum (DSSS)**
*   **Frequency Hopping (FHSS)**: Rapidly changing the carrier frequency during transmission.

---
*Technical Guide by Bahattin Yunus Çetin*
