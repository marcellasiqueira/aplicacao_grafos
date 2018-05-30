# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Identifique o conceito 1 
# Matrícula: 117110492

N = int(input()) # número de vértices do grafo
grafo = {} # declara um Mapa vazio

# para cada vez (de 0 até o número total de vértices), lê-se um vértice, as arestas e associa-se essas arestas ao seu respectivo vértice
for i in range(N):
    vertice = input()
    arestas = input().split()
    grafo[vertice] = arestas

passeio = input().split() # recebe o passeio válido
trilha = True # inicializa-se a trilha como sendo verdadeira

# verifica-se se é uma trilha válida ou não
if len(passeio) != 0:
    visitados = []

    visitados.append(passeio[0])
    visitados.append(passeio[0][::-1])
    for i in range (len(passeio) - 1):
            if passeio[i + 1][0] != passeio[i][1]:
                trilha = False
            if passeio[i + 1] in visitados:
                trilha = False
            else:
                visitados.append(passeio[i + 1])
                visitados.append(passeio[i + 1][::-1])

print(trilha)