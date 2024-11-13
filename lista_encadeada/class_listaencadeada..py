
# Implementação Lista com alocação dinâmica (Lista Encadeada)

from no import No
class Lista:
    def __init__(self, tammax):
        self.tammax = tammax
        self.prim = None
        self.nelems = 0
    
    def consulta (self, x):
        p = self.prim
        while (p) and (p.dado != x):
            p = p.prox
        return (p != None)

    def insere (self, x):
        if (self.consulta(x)) or (self.nelems == self.tammax):
            return False
        p = No(x)
        p.prox = self.prim
        self.prim = p
        self.nelems += 1
        return True

     
# Casos: (1. Lista vazia 
# 1.1 Lista tem espaço -> True), 
# (2. Lista não vazia 
# 2.1 x está na lista -> False
# 2.2 x não está na lista -> 2.2.1 Lista tem espaço -> True, 2.2.2 Lista cheia -> False)

