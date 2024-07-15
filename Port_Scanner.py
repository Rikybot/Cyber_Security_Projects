import socket
import sys
import datetime
import errno
hostname = input("Enter a hostname: ")
ip_address = socket.gethostbyname(hostname)
print("Enter the starting and ending number of ports to be scanned:")
s_port = int(input("Enter the starting port: "))
e_port = int(input("Enter the ending port: "))
st = datetime.datetime.now()
try:
    for port in range(s_port, e_port+1):
        print(f'Checking port {port}:')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        conn = sock.connect_ex((ip_address, port))
        if conn == 0:
            print(f'Port {port}: Open')
        else:
            print(f'Port {port}: Closed')
            print("Reason:", errno.errorcode[conn])
            sock.close()

except KeyboardInterrupt:
    print(f'You pressed Ctrl+C')
    sys.exit()
except socket.gaierror:
    print(f'Server name could not be resolved')
    sys.exit()
except socket.error:
    print(f'Could not connect to server')
    sys.exit()
ed = datetime.datetime.now()
t = ed - st
print(f'Time taken is {t} seconds...')
