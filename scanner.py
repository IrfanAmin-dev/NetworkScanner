import scapy.all as scapy
import argparse
import requests

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--target', dest='target', help='Target IP Address/Addresses')
    options = parser.parse_args()

    if not options.target:
        parser.error("[-] Please specify an IP Address or Addresses, use --help for more info.")
    return options

def scan(ip):
    arp_req_frame = scapy.ARP(pdst=ip)
    broadcast_ether_frame = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    broadcast_ether_arp_req_frame = broadcast_ether_frame / arp_req_frame

    answered_list = scapy.srp(broadcast_ether_arp_req_frame, timeout=1, verbose=False)[0]
    result = []
    for sent, received in answered_list:
        client_dict = {"ip": received.psrc, "mac": received.hwsrc}
        result.append(client_dict)

    return result

def get_vendor(mac):
    try:
        url = f"https://api.macvendors.com/{mac}"
        vendor = requests.get(url, timeout=3).text
        return vendor
    except:
        return "Unknown Vendor"

def display_result(result):
    print("---------------------------------------------------------------")
    print("IP Address\t\tMAC Address\t\tVendor")
    print("---------------------------------------------------------------")
    for device in result:
        print(f"{device['ip']}\t{device['mac']}\t{get_vendor(device['mac'])}")

if __name__ == "__main__":
    options = get_args()
    scanned_output = scan(options.target)
    display_result(scanned_output)
