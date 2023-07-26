# function to display the board
def display(board):
    for row in board:
        print(row)
        
# function to check if position is safe
def isSafe(board,x,y,n):
    # column test 
    for row in range(x):
        if board[row][y]=='Q':
            return False
    # upper left diagonal test
    xx = x-1
    yy = y-1
    while(xx>=0 and yy>=0):
        if (board[xx][yy]=='Q'):
            return False
        xx = xx-1
        yy = yy-1
    
    # upper right diagonal test
    xx = x-1
    yy = y+1
    while(xx>=0 and yy<n):
        if (board[xx][yy]=='Q'):
            return False
        xx = xx-1
        yy = yy+1
    return True

# now placing queens
def nQueensSolver(board, x, n):
    # if we successfully placed all queens return true
    if(x>=n):
        return True
    # iterate through the columns for each row
    for col in range(n):
        # if the particular position is safe then place the queen
        if(isSafe(board,x,col,n)):
            board[x][col]='Q'
            # if the next queen can't be paced than backtrack
            if (nQueensSolver(board,x+1,n)):
                return True
            board[x][col]=' '
    return False

n = int(input('Enter the number of queens: '))
# generating board dynamically
board = [[" "]*n for i in range(n)]

if nQueensSolver(board,0,n):
    display(board)
else:
    print('NO SOLUTION FOUND')