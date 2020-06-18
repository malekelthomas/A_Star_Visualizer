import pygame
import sys
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
			self.color = (128,0,128)
		if self.status == "end":
			self.color = (128,0,128)
		elif self.status == "unvisited":
			self.color = (255,255,255)
		elif self.status == "visited":
			self.color = (33,208,196)
		elif self.status == "closed":
			self.color = (208,33,33)
		elif self.status == "path":
			self.color = (57,208,33)
		elif self.status == "null":
			self.color = (0,0,0)
	
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

def drawGrid(grid1):
	for point in grid1:
		pygame.draw.rect(screen, grid1[point].color, pygame.Rect(point[0], point[1], 100, 100))	

def closest_val(num, num_list):
	""" Finds the closest value in the list. The lambda function will compute the difference between the number provided and each number in the list and the min function will find the number in the list with the smallest difference.
	
	"""
	abs_diff_func = lambda list_val : abs(list_val-num)
	closest = min(num_list, key=abs_diff_func)
	return closest

def a_star(origin, end, grid1, visited, unvisited, checked):
	for point in grid1:
		if list(point) == origin:
			grid1[point].set_h_cost(distance(origin,end))
			grid1[point].set_f_cost()
			grid1[point].set_status("origin")
			grid1[point].set_color()
			visited.append(grid1[point])
			drawGrid(grid1)

	while(True):
		pygame.display.flip()
		current_coords = visited[0].coords
		print("cur", current_coords, grid1[tuple(current_coords)].get_f_cost())
		for point in grid1:
			if grid1[point] in zip(visited,checked) or grid1[point].status == "null":
				continue
			if grid1[point].coords[0] == current_coords[0]+105 and grid1[point].coords[1] == current_coords[1]:
				if grid1[point].status == "null":
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0]-105 and grid1[point].coords[1] == current_coords[1]:
				if grid1[point].status == "null":
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] and grid1[point].coords[1] == current_coords[1]+105:
				if grid1[point].status == "null":
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] and grid1[point].coords[1] == current_coords[1]-105:
				if grid1[point].status == "null":
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0]-105 and grid1[point].coords[1] == current_coords[1]-105:
				if grid1[point].status == "null":
					break
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0]+105 and grid1[point].coords[1] == current_coords[1]-105:
				if grid1[point].status == "null":
					break
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0]-105 and grid1[point].coords[1] == current_coords[1]+105:
				if grid1[point].status == "null":
					break
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0]+105 and grid1[point].coords[1] == current_coords[1]+105:
				if grid1[point].status == "null":
					break
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost+distance(point,current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				unvisited.append(grid1[point])
		
		if grid1[tuple(end)] in checked:
			break

		visited[0].set_status("closed")
		visited[0].set_color()	
		closed.append(visited.pop(0))
		
		for i in unvisited:
			print(i.coords, i.status)
		print("-----------sorted")
		unvisited.sort(key=lambda point:point.get_f_cost())
		for i in unvisited:
			print(i.coords, i.status)
		print("-----------------")
		unvisited[0].set_status("visited")
		unvisited[0].set_color()
		visited.append(unvisited.pop(0))

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)


size = width, height = 13,20

screen = pygame.display.set_mode(size)
green = (50,205,50)
col = (100,20,30)

grid ={}

for i in range(width):
	for j in range(height):
		b = Block()
		b.set_coords(105*i, 105*j)
		grid[(105*i,105*j)] = b


x_coords = [block[0] for block in grid]
y_coords = [block[1] for block in grid]						


seen_unvisited= []
seen_visited =[]
closed = []
shortest_path = []

drawGrid(grid)

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
				for point in grid:
					if point == (x_closest, y_closest):
						grid[point].set_status("origin")
						grid[point].set_color()
						origin_set = True
						origin_coords.append(point[0])
						origin_coords.append(point[1])
				drawGrid(grid)
	
	if end_set == False:
		for event in pygame.event.get():
			if event.type == pygame.FINGERUP:
				x_closest = closest_val(1440*event.x, x_coords)
				y_closest = closest_val(2728*event.y, y_coords)
				#x+=str(event)
				for point in grid:
					if point == (x_closest, y_closest):
						grid[point].set_status("end")
						grid[point].set_color()
						end_set= True
						end_coords.append(point[0])
						end_coords.append(point[1])
				drawGrid(grid)
	
	elif obstacles_set == False and obstacle_count <10:
		for event in pygame.event.get():
			if event.type == pygame.FINGERUP:
				x_closest = closest_val(1440*event.x, x_coords)
				y_closest = closest_val(2728*event.y, y_coords)
				for point in grid:
					if point == (x_closest, y_closest) and grid[point].status != "origin" and grid[point].status != "end" and grid[point].status != "null":
						grid[point].set_status("null")
						grid[point].set_color()
						obstacle_count+=1
						drawGrid(grid)

	else:
		a_star(origin_coords, end_coords, grid, seen_visited, seen_unvisited, closed)
		
	
				

					

			
