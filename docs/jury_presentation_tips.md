# 🏆 Jury Presentation & Finals Strategy

Winning TEKNOFEST is not just about the code; it's about proving and presenting your system's robustness to the technical jury.

## 1. Top 5 Jury Questions (Be Ready!)
1.  **"How does your system handle high-power jamming?"**
    *   *Answer*: Mention FHSS (Frequency Hopping) and our AI-based modulation adaptation.
2.  **"Why did you choose this protocol over MAVLink/standard LoRa?"**
    *   *Answer*: Focus on overhead reduction and the "System Architect" philosophy of complete control.
3.  **"What is your actual field test RSSI vs theoretical prediction?"**
    *   *Answer*: Use your Link Budget calculations to show you've accounted for Fresnel zone and fading.
4.  **"How secure is your link against replay attacks?"**
    *   *Answer*: Point to the Sequence Numbers and Nonces in our protocol spec.
5.  **"How do you ensure low latency during swarm coordination?"**
    *   *Answer*: Discuss TDMA slot allocation logic.

## 2. Field Test Checklist
*   **Antenna Polarization**: Verify they are parallel.
*   **Battery Voltage**: Low voltage = lower Tx power.
*   **Spectrum Scan**: Use our tools to check the noise floor before the official flight/test.

## 3. The "Wow" Factor
During the presentation, show the **GCS Telemetry Dashboard** (run `scripts/gui_mockup.py`). The visual representation of real-time SNR and signal bars creates a much stronger professional impression than raw terminal logs.

---
*Strategy by Bahattin Yunus Çetin*
