from PIL import Image
from Utilitary.Perlin import Perlin	
from Utilitary.Region_determination import Region_determination
from Utilitary.progressbarr import *
from Tiles import Tile
from random import randint

class World:	
	# world creation
	def __init__(self, name, size = None, smoothness = None, map = None, plates = None):
		self.__name = name

		# if a map is already given just create the world according to it
		if map != None:
			self.__size = len(map)
			self.__tiles = map
			self.__plates = plates
			self.__regions = Region_determination(self.__tiles)
		
		# if the size is defined then create a world, instead it is an already created one that is requested
		elif size != None:
			
			self.__size = size
			self.__tiles = []

			for i in progressbar(range(self.__size), "random terrain generation", 10):
				self.__tiles.append([])
				for j in range(self.__size):
					self.__tiles[i].append(Tile( randint(0,254), i, j ))
			
			for i in range(self.__size):
				for j in range(self.__size):			
					self.__tiles[i][j].recherche_voisines(self.__tiles, size)		
			
			# smooth the tiles hight
			Perlin(smoothness,self.__tiles)
			
			# find if there is different regions and mark them
			self.__regions = Region_determination(self.__tiles)

		# loading an already existing world in png format
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
		
	# saving the map	
	def save(self):	
		world_map = Image.new("RGB", (self.__size , self.__size ), "#000000")
		regions = Image.new("RGB", (self.__size , self.__size ), "#000000")
		plates = Image.new("RGB", (self.__size , self.__size ), "#000000")
		
		world_pixels = world_map.load()
		region_pixels = regions.load()
		plates_pixels = plates.load()

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
					
				plates_pixels[i, j] = self.__plates[self.__tiles[i][j].get_plate()].get_col()		

		plates.save("worlds/plates/"+self.__name+"_plates.png")
		regions.save("worlds/regions/"+self.__name+"_regions.png")
		world_map.save("worlds/worlds/"+self.__name+".png")
				
	def get_name(self): return self.__name
	def get_size(self): return self.__size
	def get_tiles(self): return self.__tiles
	def get_regions(self): return self.__regions