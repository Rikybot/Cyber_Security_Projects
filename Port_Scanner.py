import socket  # Import the socket module for network communications
import sys  # Import the sys module for system-specific parameters and functions
import datetime  # Import the datetime module to work with dates and times
import errno  # Import the errno module to handle error codes

# Prompt the user to enter a hostname
hostname = input("Enter a hostname: ")

# Get the IP address corresponding to the hostname
ip_address = socket.gethostbyname(hostname)

# Prompt the user to enter the range of ports to be scanned
print("Enter the starting and ending number of ports to be scanned:")
s_port = int(input("Enter the starting port: "))  # Starting port number
e_port = int(input("Enter the ending port: "))  # Ending port number

# Record the start time of the scan
st = datetime.datetime.now()

try:
    # Loop through the specified range of ports
    for port in range(s_port, e_port+1):
        print(f'Checking port {port}:')  # Inform the user which port is being checked
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Set a timeout of 5 seconds for the socket operations
        sock.settimeout(5)
        # Try to connect to the specified IP address and port
        conn = sock.connect_ex((ip_address, port))
        if conn == 0:
            # If connection is successful, the port is open
            print(f'Port {port}: Open')
        else:
            # If connection fails, the port is closed
            print(f'Port {port}: Closed')
            # Print the reason for the failure
            print("Reason:", errno.errorcode[conn])
        # Close the socket
        sock.close()

except KeyboardInterrupt:
    # Handle the case where the user interrupts the scan with Ctrl+C
    print(f'You pressed Ctrl+C')
    sys.exit()

except socket.gaierror:
    # Handle the case where the hostname could not be resolved to an IP address
    print(f'Server name could not be resolved')
    sys.exit()

except socket.error:
    # Handle the case where the socket could not connect to the server
    print(f'Could not connect to server')
    sys.exit()

# Record the end time of the scan
ed = datetime.datetime.now()

# Calculate and print the total time taken for the scan
t = ed - st
print(f'Time taken is {t} seconds...')
