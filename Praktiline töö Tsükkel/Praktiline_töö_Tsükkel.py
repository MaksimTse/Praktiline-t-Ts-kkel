from math import *
from random import *
import turtle
import time

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

#Ülesanne N.3

#g=1
#try:
#    f = int(input("Mitu ülesandeid sa tahad? "))
#    for d in range (0,f,1):
#        print(f"Ülesanne {g}: ")
#        a = randint(1,50)
#        b = randint(1,50)
#        c = a+b
#        for i in range (0,5,1):
#            answer = int(input(f"{a}+{b}=?"))
#            if answer == a+b:
#                print(f"See on õige! {c}")
#                print()
#                break
#            else:
#                print("Proovi veel korra")
#                print(f"Õige on {c}")
#                print()
#        g += 1
#except:
#    print("See on vale!")

#Ülesanne N.6

#print()
#print("Ülesanne 6")
#print()
#for i in range(0,5):
#    print("* "*5)
#print()
#for i in range(0,10):
#    print("* "*i)
#print()
#for i in range(0,10):
#    print("* "*(10-i))
#print()

#Ülesanne N.8
#while True:
#    try:
#        main = int(input("Vali number 1 kuni 100: "))
#        break
#    except ValueError:
#        print("See pole täisarv")
#if main<1 or main>100:
#    print("Vali õige number")
#else:
#    paaris = 0
#    paaritu = 0
#    x = 0
#    while x != main:
#        x += 1
#        print(int(x), end=" ")
#        if x % 2 == 0:
#            paaris +=1
#        else:
#            paaritu +=1

#print(f"Paaris numbrid: {paaris}")
#print(f"Paaritu numbrid: {paaritu}")



#Ülesanne N.10

#x=1
#while x<=100:
#    if x%5==0:
#        print(x,end=" ")
#    x+=1

#for x in range (1,101,1):
#    if x%5==0:
#        print(x, end=" ")

#Ülesanne N.11

#n=randint(1,10)
#x=0
#while x !=3:
#    text = input("Väljumiseks sistage number: ")
#    x+=1
#    if text == "stopp":
#        print("Välju programmist! Kohtumiseni! See sai tehtud")
#        break
#    elif int(text) == n:
#        print("Palju õnne, sa võitsid")
#        break
#    else:
#        print("Proovi veel korra")
        




#Ülesanne N.13

#print("arv", "  ruut ", "   kuup")
#for i in range(1,11):
#    print(f" {i}    {i ** 2}    {i **3}")
#print("teine variant")
#print("arv", "  ruut ", "   kuup")
#i=1
#while i < 11:
#    print(f" {i}     {i ** 2}     {i ** 3}")
#    i += 1






#Ülesanne N.16

#ans = randint(1, 10)
#while True:
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
#        print("vale! proovi veel korra!")
#        continue



#ans = random.randint(1, 10)
#g = 0
#while ans != g:
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
#        print("vale! proovi veel korra!")
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

#Ülesanne N.22

#n=1
#while True:
#    print("Tahan kommi")
#    a =str(input())
#    if a.lower() == "komm":
#        print("Aitah Oli vaja", str(n),"katse")
#        break
#    else:
#        n=n+1


#import string

#print ("Arva täht - (Aa kuni Zz)")
#letter = random.choice(string.ascii_letters)

#while True:
#    ans = str(input("teie oletus: "))
#    if letter == ans:
#        print("Tubli")
#        break
#    else:
#        print("Provi uuesti!")






























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


