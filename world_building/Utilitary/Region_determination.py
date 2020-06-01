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
			tiles[i][j].recherche_voisines(tiles, max_size)
	
	for i in range(len(tiles)):
		for j in range(len(tiles)):
			
			if(tiles[i][j].get_region() == None):
				
				regions.append(Region(id, tiles[i][j].get_type()))
				
				tiles[i][j].set_region(id)
				in_process.append(tiles[i][j])

				while len(in_process) > 0:
					
					look_up_tile = in_process[0]
					regions[id].add_tile(look_up_tile)
					
					for voisine in look_up_tile.get_close_tiles().values():
						if voisine.get_region() == None and voisine.get_type() == look_up_tile.get_type() and voisine not in in_process:
							in_process.append(voisine)
							voisine.set_region(id)
					
					in_process.pop(0)		
				
				id += 1
	
	return(regions)