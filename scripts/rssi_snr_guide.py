def interpret_lora_signal(rssi, snr):
    """
    Interprets LoRa signal quality based on RSSI and SNR.
    Reference: Semtech SX1276 Datasheet
    """
    print("-" * 40)
    print(f"LoRa Signal Analysis: RSSI={rssi}dBm, SNR={snr}dB")
    print("-" * 40)

    # SNR Interpretation
    if snr > 5:
        snr_eval = "Excellent (Strong Signal)"
    elif 0 <= snr <= 5:
        snr_eval = "Good (Clear path)"
    elif -10 <= snr < 0:
        snr_eval = "Average (Recoverable with SF)"
    else:
        snr_eval = "Critical (Near sensitivity limit)"

    # RSSI Interpretation (General rule)
    if rssi > -70:
        rssi_eval = "Strong"
    elif -90 < rssi <= -70:
        rssi_eval = "Moderate"
    elif -110 < rssi <= -90:
        rssi_eval = "Weak"
    else:
        rssi_eval = "Faint"

    print(f"Signal Strength: {rssi_eval}")
    print(f"Noise Resilience: {snr_eval}")
    
    if snr < 0:
        print("\n[ADVICE] Signal is below noise floor. Increase Spreading Factor (SF).")

def main():
    import argparse
    parser = argparse.ArgumentParser(description="LoRa Signal Quality Interpreter")
    parser.add_argument("rssi", type=float, help="Received Signal Strength Indicator (dBm)")
    parser.add_argument("snr", type=float, help="Signal-to-Noise Ratio (dB)")
    
    args = parser.parse_args()
    interpret_lora_signal(args.rssi, args.snr)

if __name__ == "__main__":
    main()
