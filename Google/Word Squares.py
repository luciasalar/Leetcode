from numpy import array
l = ["ball","area","lead","lady"]



Matrix = np.array([[0, 1, 2, 0],
[3, 9, 0, 0],
[4, 3, 0, 0],
[5, 2, 4, 0]])

def word_squares(l):
	h =[]
	for i in range(len(l)):
		for m in l[i]:
			h.append(m)
	n = len(l[1])
	Matrix = array(h).reshape(n,n)
	#print(Matrix)


	if Matrix[:, n-1] == Matrix[n-1, :]:
	
		print(Matrix)


word_squares(l)





