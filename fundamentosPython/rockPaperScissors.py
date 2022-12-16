import random

print("""
Bienvenido al juego piedra, papel o tijeras
para seleccionar una opcion tener en cuenta:
1 - Piedra
2 - Papel
3 - Tijeras
""")
userOption = int(input("Escoge una opcion: entre el 1 y el 3: "))
computerOpcion = random.randint(1, 3) #para strings se usa: choice

if userOption == computerOpcion:
    print("Empate!")
elif userOption == 1:
    if computerOpcion == 2:
        print("Has perdido, la maquina escogio Papel")
    else:
        print("Has ganado, la maquina escogio Tijeras")
elif userOption == 2:
    if computerOpcion == 1:
        print("Has ganado, la maquina escogio Piedra")
    else:
        print("Has perdido, la maquina escogido Tijeras")
elif userOption == 3:
    if computerOpcion == 1:
        print("Has perdido, la maquina escogio Piedra")
    else:
        print("Has ganado, la maquina escogido papel")