# Implementação de estrutura de Lista (MATD04)
# Possui determinado número máximo de elementos
# Chaves são apenas valores inteiros, e não permite elementos com chaves iguais 

class Lista:
    def __init__(self, tammax):
        self.dados = [0] * tammax
        self.nelemens = 0

    def consulta(self, x):
        for i in range(self.nelemens):
            if x == self.dados[i]:
                return True
        return False

    def insere(self, x):
        if self.nelemens < len(self.dados) and self.consulta(x) == False:
            self.dados[self.nelemens] = x
            self.nelemens += 1
            return True
        return False
    
    def posicao(self, x):
        for i in range(self.nelemens):
            if self.dados[i] == x:
                return i
        return -1

    def remove(self, x):
        pos = self.posicao(x)
        if pos == -1:
            return False
        self.dados[pos] = self.dados[self.nelemens-1]
        self.nelemens -= 1
        return True
    
    # Se a lista não estiver vazia, retorna True e o maior valor de chave armazenado na lista. Se estiver vazia, retorna False, -1
    def retornaMaior(self):
        if self.nelemens == 0:
            return False, -1
        maior = self.dados[0]
        for i in range(1, self.nelems):
            if self.dados[i] > maior:
                maior = self.dados[i]
        return True, maior
    
    # Retira o i-ésimo elemento da lista, se houver.
    def retiraIesimo(self, i):
        if i < self.nelemens:
            self.dados[i] = self.dados[self.nelemens - 1]
            self.nelemens -= 1

    # Retorna a quantidade de números menores que x
    def qtdmenores(self, x):
        cont = 0
        for i in range(self.nelemens):
            if self.dados[i] < x:
                cont += 1
        return cont
    
    #Retorne o menor elemento da lista
    def retornamenor(self):
        if self.nelemens == 0:
            return False, -1
        maior = self.dados[0]
        for i in range(self.nelemens):
            if self.dados[i] > self.dados[0]:
                maior = self.dados[i]
        return True, maior


    def imprimir(self):
        print(self.dados[:self.nelemens])


lista = Lista(8)
print(lista.consulta(5)) #Retorna 'False'
lista.insere(3)
lista.insere(4)
lista.insere(5)
lista.insere(9)
print(lista.consulta(5)) #Retorna 'True'
print(lista.remove(9)) #Retorna 'True'
print(lista.menores(5)) #Retorna 2
print(lista.dados) 
lista.imprimir()