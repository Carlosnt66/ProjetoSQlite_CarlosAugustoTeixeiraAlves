#!/usr/bin/env python
# -*- coding: latin1 -*-

#Retornar lista com tuplas dos valores m�ltiplos e quantidade de repeti��o de
#uma dada lista.

def geraListaValoresMultiplos(lista):
    aux = []
    aux = lista
    saida = []
    #Ordenar a lista
    aux.sort()
    print(aux)
    #Verificar repeti��es
    item = aux[0]
    conta = 0
    for i in aux:
        if i == item:
           conta += 1
        else:
            saida.append((item,conta))
            conta = 1
            item = i

    #para o �ltimo item
    saida.append((item,conta))

    return saida

vet = [1,2,1,3,2,1,3,1,2]
print(geraListaValoresMultiplos(vet))
vet = ['Carlos','Augusto','Carlos','Cristina','Raquel','Augusto']
print(geraListaValoresMultiplos(vet))
