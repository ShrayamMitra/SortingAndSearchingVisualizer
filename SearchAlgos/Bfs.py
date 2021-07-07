def BFS(draw, grid, start, end):
	cur_dat = Queue()
	cur_dat.put(start)
	came_from = {}
	#python hacks to initialise
	dist = {spot: float("inf") for row in grid for spot in row}
	dist[start] = 0;

	while not cur_dat.empty():
		#as this algo would be running ,if we want someone
		#to exit it we need to keep the following check
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = cur_dat.get() #the node

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_dist = dist[current] + 1

			if temp_dist < dist[neighbor]:
				came_from[neighbor] = current
				dist[neighbor] = temp_dist
				cur_dat.put(neighbor)
				neighbor.make_open()
		draw()

		if current != start:
			current.make_closed() #already considered

	return False
