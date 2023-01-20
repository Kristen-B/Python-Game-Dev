import pygame
import sys
import random
import time

#Using Pygame this code is a barebones game with one player and enemy

pygame.init()

clock= pygame.time.Clock()

WIDTH = 800
HEIGHT = 600

RED = (255,0,0)
BLUE = (0,0,255)
BLACK= (0,0,0)

player_size=50;

player_pos=[WIDTH/2,HEIGHT-2*player_size];

enemy_size=50;
enemy_pos=[random.randint(0,WIDTH - enemy_size),enemy_size];
screen = pygame.display.set_mode((WIDTH,HEIGHT))

game_over = False

while not game_over: 

	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			
			x = player_pos[0]
			y = player_pos[1]
		#character moves via arrow keys
			if event.key== pygame.K_LEFT:
				x-= player_size
			elif event.key == pygame.K_RIGHT:
				x+= player_size
			player_pos = [x,y]

	# enemy falls down and resets
	if enemy_pos[1] <= HEIGHT:
		enemy_pos[1] += 10
	elif enemy_pos[1] > HEIGHT:
		enemy_pos=[random.randint(0,WIDTH - enemy_size),-enemy_size];

# if collision occours w character and enemy
	if enemy_pos[0]-enemy_size< player_pos[0] and player_pos[0] <= enemy_pos[0] + enemy_size and player_pos[1] > enemy_pos[1]- enemy_size and player_pos[1] < enemy_pos[1]+enemy_size:
		enemy_pos[1] = -enemy_size


	screen.fill(BLACK)
	pygame.draw.rect(screen, RED, (player_pos[0], player_pos[1] , player_size ,player_size))
	pygame.draw.rect(screen, BLUE, (enemy_pos[0], enemy_pos[1] , enemy_size ,enemy_size))
	clock.tick(30)
	pygame.display.update()
