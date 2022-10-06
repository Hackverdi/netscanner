import scapy.all as scapy
import optparse
def get_user_input():
    parsers=optparse.OptionParser()
    parsers.add_option("-i","--ipaddress", dest="ip_address",help="Enter IP Address")
    user_input=parsers.parse_args()[0]
    if not user_input.ip_address:
        print("Enter IP Address")
    return user_input
def scan_my_network(ip):
    #1) arp_request
    arp_request_packet = scapy.ARP(pdst = ip)
    #scapy.ls(scapy.ARP())
    #2) broadcast
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast/arp_request_packet
    #3) response
    (answer,unanswer) = scapy.srp(combined_packet,timeout=1)
    answer.summary()
user_ip_address =get_user_input()
scan_my_network(user_ip_address.ip_address)

