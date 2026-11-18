"""Task A1: delay breakdown and bandwidth-delay product."""
def delays(rate_bps, links=4, size_B=1500, dist_m=2_000_000, v=2e8, routers=3, q=0.5e-3, p=0.1e-3):
    tx = links * size_B * 8 / rate_bps      # store-and-forward: one transmission per link
    prop = dist_m / v
    queue = routers * q
    proc = routers * p
    return tx, prop, queue, proc, tx + prop + queue + proc

for rate in (100e6, 1e9):
    tx, prop, qd, pr, tot = delays(rate)
    print(f"Link {rate/1e6:.0f} Mbps: tx={tx*1e3:.3f} ms prop={prop*1e3:.3f} ms queue={qd*1e3:.3f} ms proc={pr*1e3:.3f} ms TOTAL={tot*1e3:.3f} ms  (propagation share {prop/tot*100:.1f}%)")

bw, rtt = 1e9, 0.080
bdp = bw * rtt
print(f"\nBDP = {bdp/1e6:.0f} Mbit = {bdp/8/1e6:.1f} MB")
win = 64 * 1024 * 8
thr = win / rtt
print(f"64 KB window -> max throughput = {thr/1e6:.2f} Mbps = {thr/bw*100:.2f}% of the link")
print(f"Window needed to fill the link = {bdp/8/1024:.0f} KiB")
