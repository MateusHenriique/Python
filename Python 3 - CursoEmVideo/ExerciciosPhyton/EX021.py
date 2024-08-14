import pygame

pygame.init()
pygame.mixer.music.load('Python 3 - CursoEmVideo/ExerciciosPhyton/EX021.mp3')
pygame.mixer.music.play()
x = input ('parar')
pygame.mixer.stop(x)