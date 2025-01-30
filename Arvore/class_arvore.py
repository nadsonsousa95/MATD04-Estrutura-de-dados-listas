
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


    #Retorna menor valor de chave
    def MenorValor(self):
        no = self.raiz
        while (no.esq != None):
            no = no.esq
        return no.dado
    
    #Retorna maior valor de chave
    def MaiorValor(self):
        no = self.raiz
        while (no.dir != None):
            no = no.dir
        return no.dado
        
    def percursoemOrdem(self, no):
        if no != None:
            self.percursoemOrdem(no.esq)
            print(no.dado)
            self.percursoemOrdem(no.dir)

    def percursoPosOrdem(self, no):
        if no != None:
            self.percursoPosOrdem(no.esq)
            self.percursoPosOrdem(no.dir)
            print(no.dado)

    def percursoPreOrdem(self, no):
        if no != None:
            print(no.dado)
            self.percursoPreOrdem(no.esq)
            self.percursoPreOrdem(no.dir)
            

a = Arvorebinaria()
a.insere(80)
a.insere(50)
a.insere(30)
a.insere(100)
a.insere(10)
a.insere(20)
a.insere(15)
print(a.buscaIterativa(100)) #Retorna (True, 100)
print(a.buscaIterativa(40)) #Retorna False
print(a.MenorValor()) #Retorna 10
print(a.MaiorValor()) #Retorna 100
print(' ')
a.percursoemOrdem(a.raiz)
print(' ')
a.percursoPreOrdem(a.raiz)                
print(' ')
a.percursoPosOrdem(a.raiz)