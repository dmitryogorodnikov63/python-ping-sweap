import argparse
import common
import ip_sweap as ips
import http_request as hr

parser = argparse.ArgumentParser(description='Ping sweap')
parser.add_argument('task', choices=['scan', 'sendhttp'], help='Network scan or send HTTP request')
parser.add_argument('-t', '--target', help='Target for request')
parser.add_argument('-m', '--method', help='Request method', default='GET')
parser.add_argument('-hr', nargs='+', type=common.pair, help='Request header for example: -hr key:value key2:value2')
parser.add_argument('-b', '--body', type=str, help='Body for request')
parser.add_argument('-i', '--ip', type=str, help='Ip addresses')
parser.add_argument('-v', action='store_true', help='Verbose output')
args = parser.parse_args()

if args.task == 'scan':
    if args.ip:
        ips.ip_sweap(args.ip, args.v)
    else:
        print("Необходимо указать параметр -i or -ip")
else:
    headers = None
    if args.hr:
        headers = {k: v for d in args.hr for k, v in d.items()}
    hr.send_request(args.target, args.method, headers=headers, body=args.body)

