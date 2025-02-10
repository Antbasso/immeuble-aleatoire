import turtle as t
from Etage import *
from Toit import *
from random import randint 


COULEURS = ["grey","red","orange","green","blue",
            "navy","yellow","gold","tan","brown",
            "sienna","wheat","cyan","pink","salmon",
            "violet","purple"]



class Immeuble:
    def __init__(self):
        self.nom = " Immeuble"
        self.r= randint(0, 4)
        index_choisi_I = randint(0, len(COULEURS)-1)
        self.co = COULEURS[index_choisi_I]
        
    def dessiner(self):
       
        r=Rdc()
        r.dessiner(self.co)
        e=Etage()
        for i in range(self.r):
            e.dessiner(self.co)
        w=Who()
        t.color("black", self.co )
        t.begin_fill()
        w.random_t()
        t.end_fill()
        t.fd(60*(self.r + 1))
        t.lt(90)
         