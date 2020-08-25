from Tiles import *
from Worlds import World
from Plates import Plate
from Utilitary.Plate_determination import *
from random import randint

class generating_procedure():
	def __init__(self, size, nb_plates):
		self.__size = size
		self.__tiles = []
		
		# create each individual tile
		for i in range(self.__size):
			self.__tiles.append([])
			for j in range(self.__size):
				self.__tiles[i].append(Tile( 127, i, j))
				
		# define center points for each tectonic Plate
		self.__Plates = []
		CenterPoints = []
		cpt = 0
		for i in range(nb_plates):
			while True:
				newcenter = self.__tiles[randint(0,size-1)][randint(0,size-1)]
				if newcenter not in CenterPoints:
					CenterPoints.append(newcenter)
					self.__Plates.append(Plate(cpt, newcenter))
					cpt += 1
					break	

		# assign a plate to each cell 
		Plate_determination(self.__tiles, self.__Plates)
	
	def get_map(self): return self.__tiles
	def get_plates(self): return self.__Plates