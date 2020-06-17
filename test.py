import math
class Block():
	"""
	Represents each block in grid. Status will dictate start and end points.
	"""
	
	def __init__(self):
		self.coords = []
		self.status = "unvisited"
		self.color = (137,125,125)
		self.path_weight = 0
		self.heuristic = 0
	
	def set_status(self, status):
		self.status = status
	
	def set_color(self, color):
		self.color = color
		
	def set_coords(self, x, y):
		self.coords.append(x)
		self.coords.append(y)
	
	def set_path_weight(self, path_weight):
		self.path_weight = path_weight
	
	def set_heuristic(self, heuristic):
		self.heuristic = heuristic
	
	def get_heuristic(self):
		return self.heuristic
		
def distance(start_point, end_point):
	x1 = start_point[0]
	x2 = end_point[0]
	y1 = start_point[1]
	y2 = end_point[1]
	return int(10*math.sqrt((x2-x1)**2+(y2-y1)**2))/105
	
		
grid = {}
origin = [105,105]
end = [840,840]
visiting = []
closed =[]

for i in range(13):
	for j in range(20):
		b = Block()
		b.set_coords(105*i, 105*j)
		grid[(105*i,105*j)] = b


for point in grid:
	if list(point) == origin:
		grid[point].set_heuristic(distance(origin,end))
		grid[point].set_color((128,0,128))
		grid[point].set_status("visited")
		visiting.append(grid[point])

while(True):
	if any(x.coords == end for x in visiting):
		break
	
	current_coords = tuple(visiting[0].coords)
	
	for point in grid:
		if grid[point].coords[0] == current_coords[0]+105 and grid[point].coords[1] == current_coords[1]:
			if list(current_coords) == origin:
				grid[point].set_path_weight(distance(point, current_coords))
			else:
				grid[point].set_path_weight(visiting[0].path_weight+distance(point,current_coords))
			grid[point].set_heuristic(distance(point, end)+grid[point].path_weight)
			grid[point].set_status("visited")
			grid[point].set_color((128,0,128))
			visiting.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]-105 and grid[point].coords[1] == current_coords[1]:
			if list(current_coords)== origin:
				grid[point].set_path_weight(distance(point, current_coords))
			else:
				grid[point].set_path_weight(visiting[0].path_weight+distance(point,current_coords))
			grid[point].set_heuristic(distance(point, end)+grid[point].path_weight)
			grid[point].set_status("visited")
			grid[point].set_color((128,0,128))
			visiting.append(grid[point])
		elif grid[point].coords[0] == current_coords[0] and grid[point].coords[1] == current_coords[1]+105:
			if list(current_coords) == origin:
				grid[point].set_path_weight(distance(point, current_coords))
			else:
				grid[point].set_path_weight(visiting[0].path_weight+distance(point,current_coords))
			grid[point].set_heuristic(distance(point, end)+grid[point].path_weight)
			grid[point].set_status("visited")
			grid[point].set_color((128,0,128))
			visiting.append(grid[point])
		elif grid[point].coords[0] == current_coords[0] and grid[point].coords[1] == current_coords[1]-105:
			if list(current_coords) == origin:
				grid[point].set_path_weight(distance(point, current_coords))
			else:
				grid[point].set_path_weight(visiting[0].path_weight+distance(point,current_coords))
			grid[point].set_heuristic(distance(point, end)+grid[point].path_weight)
			grid[point].set_status("visited")
			grid[point].set_color((128,0,128))
			visiting.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]-105 and grid[point].coords[1] == current_coords[1]-105:
			if list(current_coords) == origin:
				grid[point].set_path_weight(distance(point, current_coords))
			else:
				grid[point].set_path_weight(visiting[0].path_weight+distance(point,current_coords))
			grid[point].set_heuristic(distance(point, end)+grid[point].path_weight)
			grid[point].set_status("visited")
			grid[point].set_color((128,0,128))
			visiting.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]+105 and grid[point].coords[1] == current_coords[1]-105:
			if list(current_coords) == origin:
				grid[point].set_path_weight(distance(point, current_coords))
			else:
				grid[point].set_path_weight(visiting[0].path_weight+distance(point,current_coords))
			grid[point].set_heuristic(distance(point, end)+grid[point].path_weight)
			grid[point].set_status("visited")
			grid[point].set_color((128,0,128))
			visiting.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]-105 and grid[point].coords[1] == current_coords[1]+105:
			if list(current_coords) == origin:
				grid[point].set_path_weight(distance(point, current_coords))
			else:
				grid[point].set_path_weight(visiting[0].path_weight+distance(point,current_coords))
			grid[point].set_heuristic(distance(point, end)+grid[point].path_weight)
			grid[point].set_status("visited")
			grid[point].set_color((128,0,128))
			visiting.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]+105 and grid[point].coords[1] == current_coords[1]+105:
			if list(current_coords) == origin:
				grid[point].set_path_weight(distance(point, current_coords))
			else:
				grid[point].set_path_weight(visiting[0].path_weight+distance(point,current_coords))
			grid[point].set_heuristic(distance(point, end)+grid[point].path_weight)
			grid[point].set_status("visited")
			grid[point].set_color((128,0,128))
			visiting.append(grid[point])
	
	visiting[0].set_color((54,43,215))
	visiting[0].set_status("closed")
	closed.append(visiting.pop(0))
	visiting.sort(key=lambda block:block.get_heuristic())
		
"""	
for i in visiting:
	print(i.status, i.coords, i.path_weight,i.get_heuristic(), distance(i.coords, end))

print("closed---------")
for i in closed:
	print(i.status, i.coords, i.path_weight, i.get_heuristic(), distance(i.coords, end))
	
"""