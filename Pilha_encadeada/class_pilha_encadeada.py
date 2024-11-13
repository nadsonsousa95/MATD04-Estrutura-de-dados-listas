# Implementação da estrutura pilha com alocação dinâmica
# Nas pilhas podem haver chaves repetidas
# baseado no princípio de Last In First Out (LIFO), ou seja "o último que entra é o primeiro que sai"

class No:
    def __init__(self, x):
        self.dado = x
        self.prox = None

    def get_dado (self):
        return self.dado

class Pilha:
    def __init__(self, maxtam):
        self.maxtam = maxtam
        self.nelems = 0
        self.topo = None

    def empilha(self, x):
        if self.maxtam == self.nelems:
            return False
        p = No(x)
        p.prox = self.topo
        self.topo = p
        self.nelems += 1
        return True
        
    def desempilha(self):
        if self.nelems == 0:
            return False
        removido = self.topo.dado
        self.topo = self.topo.prox
        self.nelems -= 1
        return True, removido 
    
    def returntop(self):
        return self.topo.dado
    
p = Pilha(7)
p.empilha(3)
p.empilha(4)
print(p.empilha(5)) # Retorna True 
print(p.returntop()) # Retorna 5
print(p.desempilha()) # Retorna True, 5
print(p.returntop()) # Retorna 4
