import turtle
from math import cos, sin, radians

def Criar_circulo(r):
    gershwin = turtle.Turtle()
    gershwin.speed(10)
    gershwin.hideturtle()
    gershwin.color('white')
    turtle.Screen().bgcolor('black')
    gershwin.penup()
    gershwin.setpos(0, -r)
    gershwin.pendown()
    gershwin.circle(r)

def Calc_pontos(r, a, q):
    
    # r é a medida do raio
    # a é o valor do angulo em radianos
    # q é a quantidade de pontos 

    Pontos = []
    for x in range(q):
        Pos_ponto = [r*cos(a*x), r*sin(a*x)]
        Pontos += [Pos_ponto]
    return Pontos

def Criar_img(p, q, m, r):
    george = turtle.Turtle()
    george.speed(10)
    george.hideturtle()
    george.setpos(0,0)
    george.penup()
    george.setpos(0, -r-30)
    george.color('#e6eaed')
    george.pendown()
    george.write(str(m), align="center", font=("Arial", 13))
    george.penup()
    for n in range(q):
        result = n*m
        if result >= q:
            result %= q
        george.penup()
        george.setpos(p[n])
        george.pendown()
        george.setpos(p[result])

def brincando(r, q, m):
    ang = radians(360/q)
    Criar_circulo(r)
    calc = Calc_pontos(r, ang, q)
    Criar_img(calc, q, m, r)

raio = int(input("Raio: "))
qnt = int(input("Quantidade de Pontos: "))
mult = int(input("Multiplicador: "))


brincando(raio, qnt, mult)

'''
for x in range(2, 9):
    brincando(300, 100, x)
    turtle.clearscreen()
'''

turtle.done()
