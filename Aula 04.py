# SE APRONFUDAR MAIS NAS SINTAXES BÁSICAS
# APRENDER A UTILIZAR LAÇOS DE REPETIÇÃO
# CRIAR PROGRAMAS COM CONDICIONAL E LAÇOS DE REPETIÇÃO
# COMANDOS - FOR
# COMANDO - WHILE
# COMANDO - RANGE (PARA GERAR NUMEROS SEQUENCIAIS

#EX-01 - COMANDO "FOR"
# for x in range(90, 101):
#     print(x)

#EX-02 DESCOBRIR SE O NUMERO É PRIMO OU NAO
a = int(input('Entre com o número: '))
div = 0
for x in range (1, a+1):
    resto = a % x
    print(a, resto)
    if resto == 0:
        div = div + 1

if div == 2:
    print('Número {} é primo'.format(a))
else:
    print('número {} não é primo'.format(a))
