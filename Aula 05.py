# APRENDER SOBRE LISTAS
# APRENDER SOBRE TUPLAS
# APLICABILIDADE DE LISTAS E TUPLAS
# 1. COMO CRIAR UMA LISTA
# 2. MANIPULAR LISTAS
# 3. REALIZAR OPERACOES COM LISTAS
# 4. O QUE E UMA TUPLA
# 5. COMO INTERAGIR COM TUPLAS
# 6. CONVERSOES DE LISTAS E TUPLAS

# CRIAR UMA LISTA DE INTEIROS
# lista = [1, 3, 5, 7]
# lista_animal = ['cahorro', 'gato', 'elefante']
# print(lista)
# print(lista_animal)
# print(lista_animal[1]) #POSICOES: CACHORRO=0, GATO=1, CACHORR0=2
#
# for x in lista_animal:
#     print(x)
#
# for x in lista:
#     print(x)
#
# soma = 0
# for x in lista:
#     soma += x
#     print(soma)
#
# print(sum(lista))
# print(max(lista))
# print(min(lista))
#
# print(max(lista_animal))
# print(min(lista_animal))

#PESQUISANDO UM ANIMAL NA LISTA
# if 'gato' in lista_animal:
#     print('existe um gato na lista')
# else:
#     print('não existe um gato na lista')
#
# if 'lobo' in lista_animal:
#     print('existe um lobo na lista')
# else:
#     print('não existe um lobo na lista. Será incluído.')
#     lista_animal.append('lobo') #'INCLUINDO UM ANIMAL NA LISTA"
#     print(lista_animal)
#     lista_animal.pop() #REMOVE SEMPRE O ULTIMO DA PILHA
#     print(lista_animal)
#     lista_animal.pop(0) #RETIRANDDO O ELEMENTO CACHORRO
#     print(lista_animal)

#lista_animal.remove(gato)
#print(lista_animal)

#ORDENANDO A LISTA - COMANDO SORT
lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
lista.sort()
lista_animal.sort()
print(lista)
print(lista_animal)

#COMANDO REVERSE - REVERTE A POSIÇÃO DA LISTA
lista = [12, 10, 7, 5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
lista.reverse()
lista_animal.reverse()
print(lista)
print(lista_animal)

#TUPLA É IMUTAVEL A LISTA NÃO
tupla = (1, 10, 12, 14)
print(tupla)

#TUPLA COM CONTADOS
tupla = (1, 10, 12, 14)
print(len(tupla))
print(len(lista_animal))

#CONVERTENDO LISTA EM TUPLA
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)

#CONVERTENDO TUPLA EM LISTA
lista = list(tupla)
print(type(lista))
lista[0] = 100
print(lista)
