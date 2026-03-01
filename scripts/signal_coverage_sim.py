import math
import argparse

def calculate_rssi(p_tx, g_tx, g_rx, freq, dist, n=2.0):
    """
    p_tx: Transmit power in dBm
    g_tx: Transmit antenna gain in dBi
    g_rx: Receive antenna gain in dBi
    freq: Frequency in MHz
    dist: Distance in meters
    n: Path loss exponent (2 for free space, 3-4 for urban)
    """
    if dist <= 0: return p_tx
    
    # Speed of light
    c = 3e8
    wavelength = c / (freq * 1e6)
    
    # Path loss (Log-Distance Path Loss Model)
    # L = 20log10(4*pi*d0 / lambda) + 10 * n * log10(d / d0)
    # Using d0 = 1m
    pl_d0 = 20 * math.log10((4 * math.pi * 1) / wavelength)
    pl = pl_d0 + 10 * n * math.log10(dist)
    
    rssi = p_tx + g_tx + g_rx - pl
    return rssi

def simulate_grid(size_m, step, p_tx, g_tx, g_rx, freq, n):
    print(f"--- Signal Coverage Simulation ({size_m}x{size_m} meters) ---")
    print(f"Freq: {freq} MHz, Ptx: {p_tx} dBm, n: {n}")
    print("-" * 50)
    
    for y in range(0, size_m + 1, step):
        row = ""
        for x in range(0, size_m + 1, step):
            dist = math.sqrt(x**2 + y**2)
            rssi = calculate_rssi(p_tx, g_tx, g_rx, freq, dist, n)
            
            if rssi > -70: row += "🟢 " # Strong
            elif rssi > -100: row += "🟡 " # Moderate
            elif rssi > -120: row += "🔴 " # Weak
            else: row += "💀 " # Disconnected
        print(row)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="RF Signal Coverage Simulator")
    parser.add_argument("--size", type=int, default=1000, help="Grid size in meters")
    parser.add_argument("--step", type=int, default=100, help="Simulation step")
    parser.add_argument("--ptx", type=float, default=14, help="Transmit power in dBm")
    parser.add_argument("--freq", type=float, default=433, help="Frequency in MHz")
    parser.add_argument("--n", type=float, default=2.5, help="Path loss exponent")
    
    args = parser.parse_args()
    simulate_grid(args.size, args.step, args.ptx, 3.0, 3.0, args.freq, args.n)
