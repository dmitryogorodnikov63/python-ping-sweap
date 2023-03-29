import argparse

import ip_sweap as ips

parser = argparse.ArgumentParser(description='Ping sweap')
parser.add_argument('-i', '--ip', required=True, type=str, help='Ip addresses')
parser.add_argument('-v', action='store_true', help='Verbose output')
args = parser.parse_args()

ips.ip_sweap(args.ip, args.v)