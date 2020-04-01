import sys
import random
import math

def make_sudoku(n):
	if n == 1:
		return [[1]]
	matrix = [[((i*n + i/n + j) % (n*n) + 1) for j in range(n*n)] for i in range(n*n)]
	#show(matrix)
	#print ''
	matrix = mix(matrix)
	#show(matrix)
	#print ''
	return matrix

def transpone(mat):
    mat2 = []
    for i in range(len(mat[0])):
        for j in range(len(mat)):
            if j==0:
                mat2.append([])
            mat2[i].append(mat[j][i])
    return mat2

def reverce_x(matrix):
	temp = []
	count = 0
	for i in range(len(matrix[0])):
		for j in range(len(matrix)):
			if j==0:
				temp.append([])
			temp[i].append(matrix[i][len(matrix)-j-1])
	return temp

def reverce_y(matrix):
	temp = []
	count = 0
	for i in range(len(matrix[0])):
		for j in range(len(matrix)):
			if j==0:
				temp.append([])
			temp[i].append(matrix[len(matrix)-i-1][j])
	return temp

def swap_x_small(matrix):
	n = int(math.sqrt(len(matrix)))
	area = random.randrange(0,n,1)
	line1 = random.randrange(0,n,1)
	line2 = random.randrange(0,n,1)
	N1 = area*n + line1	
	while (line1 == line2):
			line2 = random.randrange(0,n,1)
	N2 = area*n + line2
	temp = matrix[N1]
	matrix[N1]=matrix[N2]
	matrix[N2]=temp
	return matrix

def swap_y_small(matrix):
	matrix = transpone(swap_x_small(transpone(matrix)))
	return matrix

def swap_x_area(matrix):
	n = int(math.sqrt(len(matrix)))
	area1 = random.randrange(0,n,1)
	area2 = random.randrange(0,n,1)
	while (area1 == area2):
		area2 = random.randrange(0,n,1)
	for i in range(0, n):
		N1 = area1*n + i
		N2 = area2*n + i
		temp = matrix[N1]
		matrix[N1]=matrix[N2]
		matrix[N2]=temp
	return matrix

def swap_y_area(matrix):
	matrix = transpone(swap_x_area(transpone(matrix)))
	return matrix

def mix(matrix, amt = 10):

	'''mix_func = {0:transpone(matrix), 
				1:reverce_x(matrix),
				2:reverce_y(matrix),
				3:swap_x_small(matrix), 
				4:swap_y_small(matrix), 
				5:swap_x_area(matrix), 
				6:swap_y_area(matrix)}
	for i in range(amt+1):
		id_operation = random.randrange(0,len(mix_func),1)
		#print 'len='
		#print len(mix_func)
		#print id_operation
		matrix = mix_func.get(id_operation)'''


	mix_func = ['transpone(matrix)',
				'reverce_x(matrix)',
				'reverce_y(matrix)',
				'swap_x_small(matrix)',
				'swap_y_small(matrix)',
				'swap_x_area(matrix)',
				'swap_y_area(matrix)']
	for i in xrange(1, amt):
		id_func = random.randrange(0,len(mix_func),1)
		#print id_func
		matrix = eval(mix_func[id_func])
	return matrix


def show(matrix):
		for i in range(len(matrix[0])):
			#if i%len(matrix[0])==0:
			#	print ''
			print matrix[i]

print make_sudoku(2)
