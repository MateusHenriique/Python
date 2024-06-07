import pygame
pygame.init()
pygame.mixer.music.load('Python/ExerciciosPhyton/EX021.mp3')
pygame.mixer.music.play()
X = input ('parar')
pygame.mixer.stop(X)
