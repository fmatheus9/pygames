import pygame

pygame.init() #inicia o pygame

score1 = 0
score1_img = pygame.image.load("assets/score/0.png")
score2 = 0
score2_img = pygame.image.load("assets/score/0.png")
win = pygame.image.load("assets/win.png")

window = pygame.display.set_mode([1280, 720]) #acessa o display, tela, e define suas dimensões 
title = pygame.display.set_caption("Futeball Pong") #adiciona um título ao display

field = pygame.image.load("assets/field.png") #adiciona uma imagem 

player1 = pygame.image.load("assets/player1.png") 
player1_y = 310 #define a posição do player1
player1_moveup = False 
player1_movedown = False

player2 = pygame.image.load("assets/player2.png")
player2_y = 310

ball = pygame.image.load("assets/ball.png")
ball_x = 617 #define posição da bola
ball_y = 337
ball_dir = -4 #controla a direção, e tambem a velocidade
ball_dir_y = 1


#move o player
def move_player():
    #chama as variáveis para a função
    global player1_y

    if player1_moveup:
        player1_y -= 3
    else:
        player1_y += 0

    if player1_movedown:
        player1_y += 3
    else:
        player1_y += 0
    #define limite de movimentação
    if player1_y <= 0:
        player1_y = 0
    elif player1_y >= 575:
        player1_y = 575

def move_player2():
    global player2_y
    player2_y = ball_y

    if player2_y <= 0:
        player2_y = 0
    elif player2_y >= 575:
        player2_y = 575

#move a bola  
def move_ball():
    #chama as variáveis para a função
    global score1
    global score2
    global score1_img
    global score2_img
    global ball_x
    global ball_y
    global ball_dir
    global ball_dir_y

    ball_x += ball_dir
    ball_y += ball_dir_y

    #colisão em relação ao player 1
    if ball_x < 120: #se a posição da bola no eixo x, proximo ao jogador, as condições são verificadas: 
        if player1_y < ball_y + 23: #se a posição em relação ao eixo y do jogador for menor que a posição do eixo y da bolinha mais metade do tamanho dela
            if player1_y + 146 > ball_y: #se a posição em relação ao eixo y do jogador + 146 for maior que a posição do eixo y da bolinha
                ball_dir *= -1 #faz a colisão
    #colisão em relação ao player 2
    if ball_x > 1110:
        if player2_y < ball_y + 23:
            if player2_y + 146 > ball_y:
                ball_dir *= -1
    
    #definir limite 
    if ball_y >= 685:
        ball_dir_y *= -1
    elif ball_y <= 0:
        ball_dir_y *= -1

    #reiniciando a posição da bola
    if ball_x < -10: 
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score2 += 1
        score2_img = pygame.image.load("assets/score/" + str(score2) + ".png")

    elif ball_x > 1290:
        ball_x = 617
        ball_y = 337
        ball_dir_y *= -1
        ball_dir *= -1
        score1 += 1
        score1_img = pygame.image.load("assets/score/" + str(score1) + ".png")

def draw(): #faz com que as imagens sejam desenhadas na tela. 
    if score1 or score2 < 9:
        window.blit(field, (0, 0))
        window.blit(player1, (50, player1_y))
        window.blit(player2, (1150, player2_y))
        window.blit(ball, (ball_x, ball_y))
        window.blit(score1_img, (500, 50))
        window.blit(score2_img, (710, 50))
        move_ball()
        move_player()
        move_player2()
    else:
        window.blit(win, (300, 330))    


loop = True #para que o jogo fique aberto ele precisa estar dentro de um loop
while loop:
    for events in pygame.event.get(): #para cada evento realizado: 
        if events.type == pygame.QUIT: #encerra o loop
            loop = False
        if events.type == pygame.KEYDOWN: #se uma tecla for pressionada
            if events.key == pygame.K_w:
                player1_moveup = True
            if events.key == pygame.K_s:
                player1_movedown = True
        if events.type == pygame.KEYUP: #se a tecla for solta
            if events.key == pygame.K_w:
                player1_moveup = False
            if events.key == pygame.K_s:
                player1_movedown = False

    draw()
    pygame.display.update() #impede a janela de fechar pois a atualiza sempre
