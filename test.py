#!/usr/bin/python
#-*-coding:utf8-*-
import pygame
from pygame.locals import *
from gameobjects.vector2 import Vector2
from sys import exit
from random import randint


def main():

	background_image_path=r'./picture/sushiplate.jpg'
	sprite_image_path='./picture/fugu.png'
	SCREEN_SIZE=(640,480)
	clock=pygame.time.Clock()
	position=Vector2(100.0,100.0)
	heading=Vector2()
	speed=100

	pygame.init()

	screen = pygame.display.set_mode(SCREEN_SIZE,0,32)
	pygame.display.set_caption("hello world")
	# font=pygame.font.SysFont('arial',16)
	# font_height=font.get_linesize()

	background=pygame.image.load(background_image_path).convert()
	sprite=pygame.image.load(sprite_image_path).convert_alpha()
	destination=Vector2(randint(0,640),randint(0,480))

	while True:

		for event in pygame.event.get():
			if event.type==QUIT:
				exit()

		screen.blit(background,(0,0))
		screen.blit(sprite,position)

		time_passed=clock.tick()
		time_passed_seconds=time_passed/1000.0

		

		vector_to_mouse=Vector2.from_points(position,destination)

		if vector_to_mouse.get_length() > 1:
			heading=vector_to_mouse.normalize()
			position+=heading*time_passed_seconds*speed
		else:
			destination=Vector2(randint(0,640),randint(0,480))

		pygame.display.update()


if __name__ == '__main__':
	main()