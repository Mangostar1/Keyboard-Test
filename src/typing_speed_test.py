import keyboard
import time


def medir_velocidad_escritura():

    velocidad_usuario = 0 # velocidad por defecto
    total_teclas = 0 # total de teclas presionadas
    ultimo_tiempo = None # tiempo del último evento de teclado

    print("Presione ESC para salir.")

    while True:
        evento = keyboard.read_event()

        if evento.event_type == keyboard.KEY_DOWN:
            
            if total_teclas == 0: # se asigna el tiempo actual al primer evento de teclado
                ultimo_tiempo = time.perf_counter() # se asigna el tiempo actual al primer evento de teclado
                total_teclas += 1
                continue
            
            tiempo_actual = time.perf_counter()
            velocidad_usuario = (tiempo_actual - ultimo_tiempo) * 1000 # se asigna la velocidad en milisegundos
            total_teclas += 1

            ultimo_tiempo = tiempo_actual
            
            print(f"Velocidad de escritura: {velocidad_usuario:.2f} ms")
            print(f"Total de teclas presionadas: {total_teclas}")

        if evento.name == "esc":
            print("Saliendo...")
            break