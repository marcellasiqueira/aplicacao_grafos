# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Fluxo de entrada 
# Matrícula: 117110492

N = int(input()) # número de arestas do grafo

digrafo = {} # declara um Mapa vazio

fluxo = {} # declara um Mapa vazio

# inicializa vértice do dígrafo e percorre as arestas
for i in range(N):
    label = input()
    linha = input().split()
    digrafo[label] = []
    for j in range(0, len(linha),2):
        aresta = {}
        aresta['to'] = linha[j]
        aresta['capacity'] = int(linha[j + 1])
        digrafo[label].append(aresta)

# gera-se o fluxo
for i in range(N):
    label = input()
    linha = input().split()
    fluxo[label] = []
    for j in range(0, len(linha),2):
        aresta = {}
        aresta['to'] = linha[j]
        aresta['flow'] = int(linha[j + 1])
        fluxo[label].append(aresta)

# entrada de corte
corte = input().split()

# somatório dos fluxos
soma = 0

# verifica se o vértice não está no corte e, para cada aresta nos vértices do dígrafo de fluxo, verifica se a aresta está no corte. se sim, soma o valor do fluxo da aresta na variável de soma
for vertice in fluxo.keys():
    if vertice not in corte:
        for aresta in fluxo[vertice]:
            if aresta['to'] in corte:
                soma += aresta['flow']


print(soma)