import pygame
import sys
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

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)


size = width, height = 13,20

screen = pygame.display.set_mode(size)
green = (50,205,50)
col = (100,20,30)

grid =[]

for i in range(width):
	for j in range(height):
		block = Block()
		block.set_coords(105*i,105*j)
		grid.append(block)


				
def drawGrid():
	for b in grid:
		pygame.draw.rect(screen, b.color, pygame.Rect(b.coords[0], b.coords[1], 100, 100))

x_coords = [block.coords[0] for block in grid]
y_coords = [block.coords[1] for block in grid]						
			
			
def closest_val(num, num_list):
	""" Finds the closest value in the list. The lambda function will compute the difference between the number provided and each number in the list and the min function will find the number in the list with the smallest difference.
	
	"""
	abs_diff_func = lambda list_val : abs(list_val-num)
	closest = min(num_list, key=abs_diff_func)
	return closest
	
def distance(start_point, end_point):
	x1 = start_point[0]
	x2 = end_point[0]
	y1 = start_point[1]
	y2 = end_point[1]
	return int(10*math.sqrt((x2-x1)**2+(y2-y1)**2))/105		
closed =[]
visiting = []
path = []

def a_star(origin, end, grid1):
	for point in grid:
		if point.coords == origin:
			point.set_heuristic(distance(origin,end))
			point.set_color((128,0,128))
			point.set_status("visited")
			visiting.append(point)
			drawGrid()
			
	while(True):
			if any(x.coords == end for x in visiting):
				break
			for point in grid1:
				if distance(point.coords, visiting[0].coords) == 10 or distance(point.coords, visiting[0].coords) == 14:
					if point in visiting:
						break
					if point.status == "null":
						break
					point.set_path_weight(point.path_weight+distance(point.coords, visiting[0].coords))
					point.set_heuristic(distance(point.coords, end)+point.path_weight)
					point.set_status("visited")
					point.set_color((0,16,128))
					visiting.append(point)
					drawGrid()
				
			visiting[0].set_color((54,43,215))
			closed.append(visiting.pop(0))
			drawGrid()
			visiting.sort(key=lambda block: block.get_heuristic())
					
			
drawGrid()

origin_set = False
end_set = False
obstacles_set = False
done = False
obstacle_count=0
origin_coords =[]
end_coords = []

while True:
	pygame.display.flip()
	
	if origin_set == False:
		for event in pygame.event.get():
			if event.type == pygame.FINGERUP:
				x_closest = closest_val(1440*event.x, x_coords)
				y_closest = closest_val(2728*event.y, y_coords)
				#x+=str(event)
				for block in grid:
					if block.coords == [x_closest, y_closest]:
						block.set_status("origin")
						block.set_color((255, 255,0))
						origin_set = True
						origin_coords.append(block.coords[0])
						origin_coords.append(block.coords[1])
				drawGrid()
	
	if end_set == False:
		for event in pygame.event.get():
			if event.type == pygame.FINGERUP:
				x_closest = closest_val(1440*event.x, x_coords)
				y_closest = closest_val(2728*event.y, y_coords)
				#x+=str(event)
				for block in grid:
					if block.coords == [x_closest, y_closest]:
						block.set_status("end")
						block.set_color((255, 165,0))
						end_set = True
						end_coords.append(block.coords[0])
						end_coords.append(block.coords[1])
				drawGrid()
	
	elif obstacles_set == False and obstacle_count <10:
		for event in pygame.event.get():
			if event.type == pygame.FINGERUP:
				x_closest = closest_val(1440*event.x, x_coords)
				y_closest = closest_val(2728*event.y, y_coords)
				for block in grid:
					if block.coords == [x_closest, y_closest] and block.status != "origin" and block.status != "end" and block.status != "null":
						block.set_status("null")
						block.set_color((0,0,0))
						obstacle_count+=1
				drawGrid()
	else:
		a_star(origin_coords, end_coords, grid)
		for i in closed:
			i.set_color((0,128,0)) 
	
				

					

			
