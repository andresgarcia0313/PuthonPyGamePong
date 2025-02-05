import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de pantalla
screen_info = pygame.display.Info()
WIDTH = int(screen_info.current_w * 0.8)
HEIGHT = int(screen_info.current_h * 0.8)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Variables de juego
ball = pygame.Rect(WIDTH//2, HEIGHT//2, 15, 15)
paddle_height = int(HEIGHT * 0.16)
paddle_width = int(WIDTH * 0.03)
paddle1 = pygame.Rect(WIDTH//30, HEIGHT//2 -
                      paddle_height//2, paddle_width, paddle_height)
paddle2 = pygame.Rect(WIDTH - (WIDTH//30) - paddle_width, HEIGHT //
                      2 - (paddle_height)//2, paddle_width, paddle_height)
ball_speed = [random.choice([-5, 5]), random.choice([-5, 5])]
paddle_speed = 7

# Marcador de puntos
score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 36)

# Efectos de sonido (puedes agregar tus propios sonidos)
# pygame.mixer.init()
# hit_sound = pygame.mixer.Sound("hit.wav")
# score_sound = pygame.mixer.Sound("score.wav")

# Bucle de juego
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)

    # Dibujar palas, pelota y línea central
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    # Dibujar marcador
    score_text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 10))

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento de las palas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += paddle_speed

    # Movimiento de la pelota
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Rebote en la parte superior e inferior
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Colisión con paletas
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] = -ball_speed[0]
        # hit_sound.play()  # Sonido al rebote

    # Reinicio si hay gol
    if ball.left <= 0:
        score2 += 1
        ball.x, ball.y = WIDTH//2, HEIGHT//2
        ball_speed = [random.choice([-5, 5]), random.choice([-5, 5])]
        paddle_speed = 7
        # score_sound.play()  # Sonido cuando se anota un gol
    if ball.right >= WIDTH:
        score1 += 1
        ball.x, ball.y = WIDTH//2, HEIGHT//2
        ball_speed = [random.choice([-5, 5]), random.choice([-5, 5])]
        paddle_speed = 7
        # score_sound.play()  # Sonido cuando se anota un gol

    # Aceleración de la pelota
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_speed[0] += 2.0  # Incrementa la velocidad en cada rebote
        paddle_speed += 2.0  # Incrementa la velocidad de las palas

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
