import pygame
a = str(input('\033[1;31;47mQual é o seu nome?'))
print('\033[1;31;47mO Ronei falou de você mesmo {}!'.format(a))
b = str(input('\033[1;31;47mQuer saber o que ele disse?'))
print('\033[1;31;47mEle disse que vai fazer pudinzinho para você no fim de semana! :)')
c = str(input('\033[1;31;47mTenho outra surpresa pra você! Quer saber? '))
print('\033[1;31;47mTE AMOOOOOOOOOOOOO!')
pygame.init()
pygame.mixer.music.load('eujuro.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
