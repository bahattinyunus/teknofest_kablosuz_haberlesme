import argparse
import math

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
    class Fore: RED = GREEN = YELLOW = CYAN = RESET = ""
    class Style: BRIGHT = RESET = ""


def estimate_distance(rssi, freq_mhz, ptx=14):
    """
    Estimate theoretical distance based on FSPL (Free Space Path Loss).
    This is highly theoretical and assumes LOS.
    RSSI = Ptx - FSPL
    FSPL = Ptx - RSSI
    20log(d) = FSPL - 20log(f) - 32.44
    """
    fspl = ptx - rssi
    # 20log(d) = fspl - 20log(f) - 32.44
    log_d = (fspl - 20 * math.log10(freq_mhz) - 32.44) / 20
    distance_km = 10 ** log_d
    return distance_km

def interpret_lora_signal(rssi, snr, freq=433):
    """
    Interprets LoRa signal quality based on RSSI and SNR.
    Reference: Semtech SX1276 Datasheet
    """
    print(f"{Fore.CYAN}" + "-" * 50)
    print(f"{Style.BRIGHT}      LORA SIGNAL DIAGNOSTICS{Style.RESET}{Fore.CYAN}")
    print("-" * 50 + f"{Style.RESET}")
    print(f"Input: RSSI={rssi}dBm, SNR={snr}dB, Freq={freq}MHz")
    print("-" * 50)

    # SNR Interpretation
    if snr > 5:
        snr_eval = f"{Fore.GREEN}Excellent (Strong Signal){Style.RESET}"
    elif 0 <= snr <= 5:
        snr_eval = f"{Fore.GREEN}Good (Clear path){Style.RESET}"
    elif -10 <= snr < 0:
        snr_eval = f"{Fore.YELLOW}Average (Recoverable with SF){Style.RESET}"
    else:
        snr_eval = f"{Fore.RED}Critical (Near sensitivity limit){Style.RESET}"

    # RSSI Interpretation (General rule)
    if rssi > -70:
        rssi_eval = f"{Fore.GREEN}Strong{Style.RESET}"
    elif -90 < rssi <= -70:
        rssi_eval = f"{Fore.GREEN}Moderate{Style.RESET}"
    elif -110 < rssi <= -90:
        rssi_eval = f"{Fore.YELLOW}Weak{Style.RESET}"
    else:
        rssi_eval = f"{Fore.RED}Faint (Edge of connection){Style.RESET}"

    print(f"Signal Strength: {rssi_eval}")
    print(f"Noise Resilience: {snr_eval}")
    
    # Distance Estimation
    est_dist = estimate_distance(rssi, freq)
    print(f"Est. Free Space Dist: {Fore.CYAN}~{est_dist:.2f} km{Style.RESET} (Theoretical Max)")
    
    if snr < 0:
        print(f"\n{Fore.YELLOW}[ADVICE] Signal is below noise floor. Increase Spreading Factor (SF) or use Directive Antennas.{Style.RESET}")
    if rssi < -120:
        print(f"\n{Fore.RED}[WARNING] Dangerously close to disconnection.{Style.RESET}")

def main():
    parser = argparse.ArgumentParser(description="LoRa Signal Quality Interpreter")
    parser.add_argument("rssi", type=float, help="Received Signal Strength Indicator (dBm)")
    parser.add_argument("snr", type=float, help="Signal-to-Noise Ratio (dB)")
    parser.add_argument("--freq", type=float, default=433, help="Frequency in MHz (default 433)")
    
    args = parser.parse_args()
    interpret_lora_signal(args.rssi, args.snr, args.freq)

if __name__ == "__main__":
    main()
