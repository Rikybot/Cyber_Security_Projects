import os, socket, threading
import platform


ip = socket.gethostbyname(input("Enter the website you want to check: "))
print(f'IP Address : {ip}')
ip = ip.split('.')
sip = ip[0]+'.'+ip[1]+'.'+ip[2]+'.'

st = int(input("Enter the starting value: "))
ed = int(input("Enter the ending value: ")) + 1

oper = platform.system()
if oper == "Windows":
    ping1 = "ping -n 1 "
elif oper == "Linux":
    ping1 = "ping -c 1 "


def handle(st1, ed1, si):
    for i in range(st1, ed1):
        addr = si + str(i)
        response = os.popen(ping1 + addr)
        for lines in response.readlines():
            if lines.count("TTL"):
                print(f'{addr} -----> Live  ')
                continue


def mythreads(en, st):
    threads = []
    diff = en - st
    k = diff // 10

    for i in range(k):
        et = st + 10
        thread = threading.Thread(target=handle, args=(st, et, sip, ))
        threads.append(thread)
        st = et
    print(threads)

    for thread in threads:
        thread.start()


for thread in threads:
thread.join()


mythreads(ed, st)
