# Programa para abrir e reproduzir áudio em mp3.
import pygame
pygame.init()
pygame.mixer.music.load('01.mp3')
pygame.mixer.music.play()
pygame.event.wait()
