def DFS(draw, grid, start, end):
	cur_dat = LifoQueue()
	cur_dat.put(start)
	came_from = {}
	#python hacks to initialise
	vis = {spot: 0 for row in grid for spot in row}
	vis[start] = 1;

	while not cur_dat.empty():
		#as this algo would be running ,if we want someone
		#to exit it we need to keep the following check
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = cur_dat.get() #the node

		for neighbor in current.neighbors:
			if not vis[neighbor]:
				came_from[neighbor] = current
				vis[neighbor] = 1
				if neighbor == end:
					reconstruct_path(came_from, end, draw)
					end.make_end()
					return True
				cur_dat.put(neighbor)
				neighbor.make_open()
		draw()

		if current != start:
			current.make_closed() #already considered

	return False
