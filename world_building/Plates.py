from random import randint, random

class Plate():
	def __init__(self, id, center_cell):
		self.__id = id
		self.__tiles = []	
		self.__center_cell = center_cell
		self.__col = (randint(0,255),randint(0,255),randint(0,100))
		self.__direction = (random()*100, random()*100)
		
	def get_tiles(self): return self.__tiles
	def add_tile(self, tile): self.__tiles.append(tile)

	def get_id(self): return self.__id	
	def get_col(self): return self.__col		
	def get_center_tile(self): return self.__center_cell
	def get_direction(self): return self.__direction