import keyboard
import time
import subprocess

def detectar_chatter():
  print("key chatter en construccion...")
  print("Presione ESC para salir.")
  
  while True:
    
    evento = keyboard.read_event()
    
    if evento.event_type == keyboard.KEY_DOWN:
      
      subprocess.call("clear||cls")
      print("Funcion de deteccion de chatter en construccion...")
    
      if evento.name == "esc":
        
        print("Saliendo...")
        break