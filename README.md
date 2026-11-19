# CSA07 – Computer Networks: Assignment 5 (CO5)
**Topic:** Measuring Network Performance and Securing Applications  

## Student Information
* **Name:** Dharanidaran D
* **Register Number:** 192521337
* **Course Code & Title:** CSA07 – Computer Networks
* **Course Outcome:** CO5 (Measuring Network Performance and Securing Applications)
* **GitHub Repository:** https://github.com

---

## System Environment & Tools Used
* **Operating System:** Windows 11 / Ubuntu Linux *(update as applicable)*
* **Python Version:** Python 3.x
* **Network Simulators:** Cisco Packet Tracer 8.x / NS-3 *(update as applicable)*
* **Measurement & Analysis Tools:** Wireshark, `ping`, `traceroute` / `tracert`, `iperf3`, Linux `tc netem`

---

## Repository Structure

```text
CSA07-192521337-Assignment-5/
├── README.md
├── Report/
│   └── CSA07_Assignment_5_CO5_Report.pdf
├── TaskA1/
│   ├── delay_and_bdp_calculations.py
│   └── taskA1_analysis.txt
├── TaskA2/
│   └── taskA2_protocol_analysis.txt
├── TaskA3/
│   ├── p2p_and_voip_calculations.py
│   └── taskA3_analysis.txt
├── TaskA4/
│   ├── firewall_filter.py
│   ├── firewall_output.txt
│   ├── taskA4_analysis.txt
│   └── screenshots/
├── TaskA5/
│   └── taskA5_dos_analysis.txt
├── TaskB1/
│   ├── capture_metrics.py
│   ├── call_capture.pcapng
│   ├── ping_traceroute_logs.txt
│   ├── iperf3_logs.txt
│   ├── taskB1_analysis.txt
│   └── screenshots/
├── TaskB2/
│   ├── company_network_sim.pkt
│   ├── alt_simulator_run.cc
│   ├── simulation_results.txt
│   └── screenshots/
├── TaskB3/
│   ├── firewall_and_qos_config.txt
│   ├── netem_and_flood_logs.txt
│   ├── taskB3_tradeoff_analysis.txt
│   └── screenshots/
└── TaskB4/
    └── taskB4_engineering_decision.txt
```

---

## Instructions to Run Programs and Open Simulations

### 1. Python Scripts (`TaskA4` & `TaskB1`)
Ensure Python 3 is installed on your machine, navigate to the respective task folder, and execute:
```bash
# Task A4: Stateless Packet-Filter Firewall Simulation
cd TaskA4
python firewall_filter.py

# Task B1: Voice Packet Capture Delay, Jitter, and Loss Calculator
cd ../TaskB1
python capture_metrics.py
```

### 2. Network Simulations & Captures (`TaskB1`, `TaskB2`, `TaskB3`)
* **Wireshark Capture (`TaskB1`):** Open `TaskB1/call_capture.pcapng` in Wireshark to inspect RTP packet intervals, jitter, and packet loss.
* **Cisco Packet Tracer (`TaskB2` & `TaskB3`):** Open `.pkt` files using Cisco Packet Tracer (version 8.0 or higher) to verify priority queueing, firewall ACLs, and background traffic behavior.
* **NS-3 / Linux Lab Logs (`TaskB2` & `TaskB3`):** Review the `.cc` simulation scripts and command-line logs (`netem_and_flood_logs.txt`) for `tc netem` delay/loss and rate-limiting results.

---

## Summary of Results by Task

### Part A – Design & Theoretical Analysis
* **Task A1 (Delay and Metrics):** Computed transmission, propagation, queueing, and processing delays along with bandwidth–delay products (BDP). Defined QoS target thresholds for live video, voice, recorded video, e-mail, and bulk file downloads.
* **Task A2 (Application-Layer Protocols):** Mapped the complete SMTP handshake and reply codes, contrasted POP3 vs. IMAP, active vs. passive FTP, and SNMP GET vs. TRAP, and analyzed browser DNS/HTTP timings.
* **Task A3 (Peer-to-Peer, VoIP, and Overlays):** Calculated file distribution times across client–server, P2P, and 1 Gbps CDN architectures, derived G.711 VoIP bandwidth requirements, and explained SIP/RTP roles and VPN/CDN overlays.
* **Task A4 (SSL/TLS and Firewalls):** Implemented `firewall_filter.py` to demonstrate how rule ordering affects packet filtering (original vs. swapped rules), designed a corrected stateful/stateless rule set, and compared TLS 1.3 and Cloud WAF protections.
* **Task A5 (Denial-of-Service Protection):** Calculated SYN-flood packet rates, analyzed SYN cookies and DNS reflection/amplification attacks, and evaluated four-server load capacity under mitigated traffic.

### Part B – Implementation & Experimental Investigation
* **Task B1 (Measure a Real Network):** Measured real-world RTT, hop count, and wired vs. wireless throughput using `ping`, `traceroute`, and `iperf3`. Executed `capture_metrics.py` to compute voice delay, jitter, and loss with and without dropped packets, comparing results against Task A1 targets.
* **TaskB2 (Simulate Under Varying Conditions):** Simulated baseline vs. heavy background download traffic in a multi-branch network and verified that strict priority queueing protects VoIP latency and jitter. Cross-validated findings using an alternative simulator.
* **TaskB3 (Performance Under Stress and Attack):** Tested TCP window scaling and link degradation under `tc netem` delay/loss, enforced firewall rules, verified rate-limiting against isolated lab flood traffic, and compared DiffServ EF against Weighted Fair Queuing (WFQ).
* **TaskB4 (Final Engineering Decision):** Projected performance under 2× user load and cross-continent latency, validated rate-limit thresholds, and recommended a regional server + QoS/WAF architecture balancing cost and end-to-end delay.
