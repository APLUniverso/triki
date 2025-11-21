def imprimirTablero(tablero):
    for i in range(0,9,3):
        linea = tablero[i:i+3]
        print(" | ".join(linea))

        if i < 6:
            print("---------")   

def condicion(tablero,a,b,c):
    if (tablero[a] != " " and tablero[b] != " " and tablero[c] != " "):
        return tablero[a] == tablero[b] and tablero[b] == tablero[c]  
    else:
        return False

def verificar_ganador(tablero):
    if condicion(tablero,0,1,2) or condicion(tablero,3,4,5) or condicion(tablero,6,7,8) or condicion(tablero,0,3,6) or condicion(tablero,1,4,7) or condicion(tablero,2,5,8) or condicion(tablero,0,4,8) or condicion(tablero,2,4,6):
        return True
    else:
        return False

def put(posicion,tablero,caracter):
    for i in range(9,0,-1):
        if i >= 1 and i <= 3:
            if posicion == i:
                tablero[posicion + 5] = caracter 
        if i >= 4 and i <= 6:
            if posicion == i:
                tablero[posicion - 1] = caracter
        if i >= 7 and i <= 9:
            if posicion == i:
                tablero[posicion-7] = caracter  
    return tablero


tablero = [" ", " ", " ", " ", " ", " ", " ", " ", " ",]

print("====TRES EN RAYA====")
imprimirTablero(tablero)

print("porfavor ingrese el nombre de los jugadores")
jugador_1 = input("ingrese el nombre del jugar 1: ")
jugador_2 = input("ingrese el nombre del jugar 2: ")

print("-------------------------------------")
print("====Reglas====")
print("Para poder dibujar, escribe la posicion del espacio usando \nlas teclas a la derecha con los numeros \nrepresenta perfectamente la cuadricula del triki")


ganador = True
for i in range(0,9,1):
    if verificar_ganador(tablero) :
            print("Felicitaciones")
            if i%2 == 0:
                print(f"Ha ganado el jugador {jugador_2}")
            else:
                print(f"Ha ganado el jugador {jugador_1}")
            ganador = False
            break
    else:
        print("---------------------------------")
        print(f"Turno numero {i+1}: ")
        if i%2 == 0:
            print(f"Turno de {jugador_1} con el simbolo: O")
            posicion = int(input("Ingrese la posicion de donde desea ponerlo: "))
            imprimirTablero(put(posicion,tablero,"O"))
        else:
            print(f"Turno de {jugador_2} con el simbolo: X")
            posicion = int(input("Ingrese la posicion de donde desea ponerlo: "))
            imprimirTablero(put(posicion,tablero,"X"))

if ganador :
    print("EMPATE")
    print("el tablero quedo asi: ")
    imprimirTablero(tablero)


