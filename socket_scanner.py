import socket
from socket import gethostbyname
import argparse
import subprocess
import sys
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument("-s", "--start", type=int, help="Starting Port Number")
parser.add_argument("-e", "--end", type=int, help="Ending Port Number")
parser.add_argument("-p", "--port", nargs="+", help="Port To Scan")
args = parser.parse_args()

target = input('Enter the host to be scanned: ')
print(target)
t_IP = gethostbyname(target)
print ("Starting scan on host %s..." % (t_IP))

if args.start:
    for i in range(args.start, args.end+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((t_IP, i))
        if result == 0:
            print("Success, port %s is open." % (i,))
        else:
            print("./shrug, port %s must be closed." % (i,))
            sock.close()

if args.port:
    for p in args.port:
        split_ports = p.split(',')
        port_array = np.array(split_ports)
        port_array = port_array.astype(np.int)
        for a in port_array:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((t_IP, a))
                #print("This is result", result)
            if result == 0:
                print("Success, port ", a, "is open")
            else:
                print("./shrug, port ", a, "must be closed")
                sock.close()
