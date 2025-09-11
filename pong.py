import pygame
import random

# Inicializar pygame
pygame.init()

# Pantalla
ancho, alto = 600, 400
ventana = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Pong en Python")

# Colores
negro = (0, 0, 0)
blanco = (255, 255, 255)

# Paletas
paleta_ancho, paleta_alto = 10, 70
paleta1_y = alto // 2 - paleta_alto // 2
paleta2_y = alto // 2 - paleta_alto // 2
vel_paleta = 7

# Pelota
pelota_x, pelota_y = ancho // 2, alto // 2
pelota_radio = 7
pelota_dx, pelota_dy = random.choice([-4, 4]), random.choice([-4, 4])

# Puntuación
puntaje1, puntaje2 = 0, 0
fuente = pygame.font.SysFont("Arial", 30)

# Reloj
clock = pygame.time.Clock()

ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Teclas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w] and paleta1_y > 0:
        paleta1_y -= vel_paleta
    if teclas[pygame.K_s] and paleta1_y < alto - paleta_alto:
        paleta1_y += vel_paleta
    if teclas[pygame.K_UP] and paleta2_y > 0:
        paleta2_y -= vel_paleta
    if teclas[pygame.K_DOWN] and paleta2_y < alto - paleta_alto:
        paleta2_y += vel_paleta

    # Movimiento pelota
    pelota_x += pelota_dx
    pelota_y += pelota_dy

    # Rebote arriba/abajo
    if pelota_y - pelota_radio <= 0 or pelota_y + pelota_radio >= alto:
        pelota_dy *= -1

    # Rebote paletas
    if (pelota_x - pelota_radio <= 20 and paleta1_y < pelota_y < paleta1_y + paleta_alto) or \
       (pelota_x + pelota_radio >= ancho - 20 and paleta2_y < pelota_y < paleta2_y + paleta_alto):
        pelota_dx *= -1

    # Punto jugador 2
    if pelota_x < 0:
        puntaje2 += 1
        pelota_x, pelota_y = ancho // 2, alto // 2
        pelota_dx *= -1

    # Punto jugador 1
    if pelota_x > ancho:
        puntaje1 += 1
        pelota_x, pelota_y = ancho // 2, alto // 2
        pelota_dx *= -1

    # Dibujar
    ventana.fill(negro)
    pygame.draw.rect(ventana, blanco, (10, paleta1_y, paleta_ancho, paleta_alto))
    pygame.draw.rect(ventana, blanco, (ancho - 20, paleta2_y, paleta_ancho, paleta_alto))
    pygame.draw.circle(ventana, blanco, (pelota_x, pelota_y), pelota_radio)

    # Puntos
    texto = fuente.render(f"{puntaje1} - {puntaje2}", True, blanco)
    ventana.blit(texto, (ancho//2 - 30, 10))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
