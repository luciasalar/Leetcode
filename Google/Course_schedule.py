graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

graph["A"][1]

def find_path(graph, start, end, path = []):
	path = path + [start]  #TypeError: can only concatenate list (not "str") to list #path = [A]
	print('path is ' + str(path))
	if start == end: 
		return [path]
	if start not in graph:
		return None
	paths = []
	for node in graph[start]: #node = ['b', 'c']
		print ('node is ' + str(node))
		if node not in path:
			newpath = find_path(graph, node, end, path) #find_path(graph, 'A', 'B', ['A'])
			print ('newpath is ' + str(newpath))
			for p in newpath:
				paths.append(p)
	return paths

find_path(graph, 'A', 'B')





