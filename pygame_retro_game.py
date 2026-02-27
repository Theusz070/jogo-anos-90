import pygame
import random

# Inicializa o Pygame
pygame.init()

# Definir as cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Definir a tela
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Jogo Retro dos Anos 90')

# Definir o relógio para controlar a taxa de quadros
clock = pygame.time.Clock()

# Jogador
player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 5

# Inimigos
enemy_width = 50
enemy_height = 50
enemy_speed = 3
enemy_list = []

# Função para desenhar o jogador
def draw_player(x, y):
    pygame.draw.rect(screen, BLUE, [x, y, player_width, player_height])

# Função para desenhar os inimigos
def draw_enemy(x, y):
    pygame.draw.rect(screen, RED, [x, y, enemy_width, enemy_height])

# Função para gerar inimigos
def generate_enemy():
    x = random.randint(0, screen_width - enemy_width)
    y = -enemy_height
    enemy_list.append([x, y])

# Função para mover os inimigos
def move_enemies():
    global enemy_list
    for enemy in enemy_list:
        enemy[1] += enemy_speed
        if enemy[1] > screen_height:
            enemy_list.remove(enemy)

# Função para verificar colisões
def check_collision(player_x, player_y, enemy_list):
    for enemy in enemy_list:
        if player_x < enemy[0] + enemy_width and player_x + player_width > enemy[0]:
            if player_y < enemy[1] + enemy_height and player_y + player_height > enemy[1]:
                return True
    return False

# Função principal do jogo
def game_loop():
    global player_x, player_y, enemy_list
    
    game_over = False
    
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        
        # Movimento do jogador
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
            player_x += player_speed
        
        # Gerar inimigos aleatórios
        if random.randint(1, 30) == 1:
            generate_enemy()

        # Mover os inimigos
        move_enemies()

        # Verificar colisões
        if check_collision(player_x, player_y, enemy_list):
            game_over = True
        
        # Preencher a tela com a cor de fundo
        screen.fill(WHITE)

        # Desenhar o jogador
        draw_player(player_x, player_y)

        # Desenhar os inimigos
        for enemy in enemy_list:
            draw_enemy(enemy[0], enemy[1])

        # Atualizar a tela
        pygame.display.update()

        # Controlar a taxa de quadros
        clock.tick(60)

    # Fim de jogo
    pygame.quit()
    print("Game Over!")

# Iniciar o jogo
game_loop()
