from PIL import Image
from Utilitary.Perlin import Perlin	
from Utilitary.Region_determination import Region_determination
from Utilitary.progressbarr import *
from Tiles import Tile
from random import randint

class World:	
	# world creation
	def __init__(self, name, size = None, smoothness = None):
		self.__name = name

		#if the size is defined then create a world, instead it is an already created one that is requested
		if size != None:
			
			self.__size = size
			self.__tiles = []

			for i in progressbar(range(self.__size), "random terrain generation", 10):
				self.__tiles.append([])
				for j in range(self.__size):
					self.__tiles[i].append(Tile( randint(0,255), i, j ))
			
			for i in range(self.__size):
				for j in range(self.__size):			
					self.__tiles[i][j].recherche_voisines(self.__tiles, size-1)		
			
			# smooth the tiles hight
			self.__tiles = Perlin(smoothness,self.__tiles)
			# find if there is different regions and mark them
			self.__regions = Region_determination(self.__tiles)

		# loading an already existing world
		else:
			try:	
				map = Image.open("worlds/"+name+".png")
			except FileNotFoundError:
				raise
			self.__size = map.width
			map = map.load()

			heights = []
			for i in progressbar(range(self.__size), "loading of each tiles", 10):
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
		world_map = Image.new("RGB", (self.__size , self.__size ), "#000000")
		regions = Image.new("RGB", (self.__size , self.__size ), "#000000")
		
		world_pixels = world_map.load()
		region_pixels = regions.load()

		scale = Image.open("scale/scale.png")
		scale = scale.load()
		
		for i in range(self.__size):
			for j in range(self.__size):
				col = self.__tiles[i][j].get_h()
				world_pixels[i, j] = scale[0, col]
				
				# color the regions if you are in land
				if self.__tiles[i][j].get_type() == "land" :
					region_pixels[i, j] = self.__regions[self.__tiles[i][j].get_region()].get_col()
				else:
					region_pixels[i, j] = scale[0, col]	

		regions.save("worlds/"+self.__name+"_regions.png")
		world_map.save("worlds/"+self.__name+".png")
						
						
				
	def get_name(self): return self.__name
	def get_size(self): return self.__size
	def get_tiles(self): return self.__tiles
	def get_regions(self): return self.__regions