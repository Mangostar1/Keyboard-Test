import src.typing_speed_test as speed

while True:
    
    print("Bienvenido al Keyboard Tests")
    print("1. Medir velocidad de escritura")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1": #mide la velocidad a la que escribe el usuario
        speed.medir_velocidad_escritura()

    elif opcion == "2":
        #detectar_chatter()
        break

    elif opcion == "3":
        #test_teclas()
        break

    elif opcion == "4":
        #estadisticas()
        break

    elif opcion == "5" or opcion.lower() == "salir":
        break
    
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")