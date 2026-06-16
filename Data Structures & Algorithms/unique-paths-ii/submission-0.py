class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def solve(x: int, y: int) -> int:
            if x >= rows or y >= cols:
                return 0

            if obstacleGrid[x][y] == 1:
                return 0

            if x == rows - 1 and y == cols - 1:
                return 1

            if dp[x][y] != -1:
                return dp[x][y]

            down = solve(x+1, y)
            right = solve(x,y+1)

            dp[x][y] = down + right
            return dp[x][y]
        return solve(0,0)


