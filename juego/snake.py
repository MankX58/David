import pygame
import random
import time
import os
import shutil

# Inicializar pygame
pygame.init()



# Definir dimensiones de la ventana
width = 800
height = 600

# Crear la ventana del juego
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Juego del Cubo")

# Definir colores
white = (255, 255, 255)
black = (0, 0, 0)

# Definir las coordenadas y tamaño del cubo
cube_x = 50
cube_y = height - 100
cube_size = 50

# Definir las coordenadas y tamaño de los triángulos
triangle_x = width
triangle_y = random.randint(50, height - 150)
triangle_width = 50
triangle_height = 50

# Definir la velocidad de movimiento
cube_speed = 2
triangle_speed = 2.3

# Variable para controlar el tiempo
start_time = time.time()

game_over = False 

# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # Mover el cubo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        cube_y -= cube_speed
    elif keys[pygame.K_s]:
        cube_y += cube_speed

    # Mover los triángulos
    triangle_x -= triangle_speed

    # Verificar colisiones
    if cube_y + cube_size >= triangle_y and cube_y <= triangle_y + triangle_height and cube_x + cube_size >= triangle_x and cube_x <= triangle_x + triangle_width:
        game_over = True

    # Generar un nuevo triángulo cada 2 segundos
    if time.time() - start_time >= 0.8:
        triangle_x = width
        triangle_y = random.randint(50, height - 150)
        start_time = time.time()

    # Dibujar en la ventana
    window.fill(white)
    pygame.draw.rect(window, black, (cube_x, cube_y, cube_size, cube_size))
    pygame.draw.polygon(window, black, [(triangle_x, triangle_y), (triangle_x + triangle_width, triangle_y), (triangle_x + triangle_width/2, triangle_y - triangle_height)])

    # Actualizar la ventana
    pygame.display.update()

# Salir del juego
pygame.quit()

# Variable para controlar el juego
game_over = False



# Bucle principal del juego
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Volver el cubo al suelo después de 2 segundos
            if time.time() - start_time >= 2:
                cube_y = height - 100
                start_time = time.time()
            # Bucle principal del juego
            while not game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            cube_y -= cube_speed
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            cube_y += cube_speed

                # Mover los triángulos
                triangle_x -= triangle_speed

                # Verificar colisiones
                if cube_y + cube_size >= triangle_y and cube_y <= triangle_y + triangle_height and cube_x + cube_size >= triangle_x and cube_x <= triangle_x + triangle_width:
                    game_over = True

                # Dibujar en la ventana
                window.fill(white)
                pygame.draw.rect(window, black, (cube_x, cube_y, cube_size, cube_size))
                pygame.draw.polygon(window, black, [(triangle_x, triangle_y), (triangle_x + triangle_width, triangle_y), (triangle_x + triangle_width/2, triangle_y - triangle_height)])

                # Actualizar la ventana
                pygame.display.update()

            # Mostrar mensaje de derrota
            font = pygame.font.Font(None, 36)
            text = font.render("Perdiste", True, black)
            text_rect = text.get_rect(center=(width/2, height/2))
            window.blit(text, text_rect)
            pygame.display.update()

            # Salir del juego
            pygame.quit()

    # Mover el cubo
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        cube_y -= cube_speed
    elif keys[pygame.K_s]:
        cube_y += cube_speed

    # Mover los triángulos
    triangle_x -= triangle_speed

    # Verificar colisiones
    if cube_y + cube_size >= triangle_y and cube_y <= triangle_y + triangle_height and cube_x + cube_size >= triangle_x and cube_x <= triangle_x + triangle_width:
        game_over = True

    # Dibujar en la ventana
    window.fill(white)
    pygame.draw.rect(window, black, (cube_x, cube_y, cube_size, cube_size))
    pygame.draw.polygon(window, black, [(triangle_x, triangle_y), (triangle_x + triangle_width, triangle_y), (triangle_x + triangle_width/2, triangle_y - triangle_height)])

    # Actualizar la ventana
    pygame.display.update()

# Salir del juego
pygame.quit()