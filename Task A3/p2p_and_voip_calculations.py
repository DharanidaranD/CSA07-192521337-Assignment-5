"""Task A3: distribution time (client-server, P2P, CDN) and VoIP bandwidth."""
F = 4e9 * 8            # 4 GB in bits
N = 20
us, d, u = 100e6, 50e6, 20e6
d_cs = max(N * F / us, F / d)
d_p2p = max(F / us, F / d, N * F / (us + N * u))
print(f"Client-server: N*F/us={N*F/us:.0f} s, F/dmin={F/d:.0f} s -> {d_cs:.0f} s ({d_cs/60:.1f} min)")
print(f"Peer-to-peer : F/us={F/us:.0f} s, F/dmin={F/d:.0f} s, NF/(us+sum u)={N*F/(us+N*u):.0f} s -> {d_p2p:.0f} s ({d_p2p/60:.1f} min)")
print(f"P2P speed-up = {d_cs/d_p2p:.1f}x")

# CDN: 1 Gbps edge per region. Origin must fill R edge servers once (pre-positioning).
for regions in (1, 5, 20):
    fill = regions * F / us
    deliver = F / d                      # each centre pulls from its edge at its 50 Mbps downlink
    print(f"CDN, {regions:>2} edge(s): origin fill={fill:.0f} s (off-peak, once), centre download={deliver:.0f} s, first-ever distribution={fill+deliver:.0f} s (no pipelining)")

# VoIP G.711
rate, ptime, hdr = 64_000, 0.020, 40
pps = 1 / ptime
payload = rate * ptime / 8
ip_bw = (payload + hdr) * 8 * pps
eth_bw = (payload + hdr + 18) * 8 * pps
print(f"\nVoIP: {pps:.0f} pps, payload {payload:.0f} B, IP bandwidth {ip_bw/1e3:.1f} kbps/direction, with Ethernet {eth_bw/1e3:.1f} kbps")
link = 2e6
print(f"Calls on 2 Mbps: {int(link//ip_bw)} (IP only), {int(link//eth_bw)} (with Ethernet), {int(0.7*link//eth_bw)} at 70% utilisation")
