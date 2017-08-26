#!/usr/bin/env python

#======================================#
# IA 612 - Joshua Faust & ...          #
# Scapy Packet Fragmentation Example   #
#======================================#

import sys
from scapy.all import sr1,IP,ICMP,TCP,Raw,send,fragment

if len(sys.argv) !=2:
    print "ERROR: please enter arguments: "
    print "Usage: ./frag.py <ipaddr>"
    sys.exit(1)

# Create a packet and load your data 
data = "This is not malicious code but, this is!!!!!......."
packet = IP(dst=sys.argv[1]) / TCP() / Raw(load=data)
print sys.getsizeof(data)

#Fragment the packet and send
frags = fragment(packet,fragsize=8)
for f in frags:
    f.show()
    send(f)
    
