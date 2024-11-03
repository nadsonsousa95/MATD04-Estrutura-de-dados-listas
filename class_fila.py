
# Filas FIFO: 'First-in First-out' (Primeiro a chegar, primeiro a sair)
# Permite chaves repetidas
# Remove sempre no início, insere sempre no final

class Fila:
    def __init__(self, maxelems):
        self.dados = maxelems * [0]
        self.prim = 0
        self.nelems = 0

    def enfileira(self, x):
        if self.nelems == len(self.dados):
            return False, -1
        # recebe a ultima posição vazia
        pos = (self.prim + self.nelems) % len(self.dados)
        self.dados[pos] = x
        self.nelems += 1
        return True, x
    
    def desenfileira(self):
        if self.nelems == 0:
            return -1
        x = self.dados[self.prim]
        self.nelems -= 1
        self.prim = (self.prim + 1) % len(self.dados)
        return x

fila = Fila(8)
fila.enfileira(3)
fila.enfileira(8)
fila.enfileira(20)
fila.enfileira(12)
fila.desenfileira()
print(fila.desenfileira())


