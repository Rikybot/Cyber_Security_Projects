import socket, struct

'''s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))
s.bind(("eth0", socket.ntohs(0x0800)))
'''
sor = '\x00\x0c\x29\x4f\x8e\x35'
des = '\x00\x0C\x29x2E\x84\x7A'
code = '\x08\x00'
eth = des+sor+code
print(struct.pack('hhl', 1 ,2, 3).decode('utf-8'))
#s.send(eth)
