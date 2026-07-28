import src.typing_speed_test as speed

print("Bienvenido al Keyboard Tests")
print("Presione una opcion:")
print("1. Medir velocidad del teclado")
print("5. Salir")

while True:

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        speed.medir_velocidad_teclado()

    elif opcion == "2":
        #detectar_chatter()
        break

    elif opcion == "3":
        #test_teclas()
        break

    elif opcion == "4":
        #estadisticas()
        break

    elif opcion == "5":
        break