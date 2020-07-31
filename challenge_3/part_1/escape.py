def path_traversal(wx, hy, maze):
    #Take the width and height of the maze.
    #Then draw up a board
    
    w = len(maze[0])
    h = len(maze)
    board = [[None for i in range(w)] for i in range(h)]
    board[wx][hy] = 1

    arr = [(wx, hy)]
    while arr:
        x, y = arr.pop(0)
        for i in [[1,0],[-1,0],[0,-1],[0,1]]:
          nx, ny = x + i[0], y + i[1]
          if 0 <= nx < h and 0 <= ny < w:
            if board[nx][ny] is None:
                board[nx][ny] = board[x][y] + 1
                if maze[nx][ny] == 1 :
                    continue
                arr.append((nx, ny)) 
                  
    return board

def solution(maze):
  w = len(maze[0])
  h = len(maze)

  ans = 2 ** 32-1
  for i in range(h):
      for j in range(w):
          #Shortest path from start to end
          if path_traversal(0, 0, maze)[i][j] and path_traversal(h-1, w-1, maze)[i][j]:
              ans = min(path_traversal(0, 0, maze)[i][j] + path_traversal(h-1, w-1, maze)[i][j] - 1, ans)
  return ans
