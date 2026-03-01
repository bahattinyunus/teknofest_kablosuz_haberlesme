import random
import argparse

def simulate_csma_ca(nodes, packets, collision_window=0.1):
    """
    nodes: Number of nodes attempting to transmit
    packets: Number of packets each node wants to send
    collision_window: Probability of collision if two nodes start at similar time
    """
    total_attempts = nodes * packets
    successful = 0
    collisions = 0
    
    # Simplified CSMA/CA Simulation
    timeline = [0] * (total_attempts * 2) 
    
    for _ in range(total_attempts):
        slot = random.randint(0, len(timeline)-1)
        if timeline[slot] == 0:
            timeline[slot] = 1 # Clear to send
            successful += 1
        else:
            collisions += 1
            
    throughput = (successful / total_attempts) * 100
    return successful, collisions, throughput

def simulate_tdma(nodes, packets):
    """
    TDMA has 0 collisions by design as each node has a fixed slot.
    """
    total_packets = nodes * packets
    successful = total_packets # Guaranteed in ideal TDMA
    collisions = 0
    throughput = 100.0
    return successful, collisions, throughput

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAC Layer Performance Simulator")
    parser.add_argument("--nodes", type=int, default=5, help="Number of nodes")
    parser.add_argument("--packets", type=int, default=20, help="Packets per node")
    
    args = parser.parse_args()
    
    print(f"--- MAC Layer Performance Simulation ({args.nodes} nodes) ---")
    
    # Run CSMA
    c_s, c_c, c_t = simulate_csma_ca(args.nodes, args.packets)
    print(f"[CSMA/CA] Success: {c_s}, Collisions: {c_c}, Throughput: {c_t:.2f}%")
    
    # Run TDMA
    t_s, t_c, t_t = simulate_tdma(args.nodes, args.packets)
    print(f"[TDMA   ] Success: {t_s}, Collisions: {t_c}, Throughput: {t_t:.2f}%")
    
    print("-" * 50)
    print("Strategy: Use TDMA for high-density swarm control; Use CSMA/CA for sporadic sensor data.")
