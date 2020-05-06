from Regions import Region

import sys
sys.setrecursionlimit(25000)

def Region_determination(tiles):
	regions = []

	id = 0
	max_size = len(tiles) - 1
	in_process = []
	
	for i in range(len(tiles)):
		for j in range(len(tiles)):
			if(tiles[i][j].get_region() == None):
				
				regions.append(Region(id, tiles[i][j].get_type()))
				
				tiles[i][j].set_region(id)
				in_process.append(tiles[i][j])

				while len(in_process) > 0:
					
					look_up_tile = in_process[0]
					regions[id].add_tile(look_up_tile)
					
					voisines = recherche_voisines(tiles, look_up_tile.get_x(), look_up_tile.get_y(), max_size)
					for voisine in voisines:
						if voisine.get_region() == None and voisine.get_type() == look_up_tile.get_type() and voisine not in in_process:
							in_process.append(voisine)
							voisine.set_region(id)
					
					in_process.pop(0)		
				
				id += 1
	
	return(regions)
	
def recherche_voisines(tiles, i, j, max_size):
	voisines = []

	if   i != 0 and j != 0: voisines.append(tiles[i-1][j-1])
	elif i == 0 and j != 0: voisines.append(tiles[max_size][j-1])
	elif i != 0 and j == 0: voisines.append(tiles[i-1][max_size])
	else:	             	voisines.append(tiles[max_size][max_size])
	
	# top top
	if   i != 0: voisines.append(tiles[i-1][j])
	else:        voisines.append(tiles[max_size][j])

	# top right
	if   i != 0 and j != max_size: voisines.append(tiles[i-1][j+1])
	elif i == 0 and j != max_size: voisines.append(tiles[max_size][j+1])
	elif i != 0 and j == max_size: voisines.append(tiles[i-1][0])
	else:                          voisines.append(tiles[max_size][0])
		
		
	# left left
	if   j != 0: voisines.append(tiles[i][j-1])
	else:        voisines.append(tiles[i][max_size])

	
	# right right
	if   j != max_size: voisines.append(tiles[i][j+1])
	else:               voisines.append(tiles[i][0])
		
	# bottom left
	if   i != max_size and j != 0:        voisines.append(tiles[i+1][j-1])
	elif i == 0        and j != max_size: voisines.append(tiles[i+1][max_size])
	elif i != 0        and j == max_size: voisines.append(tiles[0][j-1])
	else:                                 voisines.append(tiles[0][max_size])
		
	# bottom bottom
	if   i != max_size: voisines.append(tiles[i+1][j])
	else:               voisines.append(tiles[0][j])
		
	# bottom right
	if   i != max_size and j != max_size: voisines.append(tiles[i+1][j+1])
	elif i == max_size and j != max_size: voisines.append(tiles[0][j+1])
	elif i != max_size and j == max_size: voisines.append(tiles[i+1][0])
	else:                                 voisines.append(tiles[0][0])
	
	return voisines