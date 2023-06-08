##neetcode solution.
# learned deque! SO COOL!


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # infect 4 squares each round,
        # put rotted oranged on Queue

        queue = deque()
        time, fresh = 0, 0
        for row in range(len(grid)):
            for column in range(len(grid[row])):
                if grid[row][column] == 2:
                    queue.append([row, column])
                elif grid[row][column] == 1:
                    fresh += 1
        # first iteration should have queue = [[0,0]]
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue and fresh > 0:
            print(queue)
            for i in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row, col = dr + r, dc + c
                    if (
                        row < 0 or row == len(grid) or col < 0 or col == len(grid[0])
                    ) or grid[row][col] != 1:
                        continue
                    else:
                        grid[row][col] = 2
                        queue.append([row, col])
                        fresh -= 1
            time += 1
        return time if fresh == 0 else -1
