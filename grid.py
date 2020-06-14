import math
def distance(start_point, end_point):
	x1 = start_point[0]
	x2 = end_point[0]
	y1 = start_point[1]
	y2 = end_point[1]
	
	return int(10*math.sqrt((x2-x1)**2+(y2-y1)**2))

closed =[]
visiting = []
path = []

print(distance([0,0],[1,1]))
def a_star(origin, end, grid):
	for block in grid:
		if block.coords == origin:
			block.path_weight = 0
			block.heuristic = distance(origin,end)
			visiting.append(block)
		if distance(block.coords, origin) <=14:
			block.path_weight = distance(block.coords, origin)
			block.heuristic = block.path_weight+distance(block.coords, end)
			visiting.append(block)
		else:
			closed.append(visiting[0].pop())
			path.append(closed[0])
			min_heuristic = path[0].heuristic
			for visit in visiting:
				if visit.heurisitic < min_heuristic:
					min_heuristic = visit.heuristic
					if distance(block.coords, visit) <= 14:
						block.path_weight+=visit.path_weight
						block.heuristic = block.path_weight+distance(block.coords,end)
			
			
		
			
			
		
		
		
	
	
	