tests = int(input())

for _ in range(tests):
    a, b = map( int, input().split() )

    print( min( a, b, (a + b) // 4 ) )
