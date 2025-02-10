import turtle as t
from random import randint

class Toit1:
    "Création d'une Class qui dessine un toit plat"
    
    
    def __init__(self):
        self.nom = "toit n°1"
        
    def dessiner(self):
        t.pensize(5)
        t.bk(2.5)
        t.fd(150)
        t.bk(147.5)
        t.rt(90)
        t.pensize(1)
        
class Toit2:
     "Création d'une Class qui dessine un toit isocèle"
     def __init__(self):
        self.nom = "Toit n°2 "
     
     def dessiner(self):
        t.bk(10)                 
        t.fd(163)                 
        t.lt(135)                 
        t.pensize(5)                 
        t.fd(115)                 
        t.lt(90)
        t.fd(115)
        t.pensize(1)
        t.lt(135)
        t.fd(10)
        t.rt(90)                

class Toit3:
    "Création d'une Class qui dessine un toit en triangle rectangle"
    def __init__(self):
        self.nom = "Toit n°3"
        
    def dessiner(self):
        t.fd(158)
        t.lt(163.4)
        t.pensize(5)
        t.fd(175)
        t.bk(10)
        t.pensize(1)
        t.lt(106.6)
        t.fd(47)

class Who:
    "Who signifie qui.C'est une fonction qui dessine aléatoirement un Toit"
    def __init__(self):
        self.nom = "Quels Toit ??"
        self.rt= randint(1, 3)
        
    def random_t(self):
        if self.rt == 1:
            t1=Toit1()
            t1.dessiner()
        elif self.rt == 2:
            t2=Toit2()
            t2.dessiner()
        else:
            t3=Toit3()
            t3.dessiner()

