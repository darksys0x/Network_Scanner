#!/usr/bin/env python

import scapy.all as scap

def scann(ip):
    RequestOf_ARP = scap.ARP(pdst=ip)
    print("*" * 50)
    print(RequestOf_ARP.summary())
    print("*" * 50)
    #scap.ls(scap.ARP())

scann('192.168.217.1/24')
