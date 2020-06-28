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
		self.color = (100, 125, 125)
		self.g_cost = 0
		self.h_cost = 0
		self.f_cost = 0
		self.point_came_from = ()

	def set_status(self, status):
		self.status = status

	def set_color(self):
		if self.status == "origin":
			self.color = (128, 0, 128)
		if self.status == "end":
			self.color = (128, 0, 128)
		elif self.status == "unvisited":
			self.color = (255, 255, 255)
		elif self.status == "visited":
			self.color = (33, 208, 196)
		elif self.status == "closed":
			self.color = (208, 33, 33)
		elif self.status == "path":
			self.color = (57, 208, 33)
		elif self.status == "null":
			self.color = (0, 0, 0)

	def set_coords(self, x, y):
		self.coords.append(x)
		self.coords.append(y)

	def set_g_cost(self, g_cost):
		self.g_cost = g_cost

	def set_h_cost(self, h_cost):
		self.h_cost = h_cost

	def set_f_cost(self):
		self.f_cost = self.g_cost + self.h_cost

	def set_pcf(self, x, y):
		self.point_came_from = (x, y)

	def get_f_cost(self):
		return self.f_cost



def distance(start_point, end_point):
	x1 = start_point[0]
	x2 = end_point[0]
	y1 = start_point[1]
	y2 = end_point[1]
	return int(10*math.sqrt((x2-x1)**2+(y2-y1)**2))


def closest_val(num, num_list):
	""" Finds the closest value in the list. The lambda function will compute the difference between the number provided and each number in the list and the min function will find the number in the list with the smallest difference.

	"""
	abs_diff_func = lambda list_val: abs(list_val - num)
	closest = min(num_list, key=abs_diff_func)
	return closest

width = 20
height = 20
margin = 1
full_width= width+ margin
full_height = height + margin
def drawGrid(grid1, display):
	for point in grid1:
		pygame.draw.rect(display, grid1[point].color, pygame.Rect((full_width)*point[0] + margin, (full_height)*point[1] + margin, width, height),margin)

def a_star(origin, end, grid1, visited, unvisited, checked, surface):
	for point in grid1:
		if list(point) == origin:
			grid1[point].set_h_cost(distance(origin, end))
			grid1[point].set_f_cost()
			grid1[point].set_status("origin")
			grid1[point].set_color()
			visited.append(grid1[point])
			drawGrid(grid1, surface)

	while (True):
		pygame.display.flip()
		current_coords = visited[0].coords
		#print("cur", current_coords, grid1[tuple(current_coords)].get_f_cost())
		for point in grid1:
			if grid1[point] in zip(visited, checked) or grid1[point].status == "null":
				continue
			if grid1[point].coords[0] == current_coords[0] + 1 and grid1[point].coords[1] == current_coords[1]:
				if grid1[point] in zip(visited, checked):
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1, surface)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				drawGrid(grid1, surface)
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] - 1 and grid1[point].coords[1] == current_coords[1]:
				if grid1[point] in zip(visited, checked):
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1, surface)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				drawGrid(grid1, surface)
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] and grid1[point].coords[1] == current_coords[1] + 1:
				if grid1[point] in zip(visited, checked):
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1, surface)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				drawGrid(grid1, surface)
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] and grid1[point].coords[1] == current_coords[1] - 1:
				if grid1[point] in zip(visited, checked):
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1, surface)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				drawGrid(grid1, surface)
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] - 1 and grid1[point].coords[1] == current_coords[1] - 1:
				if grid1[point].status == "null":
					break
				if grid1[point] in zip(visited, checked):
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1, surface)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				drawGrid(grid1, surface)
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] + 1 and grid1[point].coords[1] == current_coords[1] - 1:
				if grid1[point].status == "null":
					break
				if grid1[point] in zip(visited, checked):
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1, surface)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				drawGrid(grid1, surface)
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] - 1 and grid1[point].coords[1] == current_coords[1] + 1:
				if grid1[point].status == "null":
					break
				if grid1[point] in zip(visited, checked):
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1, surface)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				drawGrid(grid1, surface)
				unvisited.append(grid1[point])
			elif grid1[point].coords[0] == current_coords[0] + 1 and grid1[point].coords[1] == current_coords[1] + 1:
				if grid1[point].status == "null":
					break
				if grid1[point] in zip(visited, checked):
					continue
				if list(point) == end:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
					grid1[point].set_h_cost(distance(point, end))
					grid1[point].set_f_cost()
					grid1[point].set_status("end")
					grid1[point].set_color()
					grid1[tuple(current_coords)].set_status("closed")
					grid1[tuple(current_coords)].set_color()
					checked.append(grid1[tuple(current_coords)])
					checked.append(grid1[point])
					drawGrid(grid1, surface)
					pygame.display.flip()
					break
				elif current_coords == origin:
					grid1[point].set_g_cost(distance(point, current_coords))
				else:
					grid1[point].set_g_cost(visited[0].g_cost + distance(point, current_coords))
				grid1[point].set_h_cost(distance(point, end))
				grid1[point].set_f_cost()
				grid1[point].set_status("unvisited")
				grid1[point].set_color()
				drawGrid(grid1, surface)
				unvisited.append(grid1[point])

		if grid1[tuple(end)] in checked:
			break

		visited[0].set_status("closed")
		visited[0].set_color()
		drawGrid(grid1, surface)
		if len(closed) != 0:
			visited[0].set_pcf(checked[-1].coords[0],checked[-1].coords[1])  # last element in closed/prev current point
		checked.append(visited.pop(0))
		print(origin, end)
		for i in checked:
			print(i.coords, i.status)

		"""for i in unvisited:
			print(i.coords, i.status)
		print("-----------sorted")"""

		unvisited.sort(key=lambda point: point.get_f_cost())
		"""
		for i in unvisited:
			print(i.coords, i.status)
		print("-----------------")
		"""
		unvisited[0].set_status("visited")
		unvisited[0].set_color()
		drawGrid(grid1, surface)
		visited.append(unvisited.pop(0))

	point = tuple(checked[-1].coords)
	while (point != ()):
		pygame.display.flip()
		grid1[point].set_status("path")
		grid1[point].set_color()
		drawGrid(grid1, surface)
		point = tuple(grid[point].point_came_from)

closed =[]
visiting = []
path = []

pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 100)


size = width, height = 400,400

screen = pygame.display.set_mode(size)
screen2 = pygame.display.set_mode(size)
green = (50,205,50)
col = (100,20,30)
screen.fill((200,200,200))
grid ={}

blocksize = 20
for i in range(width//blocksize):
	for j in range(height//blocksize):
		b = Block()
		b.set_coords(i, j)
		grid[(i,j)] = b


x_coords = [block[0] for block in grid]
y_coords = [block[1] for block in grid]
			
			

drawGrid(grid, screen)
pygame.display.flip()
seen_unvisited= []
seen_visited =[]
closed = []
shortest_path = []

origin_set = False
end_set = False
obstacles_set = False
done = False
obstacle_count=0
origin_coords =[]
end_coords = []
i = 3
while True:
	if origin_set == False:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				x_closest = pos[0] // 21#converting mouse pos to grid, div by width or height + margin
				y_closest = pos[1] // 21
				print("Click: ", pos, "Grid: ", x_closest, y_closest)
				for point in grid:
					if point == (x_closest, y_closest):
						grid[point].set_status("origin")
						grid[point].set_color()
						origin_set = True
						origin_coords.append(point[0])
						origin_coords.append(point[1])
				drawGrid(grid, screen)
				pygame.display.flip()
	
	if end_set == False:
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				x_closest = pos[0] // 21
				y_closest = pos[1] // 21
				print("Click2: ", pos, "Grid: ", x_closest, y_closest)
				for point in grid:
					if point == (x_closest, y_closest):
						grid[point].set_status("end")
						grid[point].set_color()
						end_set = True
						end_coords.append(point[0])
						end_coords.append(point[1])
				drawGrid(grid, screen)
				pygame.display.flip()
	elif obstacles_set == False and obstacle_count < 10:

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				x_closest = pos[0] // 21
				y_closest = pos[1] // 21
				print("Click"+str(i)+": ", pos, "Grid: ", x_closest, y_closest)
				for point in grid:
					if point == (x_closest, y_closest) and grid[point].status != "origin" and grid[
						point].status != "end" and grid[point].status != "null":
						grid[point].set_status("null")
						grid[point].set_color()
						obstacle_count += 1
				drawGrid(grid, screen)
				i+=1
				pygame.display.flip()
	else:
		a_star(origin_coords, end_coords, grid, seen_visited, seen_unvisited, closed, screen)