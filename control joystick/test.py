import pygame
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No hay joystick conectado.")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()

print(f"Joystick detectado: {joystick.get_name()}")
print(f"Ejes disponibles: {joystick.get_numaxes()}")

try:
    while True:
        pygame.event.pump()
        for i in range(joystick.get_numaxes()):
            valor = joystick.get_axis(i)
            print(f"Eje {i}: {valor:.2f}", end=' | ')
        print()
        time.sleep(0.2)

except KeyboardInterrupt:
    pygame.quit()