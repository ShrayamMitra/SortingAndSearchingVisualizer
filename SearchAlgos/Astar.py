def Astar(draw, grid, start, end):
	count = 0
	cur_dat = PriorityQueue()
	# zero here is the f-score
	cur_dat.put((0, count, start))
	came_from = {}
	#python hacks to initialise
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	#this keeps track of things in/out of priority_queue
	seen = {start}

	while not cur_dat.empty():
		#as this algo would be running ,if we want someone
		#to exit it we need to keep the following check
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = cur_dat.get()[2] #the node
		cur_dat
		seen.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())

				if neighbor not in seen:
					count += 1
					cur_dat.put((f_score[neighbor], count, neighbor))
					seen.add(neighbor)
					neighbor.make_open() #inserted
		draw()

		if current != start:
			current.make_closed() #already considered

	return False
