#!/usr/bin/env python

import scapy.all as scap

def scann(ip):
    # creat arp to request all hosts {**************************************************
    #                                 ARP who has Net('192.168.217.1/24') says 192.168.217.154
    #                                 **************************************************}

    RequestOf_ARP = scap.ARP(pdst=ip)
    print("*" * 50)
    print(RequestOf_ARP.summary())
    print("*" * 50)
    #scap.ls(scap.ARP()) #  this for lis options your intrested

scann('192.168.217.1/24')
