
class No:
    def __init__(self, x):
        self.dado = x
        self.prox = None
        self.ant = None

class Lista:
    def __init__(self, tammax):
        self.prim = None
        self.ult = None
        self.nelems = 0
        self.tammax = tammax

    def listacheia(self):
        if self.tammax == self.nelems:
            return True
        return False

    def consulta(self, x):
        if self.nelems == 0:
            return False
        p = self.prim
        while(p) and (p.dado != x):
            p = p.prox
        if p == None:
            return False
        else:
            return p
    
    def insere(self, x):
        if (self.listacheia()) or (self.consulta(x) != False):
            return False
        p = No(x)
        if self.nelems == 0:
            self.prim = p
            self.ult = p
            self.nelems += 1 
            return True
        else:
            p.ant = self.ult
            self.ult.prox = p
            self.ult = p
            self.nelems += 1 
            return True

    def remove(self, x):
        p = self.consulta(x)
        if p == None:
            return False
        if (p.ant):
            p.ant.prox = p.prox
        else:
            self.prim = p.prox
        if (p.prox):
            p.prox.ant = p.ant
        self.nelems -= 1
        return True


li = Lista(10)
print(li.insere(4))
print(li.insere(5))
print(li.insere(9))
print(li.consulta(9))
print(li.remove(4))
print(li.remove(5))
print(li.prim.dado)
print(li.ult.dado)