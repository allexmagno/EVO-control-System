import Pyro4

srcom = Pyro4.Proxy("PYRO:obj_e3b3398ebbee403090ce1981bc83aecd@localhost:37439")

print(srcom.getPosInicial())

k = input("atualiza coord")

print(srcom.getPosInicial())