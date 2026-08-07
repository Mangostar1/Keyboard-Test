import keyboard
import time
import subprocess


def medir_velocidad_escritura():

    velocidad_usuario = 0 # velocidad por defecto
    total_teclas = 0 # total de teclas presionadas
    ultimo_tiempo = None # tiempo del último evento de teclado
    velocidad_promedio = [] # velocidad promedio de escritura del usuario | NO IMPLEMENTADO

    print("Presione ESC para salir.")

    while True: # bucle infinito para medir la velocidad de escritura del usuario
        evento = keyboard.read_event()

        if evento.event_type == keyboard.KEY_DOWN: # se ejecuta cuando se presiona una tecla
            
            if total_teclas == 0: # se asigna el tiempo actual al primer evento de teclado
                ultimo_tiempo = time.perf_counter() # se asigna el tiempo actual al primer evento de teclado
                total_teclas += 1
                continue
            
            tiempo_actual = time.perf_counter() # se asigna el tiempo actual al evento de teclado
            velocidad_usuario = (tiempo_actual - ultimo_tiempo) * 1000 # se asigna la velocidad en milisegundos
            velocidad_promedio.append(velocidad_usuario)
            total_teclas += 1

            ultimo_tiempo = tiempo_actual # se actualiza el tiempo del último evento de teclado
            
            subprocess.call("clear||cls")
            print(f"Velocidad de escritura: {velocidad_usuario:.2f} ms")
            print(f"Total de teclas presionadas: {total_teclas}")
            
            if velocidad_promedio != []: # si el array esta vacio, no se calcula la velocidad promedio
                promedio = sum(velocidad_promedio) / len(velocidad_promedio) # se calcula la velocidad promedio de escritura del usuario
                print(f"Velocidad promedio: {promedio:.2f} ms")

        if evento.name == "esc":
            print("Saliendo...")
            break