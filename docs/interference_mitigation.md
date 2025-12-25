# 🤜 Interference Mitigation & Jamming Resilience

TEKNOFEST competition areas are high-noise environments. To maintain a reliable link, you must use "Elite" level mitigation strategies.

---

## 1. Frequency Agile Strategies
*   **FHSS (Frequency Hopping):** Don't stay on one frequency. If 433.1 MHz is jammed, hop to 433.5 MHz.
*   **Clear Channel Assessment (CCA):** Listen before talk. Use your module to check RSSI. If RSSI > -90dBm, the channel is busy.

## 2. LoRa Specific Tuning
*   **Increase Spreading Factor (SF):** Higher SF increases the "Coding Gain," allowing the signal to be decoded even if it's below the noise floor.
    *   *Trade-off:* Higher latency and lower data rate.
*   **Bandwidth (BW):** Narrower bandwidth (125kHz vs 500kHz) increases sensitivity but slows down transmission.

## 3. Physical Protection
*   **Bandpass Filters:** Use physical SAW filters to block out-of-band noise (e.g., 868MHz noise interfering with 433MHz).
*   **Shielding:** Encasing your electronics in a Faraday cage (metal box) and only exposing the antenna prevents local EMI from crashing your MCU.

---

## 4. Coding & Logic
*   **Forward Error Correction (FEC):** Use redundant bits ($\text{Coding Rate} = 4/8$). Even if 50% of the packet is hit by a noise burst, it can be mathematically reconstructed.
*   **CRC Checks:** Always verify packet integrity at the MAC layer.

---
© 2025 Wireless-Architect
