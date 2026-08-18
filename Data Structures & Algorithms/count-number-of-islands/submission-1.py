class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #initalize the lengths for rows and columns
        rows = len(grid)
        cols = len(grid[0])
        
        if not grid:
            return 0

        visit = set()
        islands = 0

        def bfs(row, col):
            q = collections.deque()
            visit.add((row, col))
            q.append((row, col))

            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1], [0, -1]]
                
                for dr, dc in directions:
                    if ((row+dr) in range(rows) and
                    (col+dc) in range(cols) and
                    grid[row + dr][col+ dc] =="1" and
                    (row+dr, col+dc) not in visit):

                        q.append((row+dr, col+dc))
                        visit.add((row+dr, col+dc))
                    

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visit:
                    bfs(row,col)
                    islands += 1
        return islands
