# Implementação da estrutura fila com alocação dinâmica
# Permite chaves repetidas
# Filas FIFO: 'First-in First-out' (Primeiro a chegar, primeiro a sair)

class No:
    def __init__(self, x):
        self.dado = x
        self.prox = None

class Fila:
    def __init__(self):
        self.prim = None

    def enfileira(self, x):
        if self.prim == None:
            self.prim = No(x)
            return True
        
