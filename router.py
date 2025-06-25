import scapy
from scapy.layers.l2 import Ether
from scapy.sendrecv import sniff, sendp

BROADCAST = "ff:ff:ff:ff:ff:ff"
MAC_56 = "08:00:27:47:65:4f"
MAC_22 = "08:00:27:0b:4b:2a"
IFACE_56 = "enp0s8"
IFACE_22 = "enp0s9"

def send_it(a):
    a[Ether].dst = BROADCAST
    if a.sniffed_on == IFACE_22:
        a[Ether].src = MAC_56
        sendp(a, iface=IFACE_56)
    elif a.sniffed_on == IFACE_56:
        a[Ether].src = MAC_22
        sendp(a, iface=IFACE_22)


def route():
    """
        Runs an infinite loop that sends all packets received from enp0s8 to enp0s9
        and all packets received from enp0s9 to enp0s8.
    """
    sniff(iface=[IFACE_22,IFACE_56], prn=send_it)


def main():
    route()

if __name__ == "__main__":
    main()
