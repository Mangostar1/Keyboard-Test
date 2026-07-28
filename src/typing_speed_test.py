import keyboard
import time

def medir_velocidad_teclado(umbral_ms=60):
    ultima_tecla = {}
    ultimo_tiempo = time.perf_counter()

    print("Presione ESC para salir.")

    while True:
        evento = keyboard.read_event()

        if evento.event_type == keyboard.KEY_DOWN:
            tiempo_actual = time.perf_counter()
            diferencia = (tiempo_actual - ultimo_tiempo) * 1000

            if diferencia < umbral_ms:
                print("¡Tecla presionada demasiado rápido!")

            ultimo_tiempo = tiempo_actual

        if evento.name == "esc":
            print("Saliendo...")
            break




""" umbral_ms = 60

ultima_tecla = {}

ultimo_tiempo = time.perf_counter()

print("Presione ESC para salir.")

while True:

  evento = keyboard.read_event()

  if evento.event_type == keyboard.KEY_DOWN:

    tiempo_actual = time.perf_counter()

    diferencia = (tiempo_actual - ultimo_tiempo) * 1000

    # print(f"Tecla: {evento.name} ({diferencia:.2f} ms)")
    
    if diferencia < umbral_ms:
      print("¡Tecla presionada demasiado rápido!")

    ultimo_tiempo = tiempo_actual

  if evento.name == "esc":
    print("Saliendo...")
    break """