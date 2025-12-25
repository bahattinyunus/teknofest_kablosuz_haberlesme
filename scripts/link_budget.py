import math
import argparse

def calculate_fspl(frequency_mhz, distance_km):
    """
    Calculate Free Space Path Loss (FSPL) in dB.
    Formula: FSPL = 20log10(d) + 20log10(f) + 32.44
    """
    return 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz) + 32.44

def calculate_link_budget(ptx, gtx, ltx, distance_km, freq_mhz, grx, lrx, margin):
    """
    Calculate Received Power (Prx) and check against Link Margin.
    """
    fspl = calculate_fspl(freq_mhz, distance_km)
    prx = ptx + gtx - ltx - fspl + grx - lrx
    effective_margin = prx - margin  # Simplistic, margin usually defined against sensitivity
    
    return prx, fspl

def main():
    parser = argparse.ArgumentParser(description="Wireless-Architect: Link Budget Calculator")
    parser.add_argument("--ptx", type=float, default=14, help="Transmitter power (dBm)")
    parser.add_argument("--gtx", type=float, default=2.15, help="Transmitter antenna gain (dBi)")
    parser.add_argument("--ltx", type=float, default=1.0, help="Transmitter cable loss (dB)")
    parser.add_argument("--dist", type=float, required=True, help="Distance between nodes (km)")
    parser.add_argument("--freq", type=float, default=433, help="Frequency (MHz)")
    parser.add_argument("--grx", type=float, default=2.15, help="Receiver antenna gain (dBi)")
    parser.add_argument("--lrx", type=float, default=1.0, help="Receiver cable loss (dB)")
    
    args = parser.parse_args()

    prx, fspl = calculate_link_budget(args.ptx, args.gtx, args.ltx, args.dist, args.freq, args.grx, args.lrx, 0)

    print("-" * 40)
    print("      WIRELESS-ARCHITECT LINK BUDGET")
    print("-" * 40)
    print(f"Frequency:      {args.freq} MHz")
    print(f"Distance:       {args.dist} km")
    print(f"Path Loss:      {fspl:.2f} dB")
    print("-" * 40)
    print(f"TX Power:       {args.ptx} dBm")
    print(f"RX Power (Prx): {prx:.2f} dBm")
    print("-" * 40)
    print("Note: Compare Prx with your module sensitivity (e.g., -137 dBm for LoRa).")

if __name__ == "__main__":
    main()
