from math import *
from random import *
import turtle

#Ülesanne N.0



#def draw_shape(kuju):
#    turtle.pen(pencolor="purple",pensize=10)
#    turtle.speed(0)
#    turtle.shapesize(3,3,3)
#    turtle.fillcolor("red")
#    if kuju == "ring":
#        turtle.circle(50)
#    elif kuju == "kolmnurk":
#        for i in range(3):
#            turtle.forward(100)
#            turtle.left(120)
#    elif kuju == "ruut":
#        for i in range(4):
#            turtle.forward(100)
#            turtle.left(90)

#kuju = input("Sisestage kujund (ring, kolmnurk, ruut): \n")
#draw_shape(kuju)
#turtle.done()





#Ülesanne N.10

#x=1
#while x<=100:
#    if x%5==0:
#        print(x,end=" ")
#    x+=1

#for x in range (1,101,1):
#    if x%5==0:
#        print(x, end=" ")








#Ülesanne N.16


#while True:
#    ans = random.randint(1, 10)
#    g = input("mis numbri ma arvasin?(1-10, mängu lõpetamiseks kirjutage *lõpp* ) \n")
#    if g.lower() == "lõpp":
#        print("mäng on läbi!")
#        break
#    if not g.isnumeric():
#        print("Vale andmetüüp!")
#        continue
#    g = int(g)
#    if g == ans:
#        print("õige! sa arvasid ära!")
#        break
#    if g>10 or g<1:
#        print("Vahemik on vale!")
#        continue
#    elif g !=ans:
#        print(f"vale! proovi veel korra! number oli {ans}")
#        continue



#Ülesanne N.17

#try:
#    num_horiz=int(input("Sisesta ruutude arv horisontaalselt =>> \n"))
#except:
#    print("Vale andmetüüp")
#    num_horiz=randint(1,20)
#try:
#    num_vert=int(input("Sisesta ruutude arv vertikalselt =>> \n"))
#except:
#    print("Vale andmetüüp")
#    num_vert=randint(1,20)

#for y in range(num_vert):
#    for x in range(num_horiz):
#        print("o", end=" ")
#    print()





































#sõnad = ["python", "programmeerimine", "keel", "arvuti", "keemia", ""]
#ans = random.choice(sõnad)
#g = []
#maximum = 6
#while maximum > 0:
#    print(" ".join(letter if letter in g else "_" for letter in ans))
#    print("Sul on", maximum, "oletused jäänud.")
#    guess = input("Arva ära täht või sõna: ").lower()
#    if len(guess) > 1:
#        if guess == ans:
#            print("Palju õnne! Sa arvasid õige sõna.")
#            break
#        else:
#            print("Vale! Sõna oli ", ans)
#            break
#    elif guess in g:
#        print("Sa juba arvasid seda kirja. Proovi uuesti.")
#    elif guess in ans:
#        print("Õige!")
#        g.append(guess)
#    else:
#        print("Vale!")
#        g.append(guess)
#        maximum -= 1
#    if set(ans) == set(g):
#        print("Palju õnne! Sa arvasid õige sõna.")
#        break
#    if maximum == 0:
#        print("Mäng läbi! Sõna oli:", ans)


