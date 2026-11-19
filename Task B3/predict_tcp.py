"""Theoretical TCP throughput to compare with tc netem measurements (B3.1 / B3.2)."""
from math import sqrt
LINK, MSS = 100e6, 1460 * 8
print("Predicted TCP throughput, 100 Mbps link, MSS 1460 B (min of link, window/RTT, Mathis)")
print(f"{'RTT ms':>7} {'loss %':>7} {'64KB window':>12} {'1MB window':>11}")
for rtt in (0.001, 0.050, 0.150, 0.300):
    for loss in (0, 0.01, 0.05, 0.10):
        m = MSS / rtt * 1.22 / sqrt(loss) if loss else float('inf')
        row = []
        for w in (64 * 1024 * 8, 1024 * 1024 * 8):
            row.append(min(LINK, w / rtt, m) / 1e6)
        print(f"{rtt*1e3:>7.0f} {loss*100:>7.0f} {row[0]:>9.2f} Mb {row[1]:>8.2f} Mb")
print("\nWindow needed to fill 100 Mbps:", *(f"RTT {r*1e3:.0f} ms -> {100e6*r/8/1024:.0f} KiB;" for r in (0.05, 0.15, 0.3)))
