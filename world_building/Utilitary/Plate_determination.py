def Plate_determination(tiles, Plates):
	id = 0
	size = len(tiles)

	for l in tiles:
		for tile in l:

			tile.recherche_voisines(tiles, size)
			
			min_dist = float("inf")
			
			for p in Plates:
	
				dx = abs(tile.get_x() - p.get_center_tile().get_x())
				dy = abs(tile.get_y() - p.get_center_tile().get_y())
				
				if dx > size/2:
					dx = size - dx
				if dy > size/2:
					dy = size - dy
				
				dist = dx**2 + dy**2

				if min_dist > dist:
					tile.set_plate(p.get_id())
					min_dist = dist
	
			Plates[tile.get_plate()].add_tile(tile)
	
	return(Plates)