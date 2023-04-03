import os
import ipaddress
import platform
import re

ip_regular = '^([01]?\d\d?|2[0-4]\d|25[0-5])(?:\.[01]?\d\d?|\.2[0-4]\d|\.25[0-5]){3}(?:/[0-2]\d|/3[0-2])?$'


def ip_sweap(address, v):
    ips = parse_addreses(address, v)
    print("Starting ..")
    for ip in ips:
        ping(ip, v)
    print("Complete")


def parse_addreses(address, v):
    if re.search(ip_regular, address):
        ipAddr = ipaddress.IPv4Network(address, False)
        return ipAddr.hosts()
    else:
        print("Error: Enter valid ip for example: 127.0.0.1/24")


def ping(ip, v):
    if v:
        print("Check " + str(ip))
    if platform.system() == "Windows":
        ping = 'ping -n 1 -w 1  ' + str(ip)
    else:
        ping = 'ping -c 1 -t 1  ' + str(ip)
    response = os.popen(ping)
    list = response.readlines()
    for line in list:
        if (line.count("ttl") or line.count("TTL")):
            print(str(ip) + " is UP")
            break
    if v:
        print(str(ip) + " is DOWN")