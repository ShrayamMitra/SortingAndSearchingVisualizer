def insertionSort(win, drawArr, arr, arrSize):
	for i in range(1, arrSize):
		for j in reversed(range(1,i+1)):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			if arr[j].height>arr[j-1].height:
				break
			arr[j].make_sel()
			arr[j-1].make_cur()
			win.fill(WHITE)
			drawArr()
			pygame.time.delay(70)
			arr[j],arr[j-1] = arr[j-1],arr[j]
			win.fill(WHITE)
			drawArr()
			pygame.time.delay(70)
			arr[j].make_norm()
			arr[j-1].make_norm()