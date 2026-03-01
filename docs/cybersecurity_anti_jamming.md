# 🛡️ Cybersecurity & Anti-Jamming Tactical Guide

In TEKNOFEST and real-world aeronautical missions, securing the communication link is as important as the range. This guide covers the primary threats and countermeasures.

## 1. Encryption (AES-256)
Never send telemetry data in plain text.
*   **Implementation**: Use the `Crypto.Cipher` library in Python or dedicated hardware AES engines in MCUs (like ESP32/STM32).
*   **Key Management**: Rotate keys and never store them in public GitHub repositories.

## 2. Anti-Jamming: FHSS (Frequency Hopping)
If a jammer blocks a specific frequency, your system must hop to another.
*   **Algorithm**: Use a pseudo-random seed known only to the transmitter and receiver.
*   **Dwell Time**: The shorter the time spent on one frequency, the harder it is to jam.

## 3. Replay Protection (Nonce & Timestamps)
Attackers can capture valid packets and "replay" them later (e.g., a "Disarm" command).
*   **Countermeasure**: Each packet must include a unique Sequence Number or Timestamp.
*   **Validation**: The receiver must reject any packet with a sequence number lower or equal to the last received one.

## 4. Man-in-the-Middle (MitM) Attacks
An attacker spoofing the Ground Control Station (GCS).
*   **Solution**: Use HMAC (Hash-based Message Authentication Code) to verify that the message truly came from the authorized GCS.

---
*Developed by Bahattin Yunus Çetin*
