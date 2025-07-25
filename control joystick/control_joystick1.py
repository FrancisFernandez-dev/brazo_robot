import pygame
import serial
import time

def aplicar_deadzone(valor, zona):
    if abs(valor) < zona:
        return 0
    else:
        if valor > 0:
            return (valor - zona) / (1 - zona)
        else:
            return (valor + zona) / (1 - zona)

arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No joystick conectado")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

deadzone = 0.15

# Posiciones iniciales de los servos
pos1 = 90
pos2 = 90
pos3 = 90

# Controla la sensibilidad (grados que cambia por ciclo)
velocidad = 4       # Baja sensibilidad (puedes probar con 0.5 o 0.2 para más lenta)

try:
    while True:
        pygame.event.pump()

        eje_izq_x = aplicar_deadzone(joystick.get_axis(0), deadzone)
        eje_izq_y = aplicar_deadzone(joystick.get_axis(1), deadzone)
        eje_der_x = aplicar_deadzone(joystick.get_axis(3), deadzone)

        # Cambiar posición sumando la velocidad escalada por el eje
        pos1 += eje_izq_x * velocidad
        pos2 += eje_izq_y * velocidad
        pos3 += eje_der_x * velocidad

        # Limitar los valores para que queden entre 0 y 180
        pos1 = max(0, min(180, pos1))
        pos2 = max(0, min(180, pos2))
        pos3 = max(0, min(180, pos3))

        mensaje = f"{int(pos1)},{int(pos2)},{int(pos3)}\n"
        arduino.write(mensaje.encode('utf-8'))

        print(f"Servo1: {int(pos1)} | Servo2: {int(pos2)} | Servo3: {int(pos3)}")

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Programa terminado")
finally:
    arduino.close()
    pygame.quit()
