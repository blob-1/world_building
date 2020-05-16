from Utilitary.progressbarr import *

def Perlin(nb_itearions, drawing_zonnes):

	for i in progressbar(range(nb_itearions), "Perlin Generation : ", 10):
		
		pixels_number = len(drawing_zonnes)-1

		new_drawing_zonnes = drawing_zonnes
		
		for i in range(0, pixels_number+1):
			for j in range(0, pixels_number+1):

				value = 0
				# top left
				if   i != 0 and j != 0: value += drawing_zonnes[i-1][j-1]
				elif i == 0 and j != 0: value += drawing_zonnes[pixels_number][j-1]
				elif i != 0 and j == 0: value += drawing_zonnes[i-1][pixels_number]
				else:					value += drawing_zonnes[pixels_number][pixels_number]
	
				# top top
				if   i != 0: value += drawing_zonnes[i-1][j]
				else:        value += drawing_zonnes[pixels_number][j]

				# top right
				if   i != 0 and j != pixels_number: value += drawing_zonnes[i-1][j+1]
				elif i == 0 and j != pixels_number: value += drawing_zonnes[pixels_number][j+1]
				elif i != 0 and j == pixels_number: value += drawing_zonnes[i-1][0]
				else:                               value += drawing_zonnes[pixels_number][0]
					
		
				# left left
				if   j != 0: value += drawing_zonnes[i][j-1]
				else:        value += drawing_zonnes[i][pixels_number]
					
				# self count
				value += drawing_zonnes[i][j]
				
				# right right
				if   j != pixels_number: value += drawing_zonnes[i][j+1]
				else:                    value += drawing_zonnes[i][0]
					
				# bottom left
				if   i != pixels_number and j != 0:             value += drawing_zonnes[i+1][j-1]
				elif i == 0             and j != pixels_number: value += drawing_zonnes[i+1][pixels_number]
				elif i != 0             and j == pixels_number: value += drawing_zonnes[0][j-1]
				else:                                           value += drawing_zonnes[0][pixels_number]
								
				# bottom bottom
				if   i != pixels_number: value += drawing_zonnes[i+1][j]
				else:                    value += drawing_zonnes[0][j]
					
				# bottom right
				if   i != pixels_number and j != pixels_number: value += drawing_zonnes[i+1][j+1]
				elif i == pixels_number and j != pixels_number: value += drawing_zonnes[0][j+1]
				elif i != pixels_number and j == pixels_number: value += drawing_zonnes[i+1][0]
				else:                                           value += drawing_zonnes[0][0]

				new_drawing_zonnes[i][j] = value/9
	
		drawing_zonnes = new_drawing_zonnes
		
	return drawing_zonnes