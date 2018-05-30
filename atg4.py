# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Subgrafo
# Matrícula: 117110492

NG = int(input()) # número de vértices do grafo G
grafo = {} # declara um Mapa vazio 

# para cada vez (de 0 até o número total de vértices do grafo G), lê-se um vértice, as arestas e associa-se essas arestas ao seu respectivo vértice
for i in range(NG):
	verticeG = input()
	arestasG = input().split()
	grafo[verticeG] = arestasG

NS = int(input()) # número de vértices do grafo S

subgrafo = True # assume inicialmente como True se o grafo S é um subgrafo de G

# verifica, inicialmente, se os vértices de S estão em G e, se sim, passa a verificar se as arestas também estão. Caso elas não estejam ou, caso os vértices não estejam, a variável 'subgrafo' passa a ser False
for i in range(NS):
	verticeS = input()
	if verticeS in grafo:
		arestasS = input().split()
		for i in arestasS:
			if i not in grafo[verticeS]: subgrafo = False
	else:
		subgrafo = False
		
print(subgrafo)