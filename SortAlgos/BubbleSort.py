def bubbleSort(win, drawArr, arr, arrSize):
	for curSize in reversed(range(arrSize)):
		for i in range(curSize):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
			arr[i].make_sel()
			arr[i+1].make_cur()
			win.fill(WHITE)
			drawArr()
			pygame.time.delay(70)
			if arr[i].height>arr[i+1].height:
				arr[i],arr[i+1] = arr[i+1],arr[i]
			win.fill(WHITE)
			drawArr()
			pygame.time.delay(70)
			arr[i].make_norm()
		arr[curSize].make_norm()