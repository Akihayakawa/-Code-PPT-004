import random
import time 
lista = ["Piedra","Papel","Tijera"]
jugador = input("Piedra papel o tijera?: ")
time.sleep(1)
ran = random.choice(lista)
print(ran)
def piedra():
    if ran == "Papel":
        print("has perdido")
    elif ran == "Tijera":
        print("Has ganado")
def papel():
    if ran == "Piedra":
        print("Has ganado")
    elif ran == "Tijera":
        print("Has perdido")

def tijera():
    if ran == "Papel":
        print("Has ganado")
    elif ran == "Piedra":
        print("Has perido")

if jugador == ran:
    print("ha sido un empate")
elif jugador == "piedra":
    piedra()
elif jugador == "tijera" :
    tijera()
elif jugador == "papel":
    papel()

pritn('''
    A____A
    |・ㅅ・|
    |っ　ｃ|
    |　　　|
    |　　　|
    |　　　|
    |　　　|
    |　　　|
    U￣￣U
 ''')

