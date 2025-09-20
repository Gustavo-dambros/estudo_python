#tocando mp3 no pyhon
import pygame

pygame.init()
pygame.mixer.music.load('nome do arquivo mp3')
pygame.mixer.music.play()
pygame.event.wayt()