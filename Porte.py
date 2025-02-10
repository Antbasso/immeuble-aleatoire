import turtle as t
from random import randint
from Fenetre import *

COULEURS = ["grey","red","orange","green","blue","navy","yellow","gold","tan","brown","sienna","wheat","cyan","pink","salmon","violet","purple"]


class Porte1:
    def __init__(self):
        index_choisi_P = randint(0, len(COULEURS)-1)
        self.nom = "porte n°1"
        self.c1 = COULEURS[index_choisi_P]
        
    def dessiner(self):
        t.color("black", self.c1 )
        t.begin_fill()
        for i in range(2):
             t.fd(30)
             t.lt(90)
             t.fd(50)
             t.lt(90)
        t.end_fill()
        t.up()
        t.fd(25)
        t.lt(90)
        t.fd(20)
        t.down()
        t.color("black", "black")
        t.begin_fill()
        t.circle(2.5)
        t.end_fill()
        t.up()
        t.lt(180)
        t.fd(20)
        t.rt(90)
        t.fd(25)
        t.lt(180)
        
    
class Porte2:
    def __init__(self):
        index_choisi_P = randint(0, len(COULEURS)-1)
        self.nom = "porte n°2"
        self.c2 = COULEURS[index_choisi_P]

    def dessiner(self):
        t.color("black", self.c2 )
        t.begin_fill()
        t.fd(30)
        t.lt(90)
        t.fd(45)
        t.circle(15,180)
        t.fd(45)
        t.lt(90)
        t.up()
        t.fd(25)
        t.lt(90)
        t.fd(20)
        t.down()
        t.end_fill()
        t.color("black", "black")
        t.begin_fill()
        t.circle(2.5)
        t.end_fill()
        t.up()
        t.fd(30)
        t.lt(90)
        t.fd(10)
        t.down()
        t.color("black", "white" )
        t.begin_fill()
        t.circle(5)
        t.end_fill()
        t.pensize(1)
        t.lt(90)
        t.fd(10)
        t.bk(5)
        t.rt(90)
        t.fd(5)
        t.bk(10)
        t.fd(5)
        t.up()
        t.rt(90)
        t.st()
        t.bk(45)
        t.rt(90)
        t.bk(15)
class Porte3:
    
    def __init__(self):
        index_choisi_P = randint(0, len(COULEURS)-1)
        self.nom = "porte n°3"
        self.c3 = COULEURS[index_choisi_P]
        
    def dessiner(self):
        t.color("black", self.c3 )
        t.begin_fill()
        t.fd(30)
        t.lt(90)
        t.fd(45)
        t.circle(15,180)
        t.fd(45)
        t.lt(90)
        t.up()
        t.fd(25)
        t.lt(90)
        t.fd(20)
        t.down()
        t.end_fill()
        t.color("black", "black")
        t.begin_fill()
        t.circle(2.5)
        t.end_fill()
        t.up()
        t.fd(25)
        t.lt(90)
        t.down()
        t.color("black", "white" )
        t.begin_fill()
        t.rt(90)
        t.circle(10,180)
        t.rt(90)
        t.bk(20)
        t.end_fill()
        t.up()
        t.lt(90)
        t.fd(45)
        t.rt(90)
        t.fd(25)
        t.rt(180)
        
        
class Who2:
    def __init__(self):
        self.nom = "Quelle Porte ??"
        self.rdm= randint(1, 3)
        
        
    def random_t(self):
        if self.rdm == 1:
            t.pendown()
            p1=Porte1()
            p1.dessiner()
        elif self.rdm == 2:
            t.pendown()
            p2=Porte2()
            p2.dessiner()
        else:
            t.pendown()
            p3=Porte3()
            p3.dessiner()
        
