import pytest
import math
import sys
import os

# Add scripts directory to path for imports
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scripts'))

from link_budget import calculate_link_budget
from signal_coverage_sim import calculate_rssi
from mac_layer_sim import simulate_csma_ca, simulate_tdma

def test_link_budget_math():
    # Test with known values
    # calculate_link_budget(p_tx, g_tx, g_rx, freq, dist)
    result = calculate_link_budget(14, 3, 3, 433, 1000)
    assert result < 0 # RSSI should be negative
    assert isinstance(result, float)

def test_rssi_coverage_logic():
    rssi_close = calculate_rssi(14, 3, 3, 433, 10)
    rssi_far = calculate_rssi(14, 3, 3, 433, 1000)
    assert rssi_close > rssi_far # Closer should be stronger

def test_mac_sim_logic():
    nodes = 5
    packets = 10
    total = nodes * packets
    
    # CSMA
    s, c, t = simulate_csma_ca(nodes, packets)
    assert s + c == total
    assert 0 <= t <= 100
    
    # TDMA
    ts, tc, tt = simulate_tdma(nodes, packets)
    assert tc == 0
    assert tt == 100.0
