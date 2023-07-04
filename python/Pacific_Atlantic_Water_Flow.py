## Neetcode Solution
## What a clever solution!
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()
        res = []

        def dfs(r, c, visited, prevHeight):
            if (
                (r, c) in visited
                or r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or heights[r][c] < prevHeight
            ):
                return
            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res


### My Solution
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        def dfs(row, col, height, visited, dfs_res):
            if row < 0 or col < 0:
                dfs_res[0] = "Pacific"
                return dfs_res
            if row >= len(heights) or col >= len(heights[0]):
                dfs_res[1] = "Atlantic"
                return dfs_res
            if (row, col) in visited:
                return dfs_res
            if height >= heights[row][col]:
                visited.add((row, col))
                dfs_res = dfs(row - 1, col, heights[row][col], visited, dfs_res)
                dfs_res = dfs(row + 1, col, heights[row][col], visited, dfs_res)
                dfs_res = dfs(row, col + 1, heights[row][col], visited, dfs_res)
                dfs_res = dfs(row, col - 1, heights[row][col], visited, dfs_res)
            return dfs_res

        for r in range(len(heights)):
            for c in range(len(heights[r])):
                visited = set()
                dfs_res = dfs(r, c, heights[r][c], visited, ["", ""])
                print(dfs_res, [r, c])
                if dfs_res == ["Pacific", "Atlantic"]:
                    res.append([r, c])
        return res
