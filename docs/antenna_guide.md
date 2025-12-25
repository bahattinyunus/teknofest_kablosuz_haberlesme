# 📡 Antenna Selection & Design Guide

In wireless communication, the antenna is the most critical element for signal quality. This guide covers common types used in TEKNOFEST projects.

---

## 🏗️ Common Antenna Types

### 1. Dipole Antenna
*   **Description:** A simple T-shaped antenna consisting of two identical conductive elements.
*   **Gain:** Typically **2.15 dBi**.
*   **Usage:** General purpose, omnidirectional (donut shape).
*   **Elite Tip:** Length should be exactly $\lambda/2$ for resonance.

### 2. Monopole (Whip) Antenna
*   **Description:** Half a dipole mounted over a ground plane.
*   **Usage:** Handheld devices, vehicles.
*   **Elite Tip:** Requires a good ground plane to function efficiently.

### 3. Yagi-Uda (Directional)
*   **Description:** Consists of a driven element and multiple parasitic elements (directors and a reflector).
*   **Gain:** **7 dBi to 15+ dBi**.
*   **Usage:** Point-to-point long-range links (e.g., ground station to drone).
*   **Elite Tip:** Must be pointed accurately at the target.

---

## 📏 Radiation Patterns
Understanding where your energy goes:
- **Omnidirectional:** 360-degree coverage in the horizontal plane.
- **Directional:** Focuses energy in one direction for extreme distance.

---

## 🛠️ Matching and SWR
- **SWR (Standing Wave Ratio):** Measures how much power is reflected back.
- **Ideal:** 1.0:1 (Perfect matching).
- **Acceptable:** Below 1.5:1.
- **Dangerous:** Above 3.0:1 (Can damage transmitter).

---

© 2025 Wireless-Architect | Bahattin Yunus Çetin
