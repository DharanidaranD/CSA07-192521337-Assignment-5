"""Network performance metrics from a captured packet trace (e.g. from Wireshark)."""
# (sequence number, send time in ms, receive time in ms or None if lost, size in bytes)
TRACE = [(1, 0, 42, 1200), (2, 20, 61, 1200), (3, 40, 85, 1200),
         (4, 60, None, 1200), (5, 80, 119, 1200), (6, 100, 146, 1200),
         (7, 120, 158, 1200), (8, 140, 190, 1200), (9, 160, None, 1200),
         (10, 180, 222, 1200)]

def metrics(trace):
    got = [(s, tx, rx, b) for s, tx, rx, b in trace if rx is not None]
    # TODO 1 (completed)
    loss = (len(trace) - len(got)) / len(trace) * 100
    delays = [rx - tx for _, tx, rx, _ in got]
    avg_delay = sum(delays) / len(delays)
    jitter = sum(abs(delays[i] - delays[i - 1]) for i in range(1, len(delays))) / (len(delays) - 1)
    bits = sum(b * 8 for _, _, _, b in got)
    throughput = bits / (got[-1][2] - got[0][1])      # bits per ms == kbps
    return loss, avg_delay, jitter, throughput

def report(title, trace):
    loss, d, j, thr = metrics(trace)
    print(title)
    print(f"packet loss {loss:.1f} %")
    print(f"average delay {d:.1f} ms, jitter {j:.1f} ms")
    print(f"throughput {thr:.1f} kbps")
    print("VoIP quality:", "acceptable" if d < 150 and j < 30 and loss < 1 else "poor")

report("== Original trace ==", TRACE)
print()
report("== Lost packets removed (loss hidden, NOT a real improvement) ==", [t for t in TRACE if t[2] is not None])
