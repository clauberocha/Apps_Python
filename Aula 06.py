#APRENDER SOBRE CONJUNTOS
#APRENDER A MANIPULAR CONJUNTOS
#APLICABILIDADE DE CONJUNTOS
# 1. O QUE É UM CONJUNTO
# 2. MÉTODO DE UNIÃO
# 3. MÉTODO DE INTERSECÇÃO
# 4. MÉTODO DE DIFERENÇA
# 5. MÉTODO DE DIFERENÇA SIMÉTRICA
# REMOÇÃO DE DUPLICIDADE DE LISTAS UTILIZANDO

# [] - TUPLA
# () - LISTA
# {} - CONJUNTO

conjunto = {1, 2, 3, 4}
print('Conjunto: {}'.format(conjunto))

conjunto = {1, 2, 3, 4}
conjunto.add(5) #ADCIONA UM NOVO DADO AO CONJUNTO
print('Adicao de dados no conjunto: {}'.format(conjunto))

conjunto = {1, 2, 3, 4}
conjunto.discard(2) #RETIRA UM DADO DO CONJUNTO
print('Remocao de dados no conjunto: {}'.format(conjunto))

#EXEMPLO 1 - UNIAO DOS CONJUNTOS
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

#EXEMPLO 2 - INTERESERCCAO DOS CONJUNTOS
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_interseccao = conjunto.intersection(conjunto2)
print('Interseccao: {}'.format(conjunto_interseccao))

#EXEMPLO 3 - DIFERENÇAS ENTRE CONJUNTOS
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diterenca entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diterenca entre 2 e 1: {}'.format(conjunto_diferenca2))

#EXEMPLO 4 - DIFERENÇAS SIMETRICA ENTRE CONJUNTOS
conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_diff_simetrica = conjunto.symmetric_difference (conjunto2)
print('Diterenca Simetrica entre 1 e 2: {}'.format(conjunto_diff_simetrica))

#EXEMPLO 5 - CONJUNTO SUBSET (verifica se um conjunto é subconjunto de outro
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é subconjunto de B: {}'.format(conjunto_subset))
conjunto_subset = conjunto_b.issubset(conjunto_a)
print('B é subconjunto de A: {}'.format(conjunto_subset))
conjunto_superset_b = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A: {}'.format(conjunto_superset_b))

#CONVERTER LISTA PARA CONJUNTO
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)

#CONVERTER CONJUNTO EM LISTA
lista_animais = list(conjunto_animais)
print(lista_animais)
