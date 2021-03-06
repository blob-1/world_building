from Utilitary.progressbarr import *
from copy import copy

def Perlin(nb_itearions, tiles_heights):

	maps = []

	new_tiles_heights = copy(tiles_heights)
	for i in progressbar(range(nb_itearions), "Perlin Generation : ", 10):	
		pixels_number = len(tiles_heights)-1
		
		for j in range(0, pixels_number+1):
			for k in range(0, pixels_number+1):

				value = 0
				# top left
				value += tiles_heights[j][k].get_close_tiles("TL").get_h()
				# top top
				value += tiles_heights[j][k].get_close_tiles("T").get_h()
				# top right
				value += tiles_heights[j][k].get_close_tiles("TR").get_h()					
				# left left
				value += tiles_heights[j][k].get_close_tiles("L").get_h()
				# self count
				value += tiles_heights[j][k].get_h()
				# right right
				value += tiles_heights[j][k].get_close_tiles("R").get_h()
				# bottom left
				value += tiles_heights[j][k].get_close_tiles("BL").get_h()
				# bottom bottom
				value += tiles_heights[j][k].get_close_tiles("B").get_h()
				# bottom right
				value += tiles_heights[j][k].get_close_tiles("BR").get_h()

				new_tiles_heights[j][k].set_h(value/9)
	
		maps.append(new_tiles_heights)
	
	for i in range(0, pixels_number+1):
			for j in range(0, pixels_number+1):
				value = 0
				cpt = 0
				for map in maps:
					cpt += 1
					value += map[i][j].get_h()*(1/(2**cpt))
					
				value += tiles_heights[i][j].get_h()*(1/(2**cpt))
				
				tiles_heights[i][j].set_h(value)
		
	return tiles_heights