import math
class Block():
	"""
	Represents each block in grid. Status will dictate start and end points.
	"""
	
	def __init__(self):
		self.coords = []
		self.status = "blank"
		self.color = (137,125,125)
		self.g_cost = 0
		self.h_cost = 0
		self.f_cost = 0
		self.point_came_from = []
	
	def set_status(self, status):
		self.status = status
	
	def set_color(self):
		if self.status == "origin":
			self.color == (128,0,128)
		if self.status == "end":
			self.color == (128,0,128)
		elif self.status == "unvisited":
			self.color = (255,255,255)
		elif self.status == "visited":
			self.color = (33,208,196)
		elif self.status == "closed":
			self.color = (208,33,33)
		elif self.status == "path":
			self.color = (57,208,33)
	
	def set_coords(self, x, y):
		self.coords.append(x)
		self.coords.append(y)
	
	def set_g_cost(self, g_cost):
		self.g_cost = g_cost
	
	def set_h_cost(self, h_cost):
		self.h_cost = h_cost

	def set_f_cost(self):
		self.f_cost = self.g_cost+self.h_cost
	
	def get_f_cost(self):
		return self.f_cost
		
def distance(start_point, end_point):
	x1 = start_point[0]
	x2 = end_point[0]
	y1 = start_point[1]
	y2 = end_point[1]
	return int(10*math.sqrt((x2-x1)**2+(y2-y1)**2))/105
	
		
grid = {}
origin = [105,105]
end = [840,840]
seen_unvisited= []
seen_visited =[]
closed = []

for i in range(13):
	for j in range(20):
		b = Block()
		b.set_coords(105*i, 105*j)
		grid[(105*i,105*j)] = b


for point in grid:
	if list(point) == origin:
		grid[point].set_h_cost(distance(origin,end))
		grid[point].set_f_cost()
		grid[point].set_status("origin")
		grid[point].set_color()
		seen_visited.append(grid[point])

while(True):
	
	current_coords = seen_visited[0].coords
	print("cur", current_coords, grid[tuple(current_coords)].get_f_cost())
	for point in grid:
		if grid[point] in zip(seen_visited,closed):
			continue
		if grid[point].coords[0] == current_coords[0]+105 and grid[point].coords[1] == current_coords[1]:
			if list(point) == end:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
				grid[point].set_h_cost(distance(point, end))
				grid[point].set_f_cost()
				grid[point].set_status("end")
				grid[point].set_color()
				grid[tuple(current_coords)].set_status("closed")
				grid[tuple(current_coords)].set_color()
				closed.append(grid[tuple(current_coords)])
				closed.append(grid[point])
				break
			elif current_coords == origin:
				grid[point].set_g_cost(distance(point, current_coords))
			else:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
			grid[point].set_h_cost(distance(point, end))
			grid[point].set_f_cost()
			grid[point].set_status("unvisited")
			grid[point].set_color()
			seen_unvisited.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]-105 and grid[point].coords[1] == current_coords[1]:
			if list(point) == end:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
				grid[point].set_h_cost(distance(point, end))
				grid[point].set_f_cost()
				grid[point].set_status("end")
				grid[point].set_color()
				grid[tuple(current_coords)].set_status("closed")
				grid[tuple(current_coords)].set_color()
				closed.append(grid[tuple(current_coords)])
				closed.append(grid[point])
				break
			elif current_coords == origin:
				grid[point].set_g_cost(distance(point, current_coords))
			else:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
			grid[point].set_h_cost(distance(point, end))
			grid[point].set_f_cost()
			grid[point].set_status("unvisited")
			grid[point].set_color()
			seen_unvisited.append(grid[point])
		elif grid[point].coords[0] == current_coords[0] and grid[point].coords[1] == current_coords[1]+105:
			if list(point) == end:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
				grid[point].set_h_cost(distance(point, end))
				grid[point].set_f_cost()
				grid[point].set_status("end")
				grid[point].set_color()
				grid[tuple(current_coords)].set_status("closed")
				grid[tuple(current_coords)].set_color()
				closed.append(grid[tuple(current_coords)])
				closed.append(grid[point])
				break
			elif current_coords == origin:
				grid[point].set_g_cost(distance(point, current_coords))
			else:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
			grid[point].set_h_cost(distance(point, end))
			grid[point].set_f_cost()
			grid[point].set_status("unvisited")
			grid[point].set_color()
			seen_unvisited.append(grid[point])
		elif grid[point].coords[0] == current_coords[0] and grid[point].coords[1] == current_coords[1]-105:
			if list(point) == end:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
				grid[point].set_h_cost(distance(point, end))
				grid[point].set_f_cost()
				grid[point].set_status("end")
				grid[point].set_color()
				grid[tuple(current_coords)].set_status("closed")
				grid[tuple(current_coords)].set_color()
				closed.append(grid[tuple(current_coords)])
				closed.append(grid[point])
				break
			elif current_coords == origin:
				grid[point].set_g_cost(distance(point, current_coords))
			else:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
			grid[point].set_h_cost(distance(point, end))
			grid[point].set_f_cost()
			grid[point].set_status("unvisited")
			grid[point].set_color()
			seen_unvisited.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]-105 and grid[point].coords[1] == current_coords[1]-105:
			if list(point) == end:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
				grid[point].set_h_cost(distance(point, end))
				grid[point].set_f_cost()
				grid[point].set_status("end")
				grid[point].set_color()
				grid[tuple(current_coords)].set_status("closed")
				grid[tuple(current_coords)].set_color()
				closed.append(grid[tuple(current_coords)])
				closed.append(grid[point])
				break
			elif current_coords == origin:
				grid[point].set_g_cost(distance(point, current_coords))
			else:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
			grid[point].set_h_cost(distance(point, end))
			grid[point].set_f_cost()
			grid[point].set_status("unvisited")
			grid[point].set_color()
			seen_unvisited.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]+105 and grid[point].coords[1] == current_coords[1]-105:
			if list(point) == end:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
				grid[point].set_h_cost(distance(point, end))
				grid[point].set_f_cost()
				grid[point].set_status("end")
				grid[point].set_color()
				grid[tuple(current_coords)].set_status("closed")
				grid[tuple(current_coords)].set_color()
				closed.append(grid[tuple(current_coords)])
				closed.append(grid[point])
				break
			elif current_coords == origin:
				grid[point].set_g_cost(distance(point, current_coords))
			else:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
			grid[point].set_h_cost(distance(point, end))
			grid[point].set_f_cost()
			grid[point].set_status("unvisited")
			grid[point].set_color()
			seen_unvisited.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]-105 and grid[point].coords[1] == current_coords[1]+105:
			if list(point) == end:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
				grid[point].set_h_cost(distance(point, end))
				grid[point].set_f_cost()
				grid[point].set_status("end")
				grid[point].set_color()
				grid[tuple(current_coords)].set_status("closed")
				grid[tuple(current_coords)].set_color()
				closed.append(grid[tuple(current_coords)])
				closed.append(grid[point])
				break
			elif current_coords == origin:
				grid[point].set_g_cost(distance(point, current_coords))
			else:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
			grid[point].set_h_cost(distance(point, end))
			grid[point].set_f_cost()
			grid[point].set_status("unvisited")
			grid[point].set_color()
			seen_unvisited.append(grid[point])
		elif grid[point].coords[0] == current_coords[0]+105 and grid[point].coords[1] == current_coords[1]+105:
			if list(point) == end:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
				grid[point].set_h_cost(distance(point, end))
				grid[point].set_f_cost()
				grid[point].set_status("end")
				grid[point].set_color()
				grid[tuple(current_coords)].set_status("closed")
				grid[tuple(current_coords)].set_color()
				closed.append(grid[tuple(current_coords)])
				closed.append(grid[point])
				break
			elif current_coords == origin:
				grid[point].set_g_cost(distance(point, current_coords))
			else:
				grid[point].set_g_cost(seen_visited[0].g_cost+distance(point,current_coords))
			grid[point].set_h_cost(distance(point, end))
			grid[point].set_f_cost()
			grid[point].set_status("unvisited")
			grid[point].set_color()
			seen_unvisited.append(grid[point])
	
	if grid[tuple(end)] in closed:
		break

	seen_visited[0].set_status("closed")
	seen_visited[0].set_color()	
	closed.append(seen_visited.pop(0))
	
	for i in seen_unvisited:
		print(i.coords, i.status)
	print("-----------sorted")
	seen_unvisited.sort(key=lambda point:point.get_f_cost())
	for i in seen_unvisited:
		print(i.coords, i.status)
	print("-----------------")
	seen_unvisited[0].set_status("visited")
	seen_unvisited[0].set_color()
	seen_visited.append(seen_unvisited.pop(0))

