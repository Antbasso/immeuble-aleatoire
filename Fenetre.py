import turtle as t
from Balcon import *
from random import randint

class Fenetre:
    def __init__(self):
        self.nom = "fenetre"
        
    def dessiner(self):
        t.pendown()
        t.color("black", 'White' )
        t.begin_fill()
        for i in range(4):
            t.forward(30)
            t.left(90)
        t.end_fill()
        t.penup()
        t.forward(15)
        t.left(90)
        t.pendown()
        t.forward(30)
        t.penup()
        t.left(90)
        t.forward(15)
        t.left(90)
        t.forward(15)
        t.left(90)
        t.pendown()
        t.forward(30)
        t.penup()
        t.right(90)
        t.fd(15)
        t.right(90)
        t.fd(30)
        t.right(180)
        t.penup()
        
        
class Fenetre2:
    def __init__(self):
        self.nom = "fenetre2"
        
    def dessiner(self):
        t.color("black", 'White' )
        t.begin_fill()
        t.pendown()
        for i in range(4):
            t.forward(30)
            t.left(90)
        t.penup()
        b=Balcon()
        b.dessiner()
        t.end_fill()
        
class Who3:
    def __init__(self):
        self.nom = "Quelle Fenetre ??"
        self.rdm= randint(1, 2)
        
    def random_t(self):
        if self.rdm == 1:
            p1=Fenetre()
            p1.dessiner()
        
        else:
            p2=Fenetre2()
            p2.dessiner()
    
