import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(b'\x01\x02\x03\x04', ('172.20.10.2', 12345))
