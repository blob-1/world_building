import pygame as py
from pygame.display import set_mode
from pygame.image import load
py.init()

py.key.set_repeat(1, 50)	
	
def Game(world):
	world_map  = "worlds/worlds/"+world.get_name()+".png"
	region_map = "worlds/regions/"+world.get_name()+"_regions.png"
	plates_map = "worlds/plates/"+world.get_name()+"_plates.png"

	win = set_mode((world.get_size(), world.get_size()))

	game_ON = True
	while game_ON:

		bg = load(world_map).convert_alpha()

		win.blit(bg, (0,0))