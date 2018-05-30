# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Grafo Completo  
# Matrícula: 117110492

N = int(input()) # número de vértices do grafo
grafo = {} # declara um Mapa vazio

# para cada vez (de 0 até o número total de vértices), lê-se um vértice, as arestas e associa-se essas arestas ao seu respectivo vértice
for i in range(N):
	vertice = input()
	arestas = input().split()
	grafo[vertice] = arestas

# assume inicialmente como True se é um grafo completo
completo = True

# verifica se é um grafo completo e, se não for, a variável 'completo' assume False
for i in grafo.keys():
	arestasNaoRepetidas = set(grafo[i])
	arestasNaoRepetidas.discard(i)
	if len(arestasNaoRepetidas) != N -1:
		completo = False
		break

print(completo)