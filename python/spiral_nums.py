class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [["" for _ in range(n)] for _ in range(n)]
        counter = n * n
        number_counter = 1
        r, c = 0, 0
        direction = "right"
        while number_counter < counter + 1:
            if direction == "right":
                matrix[r][c] = number_counter
                if c + 1 >= n or matrix[r][c + 1] != "":
                    direction = "down"
                    r += 1
                else:
                    c += 1
            elif direction == "down":
                matrix[r][c] = number_counter
                if r + 1 >= n or matrix[r + 1][c] != "":
                    direction = "left"
                    c -= 1
                else:
                    r += 1
            elif direction == "left":
                matrix[r][c] = number_counter
                if c - 1 < 0 or matrix[r][c - 1] != "":
                    direction = "up"
                    r -= 1
                else:
                    c -= 1
            elif direction == "up":
                matrix[r][c] = number_counter
                if r - 1 < 0 or matrix[r - 1][c] != "":
                    direction = "right"
                    c += 1
                else:
                    r -= 1
            number_counter += 1
        print(matrix)
        return matrix
