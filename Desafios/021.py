#ou
#import playsound
#playsound.playsound('python/Desafios/02.mp3')

import pygame
pygame.mixer.init()
pygame.mixer.music.load('python/Desafios/02.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
#Com isso, você consegue digitar o nome do arquivo e tocar ele(contanto que ele esteja contido na pasta do seu código!)
#fica a dica!