import pygame
import time
import random

# Inicializar pygame
pygame.init()

# Tamaño de la pantalla
ancho = 600
alto = 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Snake en Python")

# Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
verde = (0, 255, 0)
rojo = (255, 0, 0)

# Configuración del Snake
tamaño_bloque = 20
velocidad = 10
clock = pygame.time.Clock()

# Fuente
fuente = pygame.font.SysFont("Arial", 25)

def mostrar_mensaje(msg, color):
    texto = fuente.render(msg, True, color)
    ventana.blit(texto, [ancho/6, alto/3])

def juego():
    game_over = False
    x = ancho // 2
    y = alto // 2
    x_cambio = 0
    y_cambio = 0

    snake = []
    longitud = 1

    # Comida inicial
    comida_x = round(random.randrange(0, ancho - tamaño_bloque) / 20.0) * 20
    comida_y = round(random.randrange(0, alto - tamaño_bloque) / 20.0) * 20

    while not game_over:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                game_over = True
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    x_cambio = -tamaño_bloque
                    y_cambio = 0
                elif evento.key == pygame.K_RIGHT:
                    x_cambio = tamaño_bloque
                    y_cambio = 0
                elif evento.key == pygame.K_UP:
                    y_cambio = -tamaño_bloque
                    x_cambio = 0
                elif evento.key == pygame.K_DOWN:
                    y_cambio = tamaño_bloque
                    x_cambio = 0

        x += x_cambio
        y += y_cambio

        if x >= ancho or x < 0 or y >= alto or y < 0:
            game_over = True

        ventana.fill(negro)
        pygame.draw.rect(ventana, rojo, [comida_x, comida_y, tamaño_bloque, tamaño_bloque])

        cabeza = []
        cabeza.append(x)
        cabeza.append(y)
        snake.append(cabeza)

        if len(snake) > longitud:
            del snake[0]

        for bloque in snake[:-1]:
            if bloque == cabeza:
                game_over = True

        for bloque in snake:
            pygame.draw.rect(ventana, verde, [bloque[0], bloque[1], tamaño_bloque, tamaño_bloque])

        pygame.display.update()

        if x == comida_x and y == comida_y:
            comida_x = round(random.randrange(0, ancho - tamaño_bloque) / 20.0) * 20
            comida_y = round(random.randrange(0, alto - tamaño_bloque) / 20.0) * 20
            longitud += 1

        clock.tick(velocidad)

    ventana.fill(blanco)
    mostrar_mensaje("¡Game Over! Presiona ESC para salir", rojo)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    quit()

juego()
