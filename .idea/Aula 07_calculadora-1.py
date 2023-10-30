# 1. APRENDER A UTLIZACAO DE METODOS E FUNCOES NO PYTHON
# 2. APRENDER A UTILIZAÇÃO DE CLASSES
# 3. ENTENDER OS MOTIVOS PARA SE USAR METODOS, FUNCOES E CLASSES
# - O QUE SAO METODOS E FUNCOES
# - COMO DECLARAR METODOS E FUNCOES
# - VANTAGENS DE SE UTILIZAR METODOS E FUNCOES
# - COMO IMPLEMENTAR CLASS ;
# - VANTAGENS DE SE UTILIZAR CLASSES

#POR CONVENÇÃO:
#NO PYTHON METODO É TUDO QUE NAO RETORNA VALOR
# FUNCAO É TUDO QUE RETORNA VALOR
# NO PYTHON O METODO DE CHAMA DEFINICAO (def)

# def soma(a, b) :
#     return a + b
#
# def subtracao(a, b) :
#     return a - b
#
# def multiplicacao(a, b) :
#     return a * b
#
# def divisao(a, b) :
#     return a / b
#
# print(soma(1, 2))
# print(soma(3,4))
# print(subtracao(5, 2))
# print(subtracao(9, 2))
# print(multiplicacao(5, 4))
# print(multiplicacao(9, 8))
# print(divisao(36, 6))
# print(divisao(10, 5))
########################################################

#CLASSE
class Calculadora:
    def __init__(self, num1, num2): #isntanciar a classe
        self.valor_a = num1
        self.valor_b = num2
    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b
#instansiando uma classe
calculadora = Calculadora(10, 2)
print(calculadora.valor_a)
print(calculadora.valor_b)
print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())

