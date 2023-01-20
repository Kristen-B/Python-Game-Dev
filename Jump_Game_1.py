import pygame as g
import sys
import time

g.init()
clock= g.time.Clock()

WIDTH = 800; HEIGHT = 600; screen = g.display.set_mode((WIDTH,HEIGHT))
player_size=50;player_pos=[WIDTH/2,HEIGHT-2*player_size];

jump=False
game_over = False

while not game_over: 

	for event in g.event.get():

		if event.type == g.QUIT:
			sys.exit()
		if event.type == g.KEYDOWN:
			if event.key== g.K_SPACE:
				jump=True
				increment = 0

	
	if(jump == True):
		player_pos[1]=player_pos[1]-10+increment
		increment +=1


	screen.fill((0,0,0))
	g.draw.rect(screen, (0,0,255),(player_pos[0], player_pos[1] , player_size ,player_size))
	clock.tick(30)
	g.display.update()
