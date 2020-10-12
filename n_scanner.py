#!/usr/bin/env python

import scapy.all as scap
import argparse


def getIP():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--ip", dest="ip", help="please enter IP you want to saccning IP /IP range")
    option = parser.parse_args()
    return option


def scann(ip):
    RequestOf_ARP = scap.ARP(pdst=ip)
    brodcast = scap.Ether(dst='ff:ff:ff:ff:ff:ff')
    RequestOf_ARP_brodcast = brodcast / RequestOf_ARP
    answer_list = scap.srp(RequestOf_ARP_brodcast, timeout=1, verbose=False)[0]
    clint_list = []

    for el in answer_list:
        clint_Dir = {"ip": el[1].psrc, "mac": el[1].hwsrc}
        clint_list.append(clint_Dir)
    return clint_list

    # print as table


def printList(answer_list):
    print("_" * 50)
    print("IP\t\t\t MAC Address")
    print("-" * 50)
    for elment in answer_list:
        print(elment["ip"] + "\t\t" + elment['mac'])


option = getIP()
scan_resuot = scann(option.ip)
printList(scan_resuot)