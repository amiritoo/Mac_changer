#!/usr/bin/env python
import subprocess
import optparse


def mac_changer(interface, new_mac):
    subprocess.call((["ifconfig", interface, "down"]))
    subprocess.call((["ifconfig", interface, "hw", "ether", new_mac]))
    subprocess.call((["ifconfig", interface, "up"]))

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="interface to change MAC")
parser.add_option("-m", "--MAC", dest="new_mac", help="new MAC ")
(optiones, command) = parser.parse_args()

mac_changer(optiones.interface, optiones.new_mac)

