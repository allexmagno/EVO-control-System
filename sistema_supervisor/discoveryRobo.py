import socket

class Discovery:
    def __init__(self):
        pass

    def encontraIP(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind(('', 62255))

        host = ''
        while host == '':
            host = server.recvfrom(1024)

        return host