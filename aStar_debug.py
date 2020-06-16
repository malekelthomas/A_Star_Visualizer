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
	
end = [12,25]

points = [[0,0],[2,5],[12,20],[11,25]]

blocks =[]
for i in points:
	b = Block()
	b.coords = i
	b.set_heuristic(distance(i, end))
	blocks.append(b)
	

blocks.sort(key=lambda block: block.get_heuristic())	


grid =[]

for i in range(13):
	for j in range(20):
		block = Block()
		block.set_coords(105*i,105*j)
		grid.append(block)

origin = [0,105]

end = [840,840]
visiting = []
closed = []

for point in grid:
	if point.coords == origin:
		point.set_heuristic(distance(origin,end))
		point.set_color((128,0,128))
		point.set_status("visited")
		visiting.append(point)

while(True):
		if any(x.coords == end for x in visiting):
			for i in visiting:
				print(i.coords, distance(i.coords, end))
			break
		for point in grid:
			if distance(point.coords, visiting[0].coords) == 10 or distance(point.coords, visiting[0].coords) == 14:
					if point in visiting:
						break
					
					point.set_path_weight(point.path_weight+distance(point.coords, visiting[0].coords))
					point.set_heuristic(distance(point.coords, end)+point.path_weight)
					point.set_status("visited")
					point.set_color((128,0,128))
					visiting.append(point)
						
		visiting[0].set_color((54,43,215))
		closed.append(visiting.pop(0))
		visiting.sort(key=lambda block: block.get_heuristic())
					

			