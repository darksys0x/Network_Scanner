#!/usr/bin/env python

import scapy.all as scap


def scann(ip):
    #creat ARP request directry to brodcast MAC asking for IP,,
  
    RequestOf_ARP = scap.ARP(pdst=ip)
    brodcast = scap.Ether(dst='ff:ff:ff:ff:ff:ff')
    RequestOf_ARP_brodcast = brodcast/RequestOf_ARP
    print("*" * 50)
    print(RequestOf_ARP_brodcast.summary())
    print("*" * 50)
    #scap.ls(scap.ARP()) #  this for list options your intrested

scann('192.168.217.1/24')
