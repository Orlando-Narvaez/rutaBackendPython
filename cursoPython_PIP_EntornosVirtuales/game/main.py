import random

def chooseOptions():
    userOption = 0
    while userOption <= 0 or userOption >=4:
        userOption = int(input("\nEscoge una opcion: entre el 1 = (Piedra), 2 = (Papel) y el 3 = (Tijeras) : "))
        if userOption <= 0 or userOption >=4:
            print("\nIngrese un valor valido por favor")
    computerOpcion = random.randint(1, 3) #para strings se usa: choice
    print("Usted escogio: ",userOption)
    print("La maquina escogio: ",computerOpcion,"\n")
    return userOption, computerOpcion

def checkRules(userOption,computerOpcion,pointPerson,pointComputer):
    if userOption == computerOpcion:
        print("\nEmpate!")
    elif userOption == 1:
        if computerOpcion == 2:
            print("\nHas perdido, la maquina escogio Papel")
            pointComputer += 1
        else:
            print("\nHas ganado, la maquina escogio Tijeras")
            pointPerson += 1
    elif userOption == 2:
        if computerOpcion == 1:
            print("\nHas ganado, la maquina escogio Piedra")
            pointPerson += 1
        else:
            print("\nHas perdido, la maquina escogido Tijeras")
            pointComputer += 1
    elif userOption == 3:
        if computerOpcion == 1:
            print("\nHas perdido, la maquina escogio Piedra")
            pointComputer += 1
        else:
            print("\nHas ganado, la maquina escogido papel")
            pointPerson += 1
    return pointPerson, pointComputer

def checkWin(pointPerson,pointComputer):
    if pointPerson == 2:
        print("\nFelicidades, has ganado el juego!")
        return False
    elif pointComputer == 2:
        print("\nVaya has perdido, gano la maquina, suerte a la proxima")
        return False
    return True
            

def run():

    print("""
    Bienvenido al juego piedra, papel o tijeras
    para seleccionar una opcion tener en cuenta:
    1 - Piedra
    2 - Papel
    3 - Tijeras
    Gana el mejor de 3\n
    """)

    pointPerson = 0
    pointComputer = 0
    rounds = 1
    run = True

    while run == True:

        print("*" *10)
        print("ROUND ", rounds)
        print("*" *10)

        print("\nLa maquina lleva: ", pointComputer, " puntos\nUsted lleva: ", pointPerson, " puntos")

        userOption, computerOpcion = chooseOptions()

        pointPerson, pointComputer = checkRules(userOption,computerOpcion,pointPerson,pointComputer)
        
        run = checkWin(pointPerson,pointComputer)

        rounds += 1

if __name__ == '__main__':
    run()