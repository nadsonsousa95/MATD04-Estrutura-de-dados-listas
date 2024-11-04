# Exercício de Implementação de Classes em Python

class Circulo:
    def __init__(self,raio):
        self.raio = raio
        
    def calcPerimetro(self):
        print(self.raio*2*3.14)
        
    def calcArea(self):
        print(3.14*self.raio*self.raio)
        
circulo = Circulo(6)

class ContaBancaria:
    def __init__(self,conta,titular,saldo=0):
        self.conta = conta
        self.titular = titular 
        self.saldo = saldo
        
    def deposito(self,valor):
        if valor > 0:
            self.saldo += valor
            print(f"O titular {self.titular} depositou o  valor: {valor} reais na conta {self.conta}, e seu saldo agora é de {self.saldo} reais.")
            
    def sacar(self,valor):
        if valor > 0:
            self.saldo -= valor
            print(f"O titular {self.titular} sacou o valor: {valor} reais na conta {self.conta}, e seu saldo agora é de: {self.saldo} reais.")

bradesco = ContaBancaria(234500, "Cezar Augusto")

class Paciente:
    def __init__(self, nome, idade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.email = email

paciente = Paciente("joao", 23, 23456778, "nadson@gnail")

