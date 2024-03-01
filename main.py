import pygame
from pygame.locals import *
from Corpo_celeste import *
from sys import exit


pygame.init()

altura = 1000
largura = 1800

fps = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))

terra = CorpoCeleste((900, 500), 10000, 100, (0, 0), (0,0), 'terra.png')
#projetil = Projeteis((1000, 900), (-2,0), (0,0), 10, 5)
lua = CorpoCeleste((650, 450), 10000, 10, (0, 4), (0,0), 'lua.png')


while True:
    fps.tick(100)
    tela.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    
    terra.desenha(tela, True)

    lua.calcula_gravidade(terra)
    lua.atualiza_posicao()
    lua.desenha(tela, False)

    """projetil.atualizar_posicao(terra)
    projetil.desenha(tela)"""

    pygame.display.flip()