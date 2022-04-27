import numpy as np

grid = [[4, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 9, 8],
        [3, 0, 0, 0, 8, 2, 4, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 8, 0],
        [9, 0, 3, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 3, 0, 6, 7, 0],
        [0, 5, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 9, 0, 7],
        [6, 4, 0, 3, 0, 0, 0, 0, 0],]

def check_valid(row, col, num):
  #check row
  global grid
  for i in range(9):
      if grid[row][i] == num:
          return False
  #check column
  for i in range(9):
      if grid[i][col] == num:
          return False
  #check 3x3 grid
  row_start = (row//3)*3
  col_start = (col//3)*3
  for i in range(row_start, row_start+3):
      for j in range(col_start, col_start+3):
          if grid[i][j] == num:
              return False
  return True

def solve():
  global grid
  for i in range(9):
      for j in range(9):
          if grid[i][j] == 0:
              for num in range(1,10):
                  if check_valid(i, j, num):
                      grid[i][j] = num
                      solve()
                      grid[i][j] = 0
              return
              
  print(np.matrix(grid))
  return

def main():
    solve()

main()