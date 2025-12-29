import math
import argparse
try:
    from colorama import init, Fore, Style
    init()
    # Ensure Style.RESET exists, otherwise alias it to RESET_ALL or empty
    if not hasattr(Style, 'RESET'):
        if hasattr(Style, 'RESET_ALL'):
            Style.RESET = Style.RESET_ALL
        else:
            Style.RESET = ""
except ImportError:
    # Fallback if colorama is not installed
    class Fore: RED = GREEN = YELLOW = CYAN = RESET = ""
    class Style: BRIGHT = RESET = ""


def calculate_fspl(frequency_mhz, distance_km):
    """
    Calculate Free Space Path Loss (FSPL) in dB.
    Formula: FSPL = 20log10(d) + 20log10(f) + 32.44
    """
    return 20 * math.log10(distance_km) + 20 * math.log10(frequency_mhz) + 32.44

def calculate_link_budget(ptx, gtx, ltx, distance_km, freq_mhz, grx, lrx, sensitivity=None):
    """
    Calculate Received Power (Prx) and check against Link Margin.
    """
    fspl = calculate_fspl(freq_mhz, distance_km)
    prx = ptx + gtx - ltx - fspl + grx - lrx
    
    margin = None
    if sensitivity is not None:
        margin = prx - sensitivity
        
    return prx, fspl, margin

def main():
    parser = argparse.ArgumentParser(description="Wireless-Architect: Link Budget Calculator")
    parser.add_argument("--ptx", type=float, default=14, help="Transmitter power (dBm)")
    parser.add_argument("--gtx", type=float, default=2.15, help="Transmitter antenna gain (dBi)")
    parser.add_argument("--ltx", type=float, default=1.0, help="Transmitter cable loss (dB)")
    parser.add_argument("--dist", type=float, required=True, help="Distance between nodes (km)")
    parser.add_argument("--freq", type=float, default=433, help="Frequency (MHz)")
    parser.add_argument("--grx", type=float, default=2.15, help="Receiver antenna gain (dBi)")
    parser.add_argument("--lrx", type=float, default=1.0, help="Receiver cable loss (dB)")
    parser.add_argument("--sens", type=float, default=None, help="Receiver Sensitivity (dBm) e.g. -137")
    
    args = parser.parse_args()

    prx, fspl, margin = calculate_link_budget(args.ptx, args.gtx, args.ltx, args.dist, args.freq, args.grx, args.lrx, args.sens)

    print(f"{Fore.CYAN}" + "-" * 50)
    print(f"{Style.BRIGHT}      WIRELESS-ARCHITECT LINK BUDGET CALCULATOR{Style.RESET}{Fore.CYAN}")
    print("-" * 50 + f"{Style.RESET}")
    print(f"Frequency:      {Fore.YELLOW}{args.freq} MHz{Style.RESET}")
    print(f"Distance:       {Fore.YELLOW}{args.dist} km{Style.RESET}")
    print(f"Path Loss:      {Fore.RED}{fspl:.2f} dB{Style.RESET}")
    print("-" * 50)
    print(f"TX Power:       {args.ptx} dBm")
    print(f"Total Gain:     {args.gtx + args.grx} dBi")
    print(f"Total Loss:     {args.ltx + args.lrx + fspl:.2f} dB")
    print("-" * 50)
    
    color = Fore.GREEN if prx > -100 else Fore.YELLOW
    if args.sens and prx < args.sens: color = Fore.RED

    print(f"RX Power (Prx): {color}{prx:.2f} dBm{Style.RESET}")

    if margin is not None:
        print(f"Sensitivity:    {args.sens} dBm")
        margin_color = Fore.GREEN if margin > 10 else (Fore.YELLOW if margin > 0 else Fore.RED)
        print(f"Link Margin:    {margin_color}{margin:.2f} dB{Style.RESET}")
        
        if margin <= 0:
            print(f"\n{Fore.RED}[CRITICAL] Link is NOT feasible! Signal is below sensitivity.{Style.RESET}")
        elif margin < 10:
            print(f"\n{Fore.YELLOW}[WARNING] Low margin. Fading or obstruction may break the link.{Style.RESET}")
        else:
            print(f"\n{Fore.GREEN}[SUCCESS] Strong link budget.{Style.RESET}")
    else:
        print(f"\n{Style.BRIGHT}Tip: Provide --sens parameter to calculate Link Margin.{Style.RESET}")

if __name__ == "__main__":
    main()
