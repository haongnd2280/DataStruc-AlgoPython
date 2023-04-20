N = 8  

def printSolution(N, board): 
    '''A utility function to print Chessboard matrix.'''
    for i in range(N): 
        for j in range(N): 
            print(board[i][j], end=' ')
        print()

def isValidMove(N, board, x, y): 
    if x >= 0 and x < N and y >= 0 and y < N and board[x][y] == -1: 
        return True

    return False

def KnightTourBacktrack(N, board, x, y, xdirection, ydirection, pos, count):
    for i in range(len(xdirection)): 
        x_new = x + xdirection[i]
        y_new = y + ydirection[i]

        # Check if (x_new, y_new) is valid move. 
        if isValidMove(N, board, x_new, y_new):
            board[x_new][y_new] = pos + 1

            # If (x_new, y_new) is a valid move, check if it is the final block. 
            if pos + 1 == N * N: 
                count += 1
                print('Path %d found: ' %(count))
                printSolution(N, board)
            else: 
                count = KnightTourBacktrack(N, board, x_new, y_new, xdirection, ydirection, pos + 1, count)

            # Backtracking step: if cannot find a move in the preceding if-else block. 
            board[x_new][y_new] = -1 
    
    return count 

def KnightTourProblem(N): 
    # Board initilization. 
    board = [[-1 for j in range(N)] for i in range(N)]

    # direction move. 
    xdirection = [-2, -2, -1, -1, 1, 1, 2, 2]
    ydirection = [-1, 1, -2, 2, -2, 2, -1, 1]

    # solution count. 
    count = 0 

    # current count. 
    pos = 0

    #xstart = int(input('Nhap vao diem x xuat phat: '))
    # ystart = int(input('Nhap vao diem y xuat phat: '))

    # Bat dau thuc hien. 
    count = KnightTourBacktrack(N, board, 0, 0, xdirection, ydirection, pos, count)

    if count == 0: 
        print('No solution exists.')


# Bat dau chuong trinh. 
KnightTourProblem(N)





