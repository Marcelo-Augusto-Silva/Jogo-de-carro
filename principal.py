import pygame
from random import randint

pygame.init()
x = 260  # 140min        #380 max
# 260
y = 50
pos_x = 140
pos_y = 800
pos_y_a = 1000
pos_y_c = 1500
timer = 0
tempo_segundos = 0

velocidade = 15
velocidade_outros_carros = 15
fundo = pygame.image.load('pista.png')
carro = pygame.image.load('bugatti (4).png')
carro1 = pygame.image.load('bugatti (3).png')
carro3 = pygame.image.load('bugatti (2).png')
carro4 = pygame.image.load('bugatti (1).png')

fonte = pygame.font.SysFont('arial black', 20)
texto = fonte.render('Tempo : ', True, (255, 255, 255), (0, 0, 0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 40)

tamanho_janela = pygame.display.set_mode((600, 600))
pygame.display.set_caption('CRIANDO UM JOGO')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    # if comandos[pygame.K_UP]:
    # y -= velocidade
    # if comandos[pygame.K_DOWN]:
    # y += velocidade
    if comandos[pygame.K_LEFT] and x >= 140:
        x -= velocidade
    if comandos[pygame.K_RIGHT] and x <= 369:
        x += velocidade

    # if x +90 > pos_x and y -  > pos_y_a:
    #   y = 1200
    if x + 88 > pos_x + 235 and y +174 > pos_y_a:
        if pos_y_a > 0:
            y = 1200
    if x - 88 < pos_x  and y + 174 > pos_y:
        if pos_y > 0:
            y = 1200
    #if (x + 88 == pos_x + 120 and y + 174 > pos_y_c):
    if (x -88 < pos_x +120  and x > 260 and y +174 > pos_y_c) or (x + 88 > pos_x+ 120 and x < 260 and y + 174 > pos_y_c):

        if pos_y_c > 0 :
            y = 1200




    if pos_y <= -400 :
        pos_y = randint(1800, 2000)

    if pos_y_a <= -400:
        pos_y_a = randint(1200, 1600)

    if pos_y_c <= -400:
        pos_y_c = randint(790, 1000)

    if timer < 20:
        timer += 1
    else:
        tempo_segundos += 1
        texto = fonte.render('Tempo : ' + str(tempo_segundos), True, (255, 255, 255), (0, 0, 0))
        timer = 0

    pos_y -= velocidade_outros_carros + 15
    pos_y_a -= velocidade_outros_carros + 10
    pos_y_c -= velocidade_outros_carros + 20

    tamanho_janela.blit(fundo, (0, 0))
    tamanho_janela.blit(carro, (x, y))
    tamanho_janela.blit(carro1, (pos_x, pos_y))
    tamanho_janela.blit(carro3, (pos_x + 235, pos_y_a))
    tamanho_janela.blit(carro4, (pos_x + 120, pos_y_c))
    tamanho_janela.blit(texto, pos_texto)
    pygame.display.update()
pygame.quit()
