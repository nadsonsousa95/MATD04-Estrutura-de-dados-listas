
class No:
    def __init__(self, x):
        self.dado = x
        self.dir = None
        self.esq = None

class arvore:
    def __init__(self):
        self.raiz = None

    def insere(self, x):
        if self.raiz == None:
            self.raiz = No(x)
            return True
        else:
            self.insere_recursivo(x, self.raiz)

    def insere_recursivo(self, x, no_atual):
        if x < no_atual.dado:
            if no_atual.esq == None:
                no_atual.esq = No(x)
            else:
                self._inserir_recursivo(x, no_atual.esq)
        else:
            if no_atual.dir == None:
                no_atual.dir = No(x)
            else:
                self._inserir_recursivo(x, no_atual.dir)

        

#Busca por um nó com chave k com raiz em x
                
