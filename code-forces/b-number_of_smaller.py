if __name__ == "__main__":
	n, m = map( int, input().split() )
	arr_n = list( map( int, input().split() ) )
	arr_m = list( map( int, input().split() ) )

	p1, p2 = 0, 0
	answer = []

	while p1 < n and p2 < m:
		while p1 < n and arr_n[p1] < arr_m[p2]:
			p1 += 1
		answer.append(p1)
		p2 += 1

	while p2 < m:
		answer.append(p1)
		p2 += 1

	print(*answer)
