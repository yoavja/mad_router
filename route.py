import scapy
from scapy.config import conf
from scapy.layers.inet import IP, ICMP
from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff, sendp, send


def route():
    send((IP(dst="192.168.56.4%VirtualBox Host-Only Ethernet Adapter #2") / ICMP()), iface="VirtualBox Host-Only Ethernet Adapter #2")

def main():
    route()

if __name__ == "__main__":
    main()
