import socket

class Broadcast:
    def __init__(self):
        pass

    def cast(self, ip):
        porta = 62255
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        client.sendto(ip.encode(), ('255.255.255.255', porta))