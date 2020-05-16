class Tile():
	def __init__(self, height, pos_x, pox_y):
		self.__h = height

		if height > 129:
			self.__type = "land"
		else:
			self.__type = "water"
		self.__x = pos_x
		self.__y = pox_y
		self.__region = None
		
		self.__close_tiles = {"T":None,"TR":None,"R":None,"BR":None,"B":None,"BL":None,"L":None,"TL":None}
		
	def get_h(self): return self.__h 
	def get_x(self): return self.__x 
	def get_y(self): return self.__y 
	def get_region(self): return self.__region 
	def get_type(self) : return self.__type
	def get_close_tiles(self) : return self.__close_tiles
	
	def set_region(self, region): self.__region = region
	
	def recherche_voisines(self, tiles, i, j, max_size):
		x = 0
		y = 0
		
		# top left
		if   i != 0 and j != 0:               x = i-1;      y = j-1
		elif i == 0 and j != 0:               x = max_size; y = j-1
		elif i != 0 and j == 0:               x = i-1;      y = max_size
		else:	             	              x = max_size; y = max_size
		self.__close_tiles["TL"] = tiles[x][y]
		
		# top top
		if   i != 0:                          x = i-1;      y = j
		else:        			              x = max_size; y = j
		self.__close_tiles["T"] = tiles[x][y]

		# top right
		if   i != 0 and j != max_size:        x = i-1;      y = j+1
		elif i == 0 and j != max_size:        x = max_size; y = j+1
		elif i != 0 and j == max_size:        x = i-1;      y = 0
		else:                                 x = max_size; y = 0
		self.__close_tiles["TR"] = tiles[x][y]		
			
		# left left
		if   j != 0: 				          x = i;        y = j-1
		else:        				          x = i;        y = max_size
		self.__close_tiles["L"] = tiles[x][y]
		
		# right right
		if   j != max_size:                   x = i;        y = j+1
		else:                                 x = i;        y = 0
		self.__close_tiles["R"] = tiles[x][y]
			
		# bottom left
		if   i != max_size and j != 0:        x = i+1;      y = j-1
		elif i == 0        and j != max_size: x = i+1;      y = max_size
		elif i != 0        and j == max_size: x = 0;        y = j-1
		else:                                 x = 0;        y = max_size
		self.__close_tiles["BL"] = tiles[x][y]
			
		# bottom bottom
		if   i != max_size:                   x = i+1;      y = j
		else:               				  x = 0;        y = j
		self.__close_tiles["B"] = tiles[x][y]
			
		# bottom right
		if   i != max_size and j != max_size: x = i+1;      y = j+1
		elif i == max_size and j != max_size: x = 0;        y = j+1
		elif i != max_size and j == max_size: x = i+1;      y = 0
		else:                                 x = 0;        y = 0
		self.__close_tiles["BR"] = tiles[x][y]