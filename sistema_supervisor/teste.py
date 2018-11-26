import socket
import threading
import time
import Pyro4

@Pyro4.expose
class SRcom:

    def __init__(self):
        pass

    def setMover(self, direcao):
        if direcao == 'validar':
            print("solicita validar caça")

        else:
            print("movimentando para " + direcao)


client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(('', 4875))

s = SRcom
deamon = Pyro4.Daemon('localhost', port=64000)
uri = deamon.register(s)

p = threading.Thread(target=deamon.requestLoop)
p.start()

def receber():
    while True:
        recv = client.recvfrom(1024)
        msg = recv[0].decode()
        print(msg)
        if msg == 'manual':
            ur = 'uri|'+str(uri)
            client.sendto(ur.encode(), recv[1])

a = threading.Thread(target=receber)
a.start()



while True:

    a = input("=> ")
    client.sendto(a.encode(), ('localhost', 65000))


'''
a_s = threading.Lock()

b_s = threading.Lock()

a = 0


def a1():
    global a
    i = 10

    while i > 0:
        #with a_s:
        a_s.acquire()
        a = a + 1
        print("a", a)
        a_s.release()
        time.sleep(2)

        i -= 1


def b1():
    global a
    i = 10

    while i > 0:
        #with a_s:
        a_s.acquire()
        a = a + 3
        print("b", a)

        i -= 1
        a_s.release()
        time.sleep(1)


t1 = threading.Thread(target=a1).start()
a = input("a: ")

t2 = threading.Thread(target=b1).start()


a = [{'x': 3, 'y': 3}, {'x': 334, 'y': 3}, {'x': 3, 'y': 6}, {'x': 3, 'y': 5}]
while len(a) > 0:
    c = int(input("c: "))
    b = int(input("b: "))
    caca = {'x': c, 'y': b}
    for i in range(len(a)):
        print('for')
        if a[i]['x'] == caca['x'] and a[i]['y'] == caca['y']:
            print(a[i])
            del a[i]
            break
            
'''