# 🔌 Hardware Integration & Wiring Guide

Connecting your RF modules correctly is the first step toward a stable link. This guide covers common transceiver wiring.

## 1. LoRa Module (SX127x) to ESP32/Arduino
Most LoRa modules communicate via SPI.

| Pin (SX127x) | ESP32 Pin | Arduino Uno Pin | Description |
| :--- | :--- | :--- | :--- |
| **VCC** | 3.3V | 3.3V | **CAUTION**: Do not use 5V! |
| **GND** | GND | GND | Common Ground. |
| **SCK** | GPIO 18 | D13 | SPI Clock. |
| **MISO** | GPIO 19 | D12 | SPI Master In Slave Out. |
| **MOSI** | GPIO 23 | D11 | SPI Master Out Slave In. |
| **NSS (CS)**| GPIO 5 | D10 | Chip Select. |
| **DIO0** | GPIO 2 | D2 | Interrupt (Packet Rx). |

## 2. SDR (RTL-SDR / HackRF) Setup
For SDR-based sniffing and analysis:
*   **Antenna Positioning**: Ensure the antenna is vertically polarized (standing upright) for most drone telemetry.
*   **LNA Setting**: Use moderate LNA (Low Noise Amplifier) gain. Too much gain will saturate the ADC and hide actual signals.

## 3. Power Management Tips
*   **Decoupling Capacitors**: Place a 100uF - 470uF capacitor as close as possible to the radio module's VCC/GND pins to prevent voltage drops during high-current Tx bursts.
*   **Thermal**: High-power modules (e.g., 1W LoRa) require heat sinks during continuous operation.

---
*Hardware Guide by Bahattin Yunus Çetin*
