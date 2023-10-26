# SE APRONFUDAR MAIS NAS SINTAXES BÁSICAS
# APRENDER A UTILIZAR LAÇOS DE REPETIÇÃO
# CRIAR PROGRAMAS COM CONDICIONAL E LAÇOS DE REPETIÇÃO
# COMANDOS - FOR
# COMANDO - WHILE
# COMANDO - RANGE (PARA GERAR NUMEROS SEQUENCIAIS)

#EX-01 - COMANDO "FOR"
# for x in range(90, 101):
#     print(x)

#EX-02 DESCOBRIR SE O NUMERO É PRIMO OU NAO
#a = int(input('Entre com o número: '))
#div = 0
#for x in range (1, a+1):
#   resto = a % x
#   print(a, resto)
#   if resto == 0:
#       div = div + 1

#if div == 2:
#    print('Número {} é primo'.format(a))
#else:
#    print('número {} não é primo'.format(a))

#EX-03 NUMEROS PRIMOS DE 1  a 100 (FOR DENTRO DE FOR)
""" a = int(input('Entre com um valor: '))
for num in range(a):
    div = 0
    for x in range (1, num+1):
        resto = num % x
        #print(x, resto)
        if resto == 0:
            div += 1
    if div == 2:
        print(num) """

#COMANDO WHILE (LAÇO)
#a = 0
#while a <= 10:
#  print(a)
#  a += 1


#EX-05 - NOTAS BIMESTRAIS II UTILIZANDO WILE
#a = int(input('Primeiro bimestre: '))
#while a > 10:
#     a = int(input('Você digitou errado. Primeiro Bimestre: '))
#b = int(input('Segundo bimestre: '))
#while b > 10:
#     b = int(input('Você digitou errado. Segundo Bimestre: '))
#c = int(input('Terceiro bimestre: '))
#while c > 10:
#     c = int(input('Você digitou errado. Terceiro Bimestre: '))
#d = int(input('Quarto bimestre: '))
#while d > 10:
#     d = int(input('Você digitou errado. Quarto Bimestre: '))
#media = (a + b + c + d) / 4
#print('media: {}'.format(media))

#EX-06
nota = int(input('Entre com a nota: '))
while nota > 10:
    nota = int(input('Nota Inválida. Entre com a nota correta: '))
     