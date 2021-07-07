def mergeSort(win, arr, arrSize, l, r):
	if l==r:
		return
	mid = (l+r)//2
	mergeSort(win, arr, arrSize, l, mid)
	mergeSort(win, arr, arrSize, mid+1, r)
	tarr = []
	i = l
	j = mid+1
	while i<=mid and j<=r:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
		arr[i].make_sel()
		arr[j].make_cur()
		darr = setArr(arr, tarr, l, mid, r, i, j, arrSize)
		darr[mid].make_mid()
		win.fill(WHITE)
		drawArr(win, darr, arrSize)
		arr[i].make_norm()
		arr[j].make_norm()
		darr[mid].make_norm()
		pygame.time.delay(70)
		if arr[i].height<=arr[j].height:
			tarr.append(arr[i])
			i+=1
		else:
			tarr.append(arr[j])
			j+=1
		darr = setArr(arr, tarr, l, mid, r, i, j, arrSize)
		darr[mid].make_mid()
		win.fill(WHITE)
		drawArr(win, darr, arrSize)
		darr[mid].make_norm()
		pygame.time.delay(70)

	while i<=mid:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
		darr = setArr(arr, tarr, l, mid, r, i, j, arrSize)
		darr[mid].make_mid()
		darr[i].make_sel()
		win.fill(WHITE)
		drawArr(win, darr, arrSize)
		pygame.time.delay(70)
		darr[mid].make_norm()
		darr[i].make_norm()
		tarr.append(arr[i])
		i+=1
		darr = setArr(arr, tarr, l, mid, r, i, j, arrSize)
		darr[mid].make_mid()
		win.fill(WHITE)
		drawArr(win, darr, arrSize)
		darr[mid].make_norm()
		pygame.time.delay(70)

	while j<=r:
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
		darr = setArr(arr, tarr, l, mid, r, i, j, arrSize)
		darr[mid].make_mid()
		darr[j].make_sel()
		win.fill(WHITE)
		drawArr(win, darr, arrSize)
		pygame.time.delay(70)
		darr[mid].make_norm()
		darr[j].make_norm()
		tarr.append(arr[j])
		j+=1
		darr = setArr(arr, tarr, l, mid, r, i, j, arrSize)
		darr[mid].make_mid()
		win.fill(WHITE)
		drawArr(win, darr, arrSize)
		darr[mid].make_norm()
		pygame.time.delay(70)

	for i in range(l,r+1):
		arr[i] = tarr[i-l]
	arr[mid].make_mid()
	for i in range(l,r+1):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
		arr[i].make_sweep()
		drawArr(win, arr, arrSize)
		arr[i].make_norm()
		pygame.time.delay(100)
		if i == mid:
			arr[i].make_mid()
	arr[mid].make_norm()