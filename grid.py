grid = []

for i in range(13):
	for j in range(20):
		grid.append([105*i,105*j])


abs_diff_func = lambda list_val, given_val : abs(list_val-given_val)



x_coords = [i[0] for i in grid]
y_coords = [i[1] for i in grid]

closest_val = min(x_coords, key=abs_diff_func(1))
print(closest_val)