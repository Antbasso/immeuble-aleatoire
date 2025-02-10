import turtle as t
from Immeuble import *

class Main :
    def __init__(self):
        self.nom = "main"
        
    def dessiner(self):
        t.reset()
        t.st()
        t.speed(99999)
        t.setup(1000,500)
        t.penup()
        t.setpos(-500,-220)
        t.pendown()
        t.pensize(5)
        t.forward(1000)
        t.bk(1000)
        t.pensize(1)
        t.up()
        t.fd(80)
        for i in range(4):
            t.pendown()
            i=Immeuble()
            i.dessiner()
            t.penup()
            t.fd(241)
             
m=Main()
m.dessiner()