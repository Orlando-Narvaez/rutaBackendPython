import random

print("""
    Bienvenido al juego piedra, papel o tijeras
    para seleccionar una opcion tener en cuenta:
    1 - Piedra
    2 - Papel
    3 - Tijeras

    Gana el mejor de 3\n
    """)

rounds = 1
pointPerson = 0
pointComputer = 0

while True:
    print("*" *10)
    print("ROUND ", rounds)
    print("*" *10)
    print("\nLa maquina lleva: ", pointComputer, " puntos\nUsted lleva: ", pointPerson, " puntos")
    userOption = 0
    while userOption <= 0 or userOption >=4:
        userOption = int(input("\nEscoge una opcion: entre el 1 = (Piedra), 2 = (Papel) y el 3 = (Tijeras) : "))
        if userOption <= 0 or userOption >=4:
            print("\nIngrese un valor valido por favor")
    computerOpcion = random.randint(1, 3) #para strings se usa: choice

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
    
    if pointPerson == 2:
        print("\nFelicidades, has ganado el juego!")
        break
    elif pointComputer == 2:
        print("\nVaya has perdido, gano la maquina, suerte a la proxima")
        break
    else:
        rounds += 1