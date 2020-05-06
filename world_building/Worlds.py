from PIL import Image
from Utilitary.Perlin import Perlin	
from Utilitary.Region_determination import Region_determination
from Tiles import Tile
from random import random

class World:	
	# world creation
	def __init__(self, name, size = None, smoothness = None):
		self.__name = name

		#if the size is defined then create a world, instead it is an already created one that is requested
		if size != None:
			
			self.__size = size
		
			heights = []
			for i in range(self.__size):
				heights.append([])
				for j in range(self.__size):
					heights[i].append(random())
					
			heights = Perlin(smoothness, heights)
		# loading an already existing world
		else:
			try:	
				map = Image.open("worlds/"+name+".png")
			except FileNotFoundError:
				raise
			self.__size = map.width
			map = map.load()

			heights = []
			for i in range(self.__size):
				heights.append([])
				for j in range(self.__size):
					heights[i].append(map[i,j])
		
		self.__tile_creation(heights)
			
	def __tile_creation(self, height_tab):		
		scale = Image.open("scale/scale.png")
		scale = scale.load()
		
		self.__tiles = []
		for i in range(self.__size):
			self.__tiles.append([])
			for j in range(self.__size):
				self.__tiles[i].append(Tile( height_tab[i][j], i, j ))

		self.__regions = Region_determination(self.__tiles)
		
	def save(self):	
		im = Image.new("RGB", (self.__size , self.__size ), "#000000")
		pixels = im.load()

		scale = Image.open("scale/scale.png")
		scale = scale.load()
		
		for i in range(self.__size):
			for j in range(self.__size):
				col = int(self.__tiles[i][j].get_h() * 255)
				pixels[i, j] = scale[0, col]
		
		im.save("worlds/"+self.__name+".png")
						
				
	def get_name(self): return self.__name
	def get_size(self): return self.__size
	def get_tiles(self): return self.__tiles
	def get_regions(self): return self.__regions