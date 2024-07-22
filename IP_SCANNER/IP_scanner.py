import os  # To execute system commands
import socket  # To get the IP address from the hostname
import threading  # To create threads for concurrent execution
import platform  # To check the operating system

# Get the IP address of the website entered by the user
ip = socket.gethostbyname(input("Enter the website you want to check: "))
print(f'IP Address : {ip}')

# Split the IP address into its components
ip = ip.split('.')
sip = ip[0] + '.' + ip[1] + '.' + ip[2] + '.'  # Reconstruct the subnet part of the IP address

# Get the starting and ending range for IP addresses to scan
st = int(input("Enter the starting value: "))
ed = int(input("Enter the ending value: ")) + 1

# Determine the operating system and set the appropriate ping command
oper = platform.system()
if oper == "Windows":
    ping1 = "ping -n 1 "
elif oper == "Linux":
    ping1 = "ping -c 1 "

# Function to handle the pinging of IP addresses in the given range
def handle(st1, ed1, si):
    for i in range(st1, ed1):
        addr = si + str(i)  # Construct the IP address to ping
        response = os.popen(ping1 + addr)  # Execute the ping command
        for lines in response.readlines():
            if "TTL" in lines:  # Check if the response contains "TTL", indicating a live host
                print(f'{addr} -----> Live  ')

# Function to create and start threads for concurrent scanning
def mythreads(en, st):
    threads = []
    diff = en - st  # Calculate the range of IPs to scan
    k = diff // 10  # Divide the range into chunks of 10 for each thread

    for i in range(k):
        et = st + 10  # Determine the end of the current chunk
        thread = threading.Thread(target=handle, args=(st, et, sip))  # Create a new thread
        threads.append(thread)  # Add the thread to the list
        st = et  # Update the starting point for the next chunk

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Start the thread creation and scanning process
mythreads(ed, st)
