
class No:
    def __init__(self, x):
        self.dado = x
        self.dir = None
        self.esq = None

class Arvorebinaria:
    def __init__(self):
        self.raiz = None

    def buscaIterativa(self, x):
        r = self.raiz
        while (r != None) and (r.dado != x):
            if x < r.dado:
                r = r.esq
            else:
                r = r.dir
        if r == None: 
            return False
        else: return True, x        
        

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
                self.insere_recursivo(x, no_atual.esq)
        else:
            if no_atual.dir == None:
                no_atual.dir = No(x)
            else:
                self.insere_recursivo(x, no_atual.dir)

    def retornaMenor(self):
        no = self.raiz
        while (no.esq != None):
            no = no.esq
        return no.dado

        
a = Arvorebinaria()
a.insere(80)
a.insere(50)
a.insere(30)
a.insere(100)
a.insere(10)
a.insere(20)
print(a.buscaIterativa(100)) #Retorna (True, 100)
print(a.buscaIterativa(40)) #Retorna False
print(a.retornaMenor())
                
