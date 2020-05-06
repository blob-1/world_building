from random import randint

class Region():
	def __init__(self, id, type):
		self.__id = id
		self.__tiles = []	
		self.__type = type
		self.__col = (randint(0,255),randint(0,255),randint(0,100))
		
		
	def get_tiles(self): return self.__tiles
	def add_tile(self, tile): self.__tiles.append(tile)

	def get_id(self): return self.__id	
	def get_col(self): return self.__col	