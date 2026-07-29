import src.typing_speed_test as speed
import src.detector as detector

while True:
    
    print("Bienvenido al Keyboard Tests")
    print("1. Medir velocidad de escritura")
    print("2. Detectar chatter")
    print("3. Test de teclas")
    print("4. Estadísticas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1": #mide la velocidad a la que escribe el usuario
        speed.medir_velocidad_escritura()

    elif opcion == "2": #detecta si el usuario tiene chatter
        detector.detectar_chatter()
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
        
        
""" 

DICCIONARIO DE FUNCIONES:
1. medir_velocidad_escritura(): Mide la velocidad de escritura del usuario.
2. detectar_chatter(): Detecta si el usuario tiene chatter en su teclado.
3. test_teclas(): Realiza un test de teclas (función pendiente de implementación).
4. estadisticas(): Muestra estadísticas relacionadas con el uso del teclado (función pendiente de implementación).

"""