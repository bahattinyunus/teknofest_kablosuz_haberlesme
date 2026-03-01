import time
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_gauge(label, value, max_val, unit):
    bar_len = 20
    filled_len = int(bar_len * value / max_val)
    bar = "█" * filled_len + "░" * (bar_len - filled_len)
    print(f"{label:15}: [{bar}] {value:6.1f} {unit}")

def run_gcs_mockup():
    print("Initializing Architect Ground Control Station (GCS)...")
    time.sleep(1)
    
    try:
        while True:
            clear_screen()
            print("="*50)
            print("   ARCHITECT GCS - REAL-TIME TELEMETRY STREAM   ")
            print("="*50)
            print(f"Time: {time.strftime('%H:%M:%S')} | Link: [ACTIVE] | Protocol: v1.0")
            print("-"*50)
            
            # Simulated Data
            rssi = random.uniform(-105, -70)
            snr = random.uniform(-15, 12)
            battery = random.uniform(14.8, 16.8)
            distance = random.uniform(500, 5000)
            
            draw_gauge("Signal Power", rssi + 120, 60, "dBm") # Scaled for bar
            draw_gauge("SNR Level", snr + 20, 40, "dB")
            draw_gauge("Batt Voltage", battery, 17, "V")
            draw_gauge("Drone Dist", distance, 10000, "m")
            
            print("-"*50)
            print("LOGS:")
            if rssi < -100:
                print("[WARN] Link degradation detected!")
            if snr < 0:
                print("[INFO] Operating below noise floor (LoRa magic).")
            print("[TX] Heartbeat sent.")
            
            print("\nPress Ctrl+C to terminate GCS simulation.")
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nGCS Terminated.")

if __name__ == "__main__":
    run_gcs_mockup()
