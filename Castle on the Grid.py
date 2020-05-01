# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    row = len(grid)
    col = len(grid[0])
    ans = row*col

    def recur(i,j,steps,path):
        global ans
        if i>=row or i<0 or j>=col or j<0 or grid[i][j]=='X':
            return

        if i==goalX and j==goalY:
            print('here')
            ans = min(ans,steps)
            print(*path,sep=' -> ')
            return

        grid[i][j]='X'
        recur(i-1,j,steps+1,path[:]+[(i-1,j)])
        recur(i+1,j,steps+1,path[:]+[(i+1,j)])
        recur(i,j-1,steps+1,path[:]+[(i,j-1)])
        recur(i,j+1,steps+1,path[:]+[(i,j+1)])
        grid[i][j]='.'

    recur(startX,startY,0,[(startX,startY)])

    return ans

if __name__ == '__main__':

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = list(input())
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(result)
