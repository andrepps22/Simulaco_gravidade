import pygame
from math import *

class CorpoCeleste:
    def __init__(self, posicao:tuple, massa, raio, velocidade:tuple, aceleracao:tuple, imagem):
        self.x = posicao[0]
        self.y = posicao[1]
        self.massa = massa
        self.raio = raio
        self.velocidade_x = velocidade[0]
        self.velocidade_y = velocidade[1]
        self.aceleracao_x = aceleracao[0]
        self.aceleracao_y = aceleracao[1]
        self.imagem = pygame.image.load(imagem)
        self.imagem = pygame.transform.scale(self.imagem, (2*self.raio, 2*self.raio))

    def calcula_gravidade(self, outro_corpo):


        G = 0.5 #Gravidade

        # calculo da distancia
        distancia_x = outro_corpo.x - self.x
        distancia_y = outro_corpo.y - self.y
        distancia_total = sqrt(distancia_x**2 + distancia_y**2)


        # evitando que a divisão seja por zero
        if distancia_total < 1:
           distancia_total = 1
        
        # calculo do seno e cosseno
        cosseno = distancia_x / distancia_total
        seno = distancia_y / distancia_total
        

        # F = G * ((M1 * M2) / (D * D))
        Forcagravitacional = G * ((self.massa * outro_corpo.massa) / (distancia_total ** 2))

        #Aplicando a força
        forca_x = Forcagravitacional * cosseno
        forca_y = Forcagravitacional * seno

        self.aceleracao_x = forca_x / self.massa
        self.aceleracao_y = forca_y / self.massa

        self.velocidade_x += self.aceleracao_x
        self.velocidade_y += self.aceleracao_y

        

    def atualiza_posicao(self):
        # Aplica a força à velocidade do corpo celeste
        self.x += self.velocidade_x
        self.y += self.velocidade_y

    def desenha(self, tela, centralizar:bool):
        if centralizar:
            largura_imagem, altura_imagem = self.imagem.get_size()
            centro_x = (tela.get_width() - largura_imagem) // 2
            centro_y = (tela.get_height() - altura_imagem )// 2
            
            tela.blit(self.imagem, (centro_x, centro_y))
        else:

            
            tela.blit(self.imagem, (self.x, self.y))



    
