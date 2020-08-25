import pygame as py
from pygame.display import set_mode
from pygame.image import load
py.init()

py.key.set_repeat(1, 50)	
	
class Game():
	def __init__(self, world):
		infoObject = py.display.Info()
		self.__w, self.__h = infoObject.current_w, infoObject.current_h
		
		self.__win = set_mode((self.__w, self.__h))
		
		self.__world_map  = load("worlds/worlds/" +world.get_name()+".png"         ).convert_alpha()
		self.__region_map = load("worlds/regions/"+world.get_name()+"_regions.png" ).convert_alpha()
		self.__plates_map = load("worlds/plates/" +world.get_name()+"_plates.png"  ).convert_alpha()

		self.__bg = py.Surface((self.__w,self.__h))
		py.transform.scale(self.__world_map, (self.__w, self.__h), self.__bg)

	def run(self):
		game_ON = True
		while game_ON:

			evenements = py.event.get()
			for event in evenements:
				# To quit push esc
				if event.type == py.QUIT or (\
				   event.type == py.KEYDOWN and event.key == py.K_ESCAPE\
				):
					game_ON = False

				if event.type == py.KEYDOWN and event.key == py.K_p:
					self.change_bg(self.__plates_map)
					
				if event.type == py.KEYDOWN and event.key == py.K_r:
					self.change_bg(self.__region_map)

				if event.type == py.KEYDOWN and event.key == py.K_w:
					self.change_bg(self.__world_map)

			self.__win.blit(self.__bg, (0,0))
			
			py.display.flip()
			
	def change_bg(self, new_bg):
		py.transform.scale(new_bg, (self.__w, self.__h), self.__bg)