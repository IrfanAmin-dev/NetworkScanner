# 🛰️ Python Network Scanner

A simple Python-based ARP network scanner built with [Scapy](https://scapy.net/).  
It discovers active devices on your local network and shows their **IP addresses**, **MAC addresses**, and **vendor/manufacturer**.

---

## ✨ Features
- Scans a target IP range (e.g. `192.168.0.1/24`)  
- Discovers live hosts on your local LAN  
- Displays **IP + MAC address + vendor** for each device  
- Works on Windows, Linux, and macOS  

---

## ⚡ Requirements
- Python 3.7+  
- [Scapy](https://scapy.net/)  
- [Requests](https://pypi.org/project/requests/)  


Install dependencies with:
```bash
pip install scapy requests
```

## Example Output
```bash
---------------------------------------------------------------
IP Address        MAC Address           Vendor
---------------------------------------------------------------
192.168.0.1       00:11:22:33:44:55     TP-Link Technologies
192.168.0.5       F4:92:BF:12:34:56     Apple, Inc.
192.168.0.10      3C:5A:B4:65:43:21     Samsung Electronics
192.168.0.20      BC:30:5B:AA:BB:CC     Amazon Technologies Inc.
```
