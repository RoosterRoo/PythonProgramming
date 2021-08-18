n = int(input())
lst = []
for i in range(n):
	temp = []
	for j in range(i+1):
		if j == 0 or j == i:
			temp.append(7)
		else:
			temp.append(lst[i-1][j-1] + lst[i-1][j])
	lst.append(temp)
 
for i in range(n):
    for j in range(i+1):
        print(lst[i][j], end=" ")
    print()