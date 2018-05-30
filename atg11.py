# coding: utf-8
# Marcella Medeiros Siqueira Coutinho de Almeida
# [ATG] Fluxo Válido 
# Matrícula: 117110492

N = int(input()) # número de arestas do grafo

digrafo = {} # declara um Mapa vazio

fluxo = {} # declara um Mapa vazio

# inicializa o vértice no dígrafo, percorre o tamanho da entrada e adiciona a aresta no dígrafo
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
        
# inicializa a resposta como sendo verdadeira
resposta = True

#inicializa o corte de cada vértice
corteCadaVertice = {}

source = input()
sink = input()

# verifica se é um fluxo válido ou não
for i in digrafo.keys(): corteCadaVertice[i] = [0, 0]

for vertice in fluxo.keys():
    for aresta in fluxo[vertice]:
        corteCadaVertice[vertice][0] += aresta['flow']
        corteCadaVertice[aresta['to']][1] += aresta['flow']

aux = 0

for i in corteCadaVertice.keys():
    if corteCadaVertice[i][0] == corteCadaVertice[i][1] or (i == source or i == sink):
        aux += 1
if aux == len(corteCadaVertice):
    print (True)
else:
    print (False)