# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Identifique o conceito 3 
# Matrícula: 117110492

N = int(input()) # número de vértices do grafo
grafo = {} # declara um Mapa vazio

# para cada vez (de 0 até o número total de vértices), lê-se um vértice, as arestas e associa-se essas arestas ao seu respectivo vértice
for i in range(N):
    vertice = input()
    arestas = input().split()
    grafo[vertice] = arestas

passeio = input().split()
esp = False
resp = "" # string inicialmente vazia para representar as arestas que não foram passadas

# verifica o caso de ter se passado pelas arestas ou não
for i in grafo.keys():
    for j in grafo[i]:
        if ((i + j) not in passeio) and ((j + i) not in passeio):
            if esp: resp += " "
            else: esp = True
            resp += (i + j)

print (resp)