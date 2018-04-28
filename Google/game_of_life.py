

Matrix = [[0, 1, 0, 1, 0, 1, 0, 1],
 		[0, 1, 0, 0, 1, 1, 0, 1],
 		[0, 0, 1, 1, 0, 0, 0, 0],
 		[1, 1, 0, 1, 0, 1, 1, 0],
 		[1, 0, 1, 0, 0, 1, 0, 1]]

Matrix_copy = [[0, 1, 0, 1, 0, 1, 0, 1],
 		[0, 1, 0, 0, 1, 1, 0, 1],
 		[0, 0, 1, 1, 0, 0, 0, 0],
 		[1, 1, 0, 1, 0, 1, 1, 0],
 		[1, 0, 1, 0, 0, 1, 0, 1]]



#cells on the top edge
m = 0#height
n = 1 #width
while n+1 < len(Matrix[1]):
	#print(Matrix[m][n])
	l1 = [Matrix[m][n-1], Matrix[m][n], Matrix[m][n+1], Matrix[m+1][n-1], Matrix[m+1][n], Matrix[m+1][n+1], Matrix[m+2][n-1], Matrix[m+2][n], Matrix[m+2][n+1]]
#	print(l1)
	l2 =[]
	l3 =[]
	for i in l1:
		if i == 1:
			l2.append(i)
		if i == 0:
			l3.append(i)
		if Matrix[m][n] == 1 & len(l2)<2:
			Matrix[m][n] = 0
		if Matrix[m][n] == 1 & len(l2) == 2:
			Matrix[m][n] = 1
		if Matrix[m][n] == 1 & len(l2) > 3:
			Matrix[m][n] = 0
		if Matrix[m][n] == 0 & len(l3) == 3:
			Matrix[m][n] = 1

	n+=1
m+=1


#cells in the middle

m = 1 #height
while m+1 < len(Matrix) :
	n = 1 #width		
	while n+1 < len(Matrix[1]):
		#print(Matrix[m][n])
		l1 = [Matrix[m-1][n-1], Matrix[m-1][n], Matrix[m-1][n+1], Matrix[m][n-1], Matrix[m][n+1], Matrix[m+1][n-1], Matrix[m+1][n], Matrix[m+1][n+1]]
		#print(l1)
		l2 =[]
		l3 =[]
		new_m = [] 
		for i in l1:
			if i == 1:
				l2.append(i)
			#	print(i)
			if i == 0:
			#	l3.append(i)
				print(l3)
			if Matrix[m][n] == 1 & len(l2)<2:
				Matrix[m][n] = 0
			if Matrix[m][n] == 1 & len(l2) == 2:
				Matrix[m][n] = 1
			if Matrix[m][n] == 1 & len(l2) > 3:
				Matrix[m][n] = 0
			if Matrix[m][n] == 0 & len(l3) == 3:
				Matrix[m][n] = 1
			else:
				Matrix[m][n] == Matrix[m][n]
		new_m.append(Matrix[m][n])
		print(new_m)
		Matrix == Matrix_copy
		n+=1
	m+=1

#cells on the botton edge
m = len(Matrix)-1 #height
n = 1 #width
while n+1 < len(Matrix[1]):
	#print(Matrix[m][n])
	l1 = [Matrix[m][n-1], Matrix[m][n], Matrix[m][n+1], Matrix[m-1][n-1], Matrix[m-1][n], Matrix[m-1][n+1], Matrix[m-2][n-1], Matrix[m-2][n], Matrix[m-2][n+1]]
	#print(l1)
	l2 =[]
	l3 =[]
	for i in l1:
		if i == 1:
			l2.append(i)
		if i == 0:
			l3.append(i)
		if Matrix[m][n] == 1 & len(l2)<2:
			Matrix[m][n] = 0
		if Matrix[m][n] == 1 & len(l2) == 2:
			Matrix[m][n] = 1
		if Matrix[m][n] == 1 & len(l2) > 3:
			Matrix[m][n] = 0
		if Matrix[m][n] == 0 & len(l3) == 3:
			Matrix[m][n] = 1

	n+=1
m+=1
	
Matrix



l1 = [Matrix[m-1][n-1], Matrix[m-1][n], Matrix[m-1][n+1], Matrix[m][n-1], Matrix[m][n], Matrix[m][n+1], Matrix[m+1][n-1], Matrix[m+1][n], Matrix[m+1][n+1]]
#print(l1)
l2 =[]
l3 =[]
new_m = [] 
for i in l1:
	if i == 1:
		l2.append(i)
	if i == 0:
		l3.append(i)
if Matrix[m][n] == 1 & len(l2)<2:
	Matrix[m][n] = 0
if Matrix[m][n] == 1 & len(l2) == 2:
	Matrix[m][n] = 1
if Matrix[m][n] == 1 & len(l2) > 3:
	Matrix[m][n] = 0
if Matrix[m][n] == 0 & len(l3) == 3:
	Matrix[m][n] = 1
else:
	Matrix[m][n] == Matrix[m][n]

new_m.append(Matrix[m][n])

