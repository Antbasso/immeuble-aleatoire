import turtle as t

class Balcon:
    "Création d'une classe qui dessine un balcon"
    def __init__(self):
        self.nom = "balcon"
    def dessiner(self):
        t.pensize(2)
        t.pendown()
        for i in range(6):
            t.left(90)
            t.forward(8)
            t.penup()
            t.right(90)
            t.forward(5)
            t.right(90)
            t.forward(8)
            t.left(90)
            t.pendown()
        t.right(180)
        for i in range(2):
            t.forward(30)
            t.right(90)
            t.forward(8)
            t.right(90)
        t.penup()
        t.pensize(1) 
        t.fd(30)
        t.rt(180)















    
