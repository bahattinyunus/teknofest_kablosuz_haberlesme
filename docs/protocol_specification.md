# 📡 Architect Protocol Specification (v1.0)

This document formalizes the communication frame structure used by the Wireless-Architect system.

## 1. Frame Structure Overview
The protocol uses a fixed-header, variable-payload architecture designed for efficiency and error resilience.

| Preamble (2B) | Header (4B) | Payload (0-248B) | CRC-16 (2B) |
| :--- | :--- | :--- | :--- |
| `0xAA 0x55` | See Below | Data | Checksum |

## 2. Header Definition (4 Bytes)
| Bit Range | Field | Description |
| :--- | :--- | :--- |
| `0-7` | **Node ID** | Unique identifier for the transmitter (0-255). |
| `8-15` | **Type** | `0x01`: Telemetry, `0x02`: Command, `0x03`: ACK, `0x04`: Emergency. |
| `16-23` | **Length** | Total size of the payload in bytes. |
| `24-31` | **Sequence** | Rolling counter (0-255) for replay protection. |

## 3. Payload Types
### 0x01: Telemetry (Drones/UGVs)
*   **Byte 0-3**: Latitude (float32)
*   **Byte 4-7**: Longitude (float32)
*   **Byte 8-9**: RSSI (int16)

### 0x02: Command
*   **Byte 0**: Command ID (e.g., `0xA1` = Arm, `0xB2` = Disarm)
*   **Byte 1-N**: Optional parameters

## 4. Error Handling
*   **CRC-16**: If CRC fails, the packet is silently dropped to prevent malformed command execution.
*   **ACK Mechanism**: For critical commands, the receiver must reply with a Type `0x03` packet within 100ms.

---
*Architect Protocol Spec v1.0*
