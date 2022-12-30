class Solution:
	def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

		ones_row = []
		ones_col = []

		zero_row = []
		zero_col = []

		for row in grid:
			one = sum(row)
			zero = len(grid[0]) - one

			ones_row.append(one)
			zero_row.append(zero)

		for c in range(len(grid[0])):
			current_sum = 0
			for r in range(len(grid)):
				current_sum = current_sum + grid[r][c]

			ones_col.append(current_sum)
			zero_col.append(len(grid) - current_sum)

		result = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

		for r in range(len(grid)):
			for c in range(len(grid[0])):
				result[r][c] = ones_row[r] + ones_col[c] - zero_row[r] - zero_col[c]

		return result