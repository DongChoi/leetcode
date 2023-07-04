# Note: I have to practice more on putting more thought into the basecase for dfs


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ESNW = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        max_area = 0

        def dfs(coord):
            if (
                coord[0] < 0
                or coord[0] >= len(grid)
                or coord[1] < 0
                or coord[1] >= len(grid[0])
                or grid[coord[0]][coord[1]] != 1
            ):
                return 0

            grid[coord[0]][coord[1]] = 0
            currArea = 1
            for directions in ESNW:
                next_coord = [coord[0] + directions[0], coord[1] + directions[1]]
                currArea += dfs(next_coord)

            return currArea

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == 1:
                    max_area = max(dfs([row, col]), max_area)
        return max_area
