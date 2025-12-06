import random
import math

print()
print("Hola, como estas, en este momento vas a jugar piedra, papel o tijeras, el primer modo el facil es a la primera y el segundo modo es el dificil que es al mejor de 5 juegos")
print()


# VALIDACIÓN DEL MODO DE JUEGO

while True:
    entrada = input("Elige el modo de juego (1) facil,(2) dificil: ")
    print()

    try:
        c = float(entrada)
        if c == 1 or c == 2:
            break
        else:
            print("Porfavor elije solo entre el numero (1) para modo facil y (2) para el modo dificil")
            print()

    except:
        print("Porfavor elije solo entre el numero (1) para modo facil y (2) para el modo dificil")
        print()


# MODO FÁCIL

if c == 1:
    print("Has elegido el modo facil, en este modo ganaras si ganas la primera ronda")
    print()


    while True:
        entrada = input("Elige tu jugada (1) piedra,(2) papel,(3) tijeras: ")
        print() 
        try:
            jugador = float(entrada)
            if jugador == 1 or jugador == 2 or jugador == 3:
                break
            else:
                print("Porfavor elije solo entre los numeros (1) para piedra,(2) para papel y (3) para tijeras")
                print()

        except:
            print("Porfavor elije solo entre los numeros (1) para piedra,(2) para papel y (3) para tijeras")
            print()


    if jugador == 1:
        textoju = "Piedra"
    elif jugador == 2:
        textoju = "Papel"
    else:
        textoju = "Tijeras"

    compu = math.floor(random.random() * 3) + 1

    if compu == 1:
        textoco = "Piedra"
    elif compu == 2:
        textoco = "Papel"
    else:
        textoco = "Tijeras"

    print("-Tú elegiste " + textoju + " y la computadora eligió " + textoco)
    print()


    if compu == jugador:
        print("Genial no perdiste, pero tampoco ganaste, tienes un merecido empate")
        print()
        print()
        print()
        print("Fin del juego")

    elif (jugador == 1 and compu == 3) or (jugador == 2 and compu == 1) or (jugador == 3 and compu == 2):
        print("Felicidades, ganaste^^")
        print()
        print()
        print()
        print("Fin del juego")

    else:
        print("Ohhh, lastimosamente perdiste :c")
        print()
        print()
        print()
        print("Fin del juego")
        



# MODO DIFÍCIL

else:
    print("Has elegido el modo dificil, en este modo ganaras si ganas la mayoria de las 5 rondas")  
    print()

    ronda = 1
    puntosj = 0
    puntosc = 0
    empates = 0
    piedra = 0
    papel = 0
    tijeras = 0

    while ronda <= 5:

        while True:
            entrada = input("Elige tu jugada (1) piedra,(2) papel,(3) tijeras: ")
            print()

            try:
                jujugador = float(entrada)
                if jujugador == 1 or jujugador == 2 or jujugador == 3:
                    break
                else:
                    print("Porfavor elije solo entre los numeros (1) para piedra, (2) para papel y (3) para tijeras")
                    print()

            except:
                print("Porfavor elije solo entre los numeros (1) para piedra, (2) para papel y (3) para tijeras")
                print()


        if jujugador == 1:
            piedra = piedra + 1
            jutexto = "Piedra"
        elif jujugador == 2:
            papel = papel + 1
            jutexto = "Papel"
        else:
            tijeras = tijeras + 1
            jutexto = "Tijeras"

        if piedra > papel and piedra > tijeras:
            jucompu = 2
        elif papel > piedra and papel > tijeras:
            jucompu = 3
        elif tijeras > piedra and tijeras > papel:
            jucompu = 1
        else:
            jucompu = math.floor(random.random() * 3) + 1

        if jucompu == 1:
            cotexto = "Piedra"
        elif jucompu == 2:
            cotexto = "Papel"
        else:
            cotexto = "Tijeras"

        print("-Tú elegiste " + jutexto + " y la computadora eligió " + cotexto)
        print()


        if jujugador == jucompu:
            empates = empates + 1
            print("Genial no perdiste, pero tampoco ganaste, tienes un merecido empate")
            print()

        elif (jujugador == 1 and jucompu == 3) or (jujugador == 2 and jucompu == 1) or (jujugador == 3 and jucompu == 2):
            puntosj = puntosj + 1
            print("Felicidades, ganaste la ronda ^^")
            print()

        else:
            puntosc = puntosc + 1
            print("Ohhh, lastimosamente perdiste la ronda :c")
            print()


        ronda = ronda + 1

    # Resultados finales de las 5 rondas
    print("-Felicidades de las 5 rondas ganaste", puntosj)
    print()

    print("-Bueno de las 5 rondas te gane", puntosc)
    print()

    print("-Y por ultimo de las 5 rondas empatamos", empates)
    print()


    if puntosj > puntosc:
        print("Congratulations!!!!! eres el ganador")
        print()
        print()
        print()
        print("Fin del juego")

    elif puntosc > puntosj:
        print("Chale hiciste lo mejor que pudiste pero perdiste ya que te gane mas rondas, suerte en la proxima")
        print()
        print()
        print()
        print("Fin del juego")

    else:
        print("Un resultado que no me esperaba, acabamos de empatar, prueba de nuevo a ver si esta vez me ganas")
        print()
        print()
        print()
        print("Fin del juego")