# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Vértices Isolados 
# Matrícula: 117110492

N = int(input()) # número de vértices do grafo
grafo = {} # declara um Mapa vazio

# para cada vez (de 0 até o número total de vértices), lê-se um vértice, as arestas e associa-se essas arestas ao seu respectivo vértice
for i in range(N):
    vertice = input()
    arestas = input().split()
    grafo[vertice] = arestas

# verifica se os vértices são isolados e, se sim, os salva em uma lista, inicialmente vazia
resp = []
for i in grafo.keys():
    if grafo[i] == []:
        resp.append(i)
print(resp)