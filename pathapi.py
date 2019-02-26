from collections import deque

#8*8 Grid
N = 8

#Make all grids as not visited
visited = [[(-1,-1) for i in range(0,N)] for j in range(0,N)]

#Get all possible movements for the knight
def getPositions(current):
	#all possible movments for the knight 
    dx = [2, 2, -2, -2, 1, 1, -1, -1] 
    dy = [1, -1, 1, -1, 2, -2, 2, -2] 
    positions = []
    for i in range(8):
    	newpostion = (current[0]+dx[i],current[1]+dy[i])
    	#Check if new position lies inside grid:
    	if newpostion[0]>=0 and newpostion[0]< N and newpostion[1]>=0 and newpostion[1]<N:
    		positions.append(newpostion)
    return positions

def shortestPath(start,end):
	q = deque()
	q.append(start)

	#mark start position as visited
	#storing the parent values in visited for determining path
	visited[start[0]][start[1]] = start

	while q:
		current = q.popleft()
		if current == end:
			break
		#get all movements from the current position
		pos = getPositions(current)
		for i in pos:
			#check if position is not already visited and append to queue
			if visited[i[0]][i[1]]==(-1,-1):
				#Store current value in positions as parent
				visited[i[0]][i[1]] = current
				q.append(i)

	#Determine path by tracing back from end position and obtainting the parent
	path = [(end)]    
	while end != start:
		end = visited[end[0]][end[1]]
		path.append(end)

	path.reverse()
	return path

# path = shortestPath((0,0),(7,0))
# print(path)