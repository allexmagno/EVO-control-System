from sistema_robo.dados import *
from sistema_robo.com import *

lista = []
dados = Dados('(0,0)', lista)
print(dados.getCoordenadas().toString())
comunicacao = Com(dados)
print(comunicacao.getURI())
comunicacao.start()
x = int(input("x"))
y = int(input("y"))
dados.setCoordenadas(x, y)