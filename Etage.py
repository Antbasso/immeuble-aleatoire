import turtle as t
from Fenetre import *
from Porte import *
from random import randint
class Etage:
    "Création d'une classe qui dessiner un étage"
    def __init__(self):
        self.nom = "etage"

    def dessiner(self,n):
        t.begin_fill()
        t.color("black", n)
        for i in range(2):
            t.fd(140)
            t.lt(90)
            t.fd(60)
            t.lt(90)
        t.end_fill()
        t.penup()
        t.lt(90)
        t.fd(15)
        t.rt(90)
        t.fd(10)
        w=Who3()
        w.random_t()
        t.fd(46)
        w2=Who3()
        w2.random_t()
        t.fd(46)
        w3=Who3()
        w3.random_t()
        t.fd(10)
        t.rt(90)
        t.fd(15)
        t.rt(90)
        t.fd(112)
        t.rt(180)
        t.lt(90)
        t.fd(60)
        t.rt(90)
        t.pendown()
        
class Rdc:
    "Création d'une classe qui dessiner un rez de chaussée"
    def __init__(self):
        self.nom = "rdc"
    
    def dessiner(self, n):
        rdm2 = randint(1, 3)
        t.begin_fill()
        t.color("black", n)
        for i in range(2):
            t.fd(140)
            t.lt(90)
            t.fd(60)
            t.lt(90)
        t.end_fill()
        t.penup()
        t.fd(10)
        if rdm2 == 1:
            po1=Who2()
            po1.random_t()
        else:
            t.lt(90)
            t.fd(15)
            t.rt(90)
            a = Fenetre()
            a.dessiner()
            t.rt(90)
            t.fd(15)
            t.lt(90)
        t.fd(46)   
        if rdm2 == 2:
            po1=Who2()
            po1.random_t()
        else:
            t.lt(90)
            t.fd(15)
            t.rt(90)
            a = Fenetre()
            a.dessiner()
            t.rt(90)
            t.fd(15)
            t.lt(90)
        t.fd(46)  
        if rdm2 == 3:
            po1=Who2()
            po1.random_t()
        else:
            t.lt(90)
            t.fd(15)
            t.rt(90)
            a = Fenetre()
            a.dessiner()
            t.rt(90)
            t.fd(15)
            t.lt(90)
        t.up()
        t.lt(180)
        t.fd(102)
        t.rt(90)
        t.fd(60)
        t.rt(90)
        t.pendown()
