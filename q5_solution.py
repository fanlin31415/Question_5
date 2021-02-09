
def find_placement(L, beads, output_file_name):
	#sort the beads with respect to their number
	beads.sort(key = lambda x : x[1], reverse = True)
	#initialize an empty grid
	grid = [[0]*L for i in range(L)]

	#initialize traverse counter, increment the counter when we traver the gride for the second time
	traverse_counter = 0
	#iterate until beads get empty
	while beads:
		for i in range(L):
			#iterate the grids by skip one step
			for j in range((i+traverse_counter)%2, L, 2):
				#assign one color for gird[i][j]
				grid[i][j] = beads[0][0]
				#update the remaining number of bead beads[0][0]
				beads[0] = (beads[0][0], beads[0][1]-1)
				#pop the head bead when we use it up
				if beads[0][1] == 0:
					beads.pop(0)
		#update traver counter since we just finish one iteration of gird
		traverse_counter += 1

	f_out = open(output_file_name, 'w')
	for row in grid:
		f_out.write(' '.join(row) + '\n')
	f_out.close()

	print('the total penalty is: ', str(calculate_penalty(grid)))

def calculate_penalty(grid):
	dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
	n = len(grid)

	penalty = 0

	for i in range(n):
		for j in range(n):
			for dir in dirs:
				x = i + dir[0]
				y = j + dir[1]
				#check boundary validity
				if 0 <= x <= n-1 and 0 <= y <= n-1:
					#update penalty if neighbor gird has same color
					if grid[i][j] == grid[x][y]:
						penalty += 1

	return penalty

if __name__ == '__main__':
	find_placement(3, [('R', 4), ('B', 5)], 'output_question_5_0')
	find_placement(5, [('R', 12), ('B', 13)], 'output_question_5_1')
	find_placement(
		64, 
		[('R', 139), ('B', 1451), ('G', 977), ('W', 1072), ('Y', 457)], 
		'output_question_5_2')


