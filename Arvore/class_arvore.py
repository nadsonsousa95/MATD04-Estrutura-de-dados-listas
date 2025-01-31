
class No:
    def __init__(self, x):
        self.dado = x
        self.dir = None
        self.esq = None
        self.pai = None

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
        else: return True      
        

    def inserir(self, valor):
        if (self.buscaIterativa(valor) == True):
            return False
        y = None
        no = No(valor)
        x = self.raiz
        while (x != None):
            y = x
            if no.dado < x.dado:
                x = x.esq
            else: x = x.dir
        no.pai = y
        if y == None:
            self.raiz = no   #arvore vazia
        elif no.dado < y.dado:
            y.esq = no
        else:
            y.dir = no

    def MenorValor(self, no):
        if no != None:
            while (no.esq != None):
                no = no.esq
            return no.dado
    
    #Retorna maior valor de chave
    def MaiorValor(self, no):
        if no != None:
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

    def sucessor(self, no):
        if no.dir != None:
            return self.MenorValor(no.dir)       
        y = no.pai
        while y != None and no == y.dir:
            no = y
            y = y.pai
        return y


a = Arvorebinaria()
a.inserir(80)
a.inserir(50)
a.inserir(30)
a.inserir(100)
a.inserir(10)
a.inserir(20)
print(a.buscaIterativa(100)) #Retorna (True, 100)
print(a.buscaIterativa(40)) #Retorna False
print(a.MenorValor(a.raiz)) #Retorna 10
print(a.MaiorValor(a.raiz)) #Retorna 100
print(' ')
a.percursoemOrdem(a.raiz)
print(' ')
a.percursoPreOrdem(a.raiz)                
print(' ')
a.percursoPosOrdem(a.raiz)
print(' ')
print(a.sucessor(a.raiz))