from dados import *

list = []
dados = Dados("00", list)

print(dados.coordenadas.toString())
dados.coordenadas.atualizarDireita()
print(dados.coordenadas.toString())