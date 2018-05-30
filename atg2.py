# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Grau de um Vértice 
# Matrícula: 117110492

N = int(input()) # número de vértices do grafo
grafo = {} # declara um Mapa vazio

# para cada vez (de 0 até o número total de vértices), lê-se um vértice, as arestas e associa-se essas arestas ao seu respectivo vértice
for i in range(N):
    vertice = input()
    arestas = input().split()
    grafo[vertice] = arestas
    
# recebe o vértice escolhido 
vEscolhido = input()

# imprime o grau do vértice escolhido
print(len(grafo[vEscolhido]) +  grafo[vEscolhido].count(vEscolhido))