#!/usr/bin/env python

#======================================#
# IA 612 - Joshua Faust & ...          #
# Scapy Packet Fragmentation Example   #
#======================================#

import sys
from scapy.all import sr1,IP,ICMP,TCP,Raw,sendp

if len(sys.argv) !=2:
    print "ERROR: please enter arguments: "
    print "Usage: ./frag.py <ipaddr>"
    sys.exit(1)

data = "This is a test string"
p = IP(dst=sys.argv[1]) / TCP() / Raw(load=data)
sendp(p)
p.show()
