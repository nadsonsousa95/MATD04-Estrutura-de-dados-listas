
class No:
    def __init__(self, x):
        self.dado = x
        self.dir = None
        self.esq = None
        self.pai = None

class Arvorebinaria:
    def __init__(self):
        self.raiz = None

    #Se o valor de x for encontrado, retorna o nó que aponta para x
    def buscaIterativa(self, x):
        r = self.raiz
        while (r != None) and (r.dado != x):
            if x < r.dado:
                r = r.esq
            else:
                r = r.dir
        if r == None: 
            return False
        else: return r     
        

    def inserir(self, valor):
        if (self.buscaIterativa(valor) != False):
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
    
    # Substitui a subarvore com raiz no nó u pela subarvore com raiz no no v
    def transplante(self, u, v):
        if u.pai == None:
            self.raiz = v
        elif u == u.pai.esq:
            u.pai.esq = v
        else:
            u.pai.dir = v
        if v != None:
            v.pai = u.pai


    def remover(self, valor):
        if (self.buscaIterativa(valor) != False):
            no = self.buscaIterativa(valor)
            if no.esq == None:
                self.transplante(no, no.dir)
            elif no.dir == None:
                self.transplante(no, no.esq)
            else:
                y = self.MenorValor(no.dir)
                if y.pai != no:
                    self.transplante(y, y.dir)
                    y.dir = no.dir
                    y.pai.dir = y
                self.transplante(no, y)
                y.esq = no.esq
                y.pai.esq = y


    #Retorna no com maior valor de chave a partir de um nó
    def MenorValor(self, no):
        if no != None:
            while (no.esq != None):
                no = no.esq
            return no
    
    #Retorna no com maior valor de chave a partir de um nó
    def MaiorValor(self, no):
        if no != None:
            while (no.dir != None):
                no = no.dir
            return no
        
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

    # O sucessor de um nó x é um nó com menor chave maior que a chave de x
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
a.inserir(35)
a.remover(35)
print(a.buscaIterativa(100).dado) #Retorna (100)
print(a.buscaIterativa(40)) #Retorna False
print(a.MenorValor(a.raiz).dado) #Retorna 10
print(a.MaiorValor(a.raiz).dado) #Retorna 100
print(' ')
a.percursoemOrdem(a.raiz)
print(' ')
a.percursoPreOrdem(a.raiz)                
print(' ')
a.percursoPosOrdem(a.raiz)
print(' ')
print(a.sucessor(a.raiz).dado)