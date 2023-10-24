#Objetivo
    #1. SE APROFUNDAR NAS SINTAXES BASICAS
    #2. APRENDER A UTILIZAR CONDICIONAIS
        #2.1 - CONDICIONAL - COMANDO IF
        #2.2 - CONDICIONAL - COMANDO ELSE
        #2.3 - CONDICIONAL - COMANDO ELIF
    #3. APERNDER A UTLIZAR OPERADORES LÓGICOS
        #3.1 - OPERADORES LÓGICOS (AND - OR - NOT)

# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print( 'O maior múnero é {}'.format (a))
# elif b >a and b >c:
#     print('O maior número é {}' .format(b))
# else:
#     print('O maior numero é {}' .format(c))
# print ('Final do programa')

# EX-02. PESQUISANDO SE UM NUMERO DIGITADO É PAR
# a = int(input('Entre com um valor: '))
# resto = a % 2
# if resto == 0:
#     print('Número é par')
# else:
#     print('Número é impar')

#EX-03.
# a = int(input('Entre com o primeiro valor: '))
# b = int(input('Entre com o segundo valor: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or not resto_b > 0:
#     print('Foi digitado um Número é par')
# else:
#     print('Nenhum Número par foi digitado')

# #EX-04 - NOTAS BIMESTRAIS
# a = int(input('Primeiro bimestre: '))
# b = int(input('Segundo bimestre: '))
# c = int(input('Terceiro bimestre: '))
# d = int(input('Quarto bimestre: '))
# media = (a + b + c + d) / 4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10:
#     print('media: {}'.format(media))
# else:
#     print('Foi informada alguma nota errada')

#EX-05 - NOTAS BIMESTRAIS II
a = int(input('Primeiro bimestre: '))
if a > 10:
     a = int(input('Você digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo bimestre: '))
if b > 10:
     b = int(input('Você digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro bimestre: '))
if c > 10:
     c = int(input('Você digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto bimestre: '))
if d > 10:
     d = int(input('Você digitou errado. Quarto Bimestre'))
media = (a + b + c + d) / 4
print('media: {}'.format(media))