
# Implementação da classe Pilha em python (MATD04 Estrutura de Dados)
# Nas pilhas podem haver chaves repetidas
# baseado no princípio de Last In First Out (LIFO), ou seja "o último que entra é o primeiro que sai"

class Pilha:
    def __init__(self, maxelemens):
        self.dados = maxelemens * [0]
        self.nelems = 0

    #push
    def empilha(self, x):
        if self.nelems < len(self.dados):
            self.dados[self.nelems] = x
            self.nelems += 1
            return True
        return False

    #pop
    def desempilha(self):
        if self.nelems > 0:
            self.nelems -= 1
            return True, self.dados[self.nelems]
        return False, -1

