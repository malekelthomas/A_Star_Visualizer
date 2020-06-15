import pygame
import sys
import math

class Block():
	
	
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



def distance(start_point, end_point):
	x1 = start_point[0]
	x2 = end_point[0]
	y1 = start_point[1]
	y2 = end_point[1]
	return int(10*math.sqrt((x2-x1)**2+(y2-y1)**2))

closed =[]
visiting = []
path = []

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)


size = width, height = 250,250

screen = pygame.display.set_mode(size)
green = (50,205,50)
col = (100,20,30)

grid =[]

for i in range(width):
	for j in range(height):
		block = Block()
		block.set_coords(i,j)
		grid.append(block)


				
def drawGrid():
	for b in grid:
		pygame.draw.rect(screen, b.color, pygame.Rect(26*b.coords[0], 26*b.coords[1], 25, 25))
		print(b.color, b.status, b.coords)
	print("drawn---------------------")

x_coords = [block.coords[0] for block in grid]
y_coords = [block.coords[1] for block in grid]						
			
			
def closest_val(num, num_list):
	""" Finds the closest value in the list. The lambda function will compute the difference between the number provided and each number in the list and the min function will find the number in the list with the smallest difference.
	
	"""
	abs_diff_func = lambda list_val : abs(list_val-num)
	closest = min(num_list, key=abs_diff_func)
	return closest

def a_star(origin, end, grid):

	for block in grid:
		if block.coords == end:
				break
		if block.coords == origin:
			block.path_weight = 0
			block.heuristic = distance(origin,end)
			block.set_status("visited")
			block.set_color((128,0,128))
			visiting.append(block)
		elif distance(block.coords, origin) <=14:
			block.set_path_weight = distance(block.coords, origin)
			block.set_heuristic = block.path_weight+distance(block.coords, end)
			block.set_status("visited")
			block.set_color((128,0,128))
			visiting.append(block)
		else:
			if visiting == []:
				continue
			block.set_status("closed")
			block.set_color((54,43,215))
			closed.append(visiting.pop(0))
			path.append(closed[0])
			min_heuristic = path[0].heuristic
			for visit in visiting:
				if visit.heuristic < min_heuristic:
					min_heuristic = visit.heuristic
					if distance(block.coords, visit) <= 14:
						block.path_weight+=visit.path_weight
						block.heuristic = block.path_weight+distance(block.coords,end)
			

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
			if pygame.mouse.get_pressed()[0]:
				x_closest = closest_val(pygame.mouse.get_pos()[0], x_coords)
				y_closest = closest_val(pygame.mouse.get_pos()[1], y_coords)
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
			if pygame.mouse.get_pressed()[0]:
				x_closest = closest_val(pygame.mouse.get_pos()[0], x_coords)
				y_closest = closest_val(pygame.mouse.get_pos()[1], y_coords)
				for block in grid:
					if block.coords == [x_closest, y_closest]:
						block.set_status("end")
						block.set_color((255, 165,0))
						end_set = True
						end_coords.append(block.coords[0])
						end_coords.append(block.coords[1])
				drawGrid()
	if obstacles_set == False and obstacle_count <10:
		for event in pygame.event.get():
			if pygame.mouse.get_pressed()[0]:
				x_closest = closest_val(pygame.mouse.get_pos()[0], x_coords)
				y_closest = closest_val(pygame.mouse.get_pos()[1], y_coords)
				for block in grid:
					if block.coords == [x_closest, y_closest] and block.status != "origin" and block.status != "end" and block.status != "null":
						block.set_status("null")
						block.set_color((0,0,0))
						obstacle_count+=1
						drawGrid()
	if obstacle_count == 9:
		a_star(origin_coords, end_coords, grid)