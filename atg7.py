# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Identifique o conceito 2 
# Matrícula: 117110492

N = int(input()) # número de vértices do grafo
grafo = {} # declara um Mapa vazio
qtdArestas = 0 # inicializa a quantidade de arestas em 0

# além de somar o total de arestas, para cada vez (de 0 até o número total de vértices), lê-se um vértice, as arestas e associa-se essas arestas ao seu respectivo vértice
for i in range(N):
    vertice = input()
    arestas = input().split()
    qtdArestas += len(arestas)
    grafo[vertice] = arestas

qtdArestas /= 2
passeio = input().split()
trilha = True # a trilha de Euler se inicia como verdadeira
visitados = [] # uma lista inicialmente vazia para representar as arestas que já foram visitadas

# verifica se é uma trilha de Euler ou não
if len(passeio) == qtdArestas:
    visitados.append(passeio[0])
    visitados.append(passeio[0][::-1])
    for i in range (len(passeio) - 1):
            if passeio[i + 1][0] != passeio[i][1]:
                trilha = True
            if passeio[i + 1] in visitados:
                trilha = False
            else:
                visitados.append(passeio[i + 1])
                visitados.append(passeio[i + 1][::-1])
else:
	trilha = False
	
	
print(trilha)