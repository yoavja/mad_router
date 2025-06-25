import scapy
from scapy.sendrecv import sniff, sendp


def route():
    """
    Runs an infinite loop that sends all packets received from enp0s8 to enp0s9
    and all packets received from enp0s9 to enp0s8.
    """
    while 1:
        a = sniff(iface=["enp0s9","enp0s8"], count=2)
        if a[0].sniffed_on == "enp0s9":
            sendp(a[0], iface="enp0s8")
        elif a[0].sniffed_on == "enp0s8":
            sendp(a[0], iface="enp0s9")


def main():
    route()

if __name__ == "__main__":
    main()
