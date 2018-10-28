import Pyro4

ns = Pyro4.locateNS("192.165.15.110",6896)
print("a")
uri = ns.lookup('obj')
print(uri)


srcom = Pyro4.Proxy(uri)

print(srcom.getPosInicial())

k = input("atualiza coord")

print(srcom.getPosInicial())