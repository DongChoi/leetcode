"""
200. Number of Islands
Medium
20K
440
Companies
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == "1":
                    self.turn_island_to_zero(grid, x, y)
                    res += 1
        print(grid)
        return res

    def turn_island_to_zero(self, grid, x, y):
        if grid[y][x] != "1":
            return
        else:
            grid[y][x] = "0"
            if x + 1 < len(grid[0]):
                self.turn_island_to_zero(grid, x + 1, y)
            if x - 1 >= 0:
                self.turn_island_to_zero(grid, x - 1, y)
            if y + 1 < len(grid):
                self.turn_island_to_zero(grid, x, y + 1)
            if y - 1 >= 0:
                self.turn_island_to_zero(grid, x, y - 1)
