# The N queen is the problem of placing N chess queens on an N x N chessboard so that no 
# two queens attack each other. 

# The idea is to place queens one by one in different columns, starting from the leftmost column 
# (rat hay, cach nay se khong xay ra su trung lap dap an). In the current column, if we find a row 
# for which there is no clash, we mark this row and column as part of the solution. 
# If we do not find such a row due to clashes then we backtrack and return false.

# Luu y: neu trong cot dang xet, neu khong tim duoc hang nao de dat hau thi backtrack luon, vi moi
# hang phai co mot con hau. 
# Chu y: dung mot bien usedRows chi nhung hang da su dung (da co hau roi). 

N = 4 

def boardInitilization(N): 
    board = [[0 for j in range(N)] for i in range(N)]

    return board  

def printSolution(N, board): 
    for i in range(N): 
        for j in range(N): 
            print(board[i][j], end=' ')
        print()  

def isValidMove(board, x, y): 
    # phai tim cach kiem tra xem hai con hau co an nhau hay khong (tong 4 huong).
    pass

def NQueensBacktrack(board, col, sol):
    for i in range(N): 
        if isValidMove(board, i, col): 
            # Add (i, col) to the solution matrix (mark as 1). 
            sol[i][col] = 1 
            # add restriced block associated with (i, col). dung boardCopy??? 
            pass

            # check if there is any column left. 
            if col == N - 1: 
                print('One solution: ')
                printSolution(sol)
            else: 
                NQueensBacktrack(board, col + 1, sol)
        
            # Backtracking step: if there is no move feasible from (i, col). 
            sol[i][col] = 0 
            pass # remove restriced block associated with (i, col). 





