import pygame
import sys

class Block():
	"""
	Represents each block in grid. Status will dictate start and end points.
	"""
	
	def __init__(self):
		self.coords = []
		self.status = "unvisited"
		self.color = (137,125,125)
	
	def set_status(self, status):
		self.status = status
	
	def set_color(self, color):
		self.color = color
		
	def set_coords(self, x, y):
		self.coords.append(x)
		self.coords.append(y)

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
	
	if obstacles_set == False and obstacle_count <10:
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
				

					

			
