class Tile():
	def __init__(self, height, pos_x, pox_y):
		self.__h = height

		if height > 0.5:
			self.__type = "land"
		else:
			self.__type = "water"
		self.__x = pos_x
		self.__y = pox_y
		self.__region = None
		
	def get_h(self): return self.__h 
	def get_x(self): return self.__x 
	def get_y(self): return self.__y 
	def get_region(self): return self.__region 
	def get_type(self) : return self.__type
	
	def set_region(self, region): self.__region = region