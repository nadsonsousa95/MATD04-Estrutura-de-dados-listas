
# Implementação Lista com alocação dinâmica (Lista Encadeada)
# Um conjunto de nós ligados um ao outro, formando uma sequência
# Não permite valores repetidos

from no import No

class Lista:
    def __init__(self, tammax):
        self.tammax = tammax
        self.prim = None
        self.nelems = 0
        
    # insere no início
    def insereinicio (self, x):
        if (self.consulta(x) or self.nelems == self.tammax):
            return False
        p = No(x)
        p.prox = self.prim
        self.prim = p
        self.nelems += 1
        return True
        
    # insere no final
    def inserefinal (self, x):
        if (self.consulta(x) or self.nelems == self.tammax):
            return False
        p = No(x)
        if self.prim == None: # verifica se a lista está vazia
            p.prox = self.prim
            self.prim = p
            self.nelems += 1
            return True
        else:
            a = self.prim
            while a != None: # busca o último elemento da lista
                a = a.prox
            a.prox = p
            p.prox = None
            self.nelems += 1
            return True
        
    def consulta (self, x):
        p = self.prim
        while (p) and (p.dado != x):
            p = p.prox
        return (p != None)

    def remove(self, x):
        if (self.consulta(x) == False): # se x não está na lista retorna False
            return False

        if self.prim.dado == x: # verifica se x é o primeiro nó da lista e remove
            self.prim = self.prim.prox
            self.nelems -= 1
            return True
            
        p = self.prim  
        while p.prox != None: # remove se x em outra posição
            if p.prox.dado == x:
                p.prox = p.prox.prox
                self.nelems -= 1
                return True
            p = p.prox
        
        
l = Lista(7)
l.insereinicio(3)
l.insereinicio(4)
print(l.consulta(4)) # retorna True
print(l.consulta(5)) # retorna False
print(l.remove(4)) # retorna True


        
    
 


