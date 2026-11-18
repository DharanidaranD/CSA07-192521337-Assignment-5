"""A stateless packet filter: the first matching rule decides (like iptables)."""
RULES = [ # (action, protocol, destination port or None for any, source prefix or None)
    ("allow", "tcp", 443, None),
    ("allow", "tcp", 22, "10.1."),
    ("deny", "tcp", 22, None),
    ("allow", "udp", 53, None),
]
DEFAULT = "deny"

def decide(proto, port, src):
    for action, p, dport, prefix in RULES:
        # TODO 1 (completed): first matching rule decides
        if p == proto and (dport is None or dport == port) and (prefix is None or src.startswith(prefix)):
            return action
    return DEFAULT

packets = [("tcp", 443, "49.37.2.8"), ("tcp", 22, "10.1.4.20"),
           ("tcp", 22, "49.37.2.8"), ("udp", 53, "10.1.4.20"),
           ("tcp", 80, "49.37.2.8"), ("icmp", None, "49.37.2.8")]
for pk in packets:
    print(f"{pk[0]:<5} {str(pk[1]):<5} from {pk[2]:<10} -> {decide(*pk)}")

# Experiment: swap rules 2 and 3 (deny SSH first) and record the change
print("\n--- After swapping rule 2 and rule 3 ---")
RULES[1], RULES[2] = RULES[2], RULES[1]
for pk in packets:
    print(f"{pk[0]:<5} {str(pk[1]):<5} from {pk[2]:<10} -> {decide(*pk)}")

# Experiment: the ORIGINAL assignment rule order (allow tcp any->22 first) -- shows the hole
print("\n--- Original rule set from A4.2 (allow ssh from ANY first) ---")
RULES[:] = [("allow", "tcp", 443, None), ("allow", "tcp", 22, None), ("deny", "tcp", 22, None),
            ("allow", "tcp", 22, "10.1."), ("allow", "udp", 53, None)]
for pk in packets:
    print(f"{pk[0]:<5} {str(pk[1]):<5} from {pk[2]:<10} -> {decide(*pk)}")
