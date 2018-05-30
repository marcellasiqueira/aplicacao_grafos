# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Corte
# Matrícula: 117110492

N = int(input()) # número de vértices do grafo
grafo = {} # declara um mapa vazio

# para cada vez (de 0 até o número total de vértices), lê-se um vértice, as arestas e associa-se essas arestas ao seu respectivo vértice
for i in range(N):
	vertice = input()
	arestas = input().split()
	grafo[vertice] = arestas

conjunto = input().split() # recebe um conjunto de vértices

resp = [] # lista para armazenar o corte das arestas resultantes

# verifica se as arestas estão ou não no conjunto para que sejam adicionadas à lista do corte das arestas resultantes
for i in grafo.keys():
	if i in conjunto:
		for j in grafo[i]:
				if j not in conjunto: resp.append(i + j)
	else:
		for j in grafo[i]:
			if j in conjunto: resp.append(i + j)	

# imprime cada corte por linha                
for i in resp:
	print(i)	