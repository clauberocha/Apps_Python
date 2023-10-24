a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor:'))
#a = 10
#b = 5
soma= a + b
subtracao= a - b
multiplicacao= a * b
divisao= a / b
resto = a % b
#print(soma)
#print(subtracao)
#print(multiplicacao)
#print(divisao)
#print(type(soma))
#soma = str(soma)
#print(type(soma))
#print('soma: ' + soma)
#print('soma:' + str(soma))
#print('subtracao:' + str(subtracao))
#print('multiplicacao:' + str(multiplicacao))
#print('divisao:' + str(divisao))
#print(type(divisao))
#print(int(divisao))
#print(resto)
resultado = ('Soma: {soma}. \nSubtracao: {subtracao}. '
      '\nMutiplicacao:{multiplicacao}'
      '\nDivissao: {divisao}' 
      '\nResto: {resto}'.format(soma=soma,
                                subtracao=subtracao,
                                multiplicacao=multiplicacao,
                                divisao=divisao,
                                resto=resto))
print(type(a))
print(resultado)