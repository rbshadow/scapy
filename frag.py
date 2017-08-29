#!/usr/bin/env python

# ======================================#
# IA 612 - Joshua Faust & ...          #
# Scapy Packet Fragmentation Example   #
# ======================================#

import sys
from scapy.all import sr1, IP, ICMP, TCP, Raw, send, fragment

if len(sys.argv) != 2:
    print
    "ERROR: please enter arguments: "
    print
    "Usage: ./frag.py <ipaddr>"
    sys.exit(1)

# Packet Data
data = ["ABCDEFGH","HACKEEDD","TESTTEST"]
flags = [1,1,0]
frag = [0,1,2]

#craft IP and ICMP packets


# Create a packet and load your data
for i in range(0,3):
    ip=IP(dst=sys.argv[1], proto=1, id=44444, flags=flags[i], frag=frag[i])
    icmp=ICMP(type=8, code=0, chksum=0x97b7)

    if (i==0):
        packet=ip/icmp/data[i]
    else:
        packet=ip/data[i]

    print(sys.getsizeof(data))
    print("Number" + str(i+1))
    packet.show()
    send(packet)

