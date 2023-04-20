# Bai toan ma di tuan: Given a N x N board with the Knight placed on the first block 
# of an empty board. Moving accordingly to the rules of chess knight must visit each square exactly once. 
# Print the order of each the cell in which they are visited. 

# Backtracking algorithm: 
# If all squares are visited: 
#     print the solution 
# Else: 
#    1. Add one of the next moves to solution vector and RECURSIVELY check if this move leads 
#       to a solution. 
#    2. If the move chosen in the above step doesn't lead to a solution, then remove this move 
#       from the solution vector and try other alternative moves. 
#    3. If none of the alternatives work, then return False (Returning False will remove the 
#       previous added item in recursion, if False is returned by the initial call of 
#       recursion, then "no solution exist"). 

N = 8  

def isValidMove(x, y, board): 
    '''A utility function to check if (x, y) are valid indexes for N x N board.'''
    if (x >= 0 and y >= 0 and x < N and y < N and board[x][y] == -1):  # danh dau nhung o chua di bang gia tri -1.
        return True 

    return False 

def printSolution(N, board): 
    '''A utility function to print Chessboard matrix.'''
    for i in range(N): 
        for j in range(N): 
            print(board[i][j], end=' ')
        print()

def recurKnightTour(N, board, curr_x, curr_y, xdirection, ydirection, pos): 
    '''A recursive utility function to solve Knight Tour problem.'''
    if (pos == N * N): 
        return True 

    # Try all next moves from the current coordinate (x, y). 
    for i in range(8):  
        new_x = curr_x + xdirection[i]
        new_y = curr_y + ydirection[i]

        if (isValidMove(new_x, new_y, board)): 
            board[new_x][new_y] = pos   # danh dau chi so cua vi tri moi. 
            # Recursive step: 
            if (recurKnightTour(N, board, new_x, new_y, xdirection, ydirection, pos + 1)):  # = if True (if pos == N * 2)
                return True  
                # Chu y: o buoc nay, neu tim thay loi giai, thi no se lap tuc tra ve True, va khong 
                # tim them loi giai khac nua. Day se la loi giai duy nhat cua ham nay. Vi vay, ham 
                # nay co mot nhuoc diem, do la chua tim duoc het loi giai cua bai toan. 
            
            # Backtracking step: dat lai (new_x, new_y) = -1. 
            board[new_x][new_y] = -1

    return False 

def KnightTour(N): 
    '''This function solves the Knight Tour problem using backtracking. 
    This function mainly uses recurKnightTour() to solve the problem. It returns False 
    if no complete tour is possible, otherwise return True and prints the tour. 
    Please note that there may be more than one solution, this function prints one of the
    feasible solutions.'''

    # Initialization of board. 
    board = [[-1 for j in range(N)] for i in range(N)]

    # move_x and move_y define next move of Knight. 
    # tong cong co 8 move co the di chuyen tai moi buoc (tinh ca valid va invalid moves). 
    xdirection = [2, 1, -1, -2, -2, -1, 1, 2]
    ydirection = [1, 2, 2, 1, -1, -2, -2, -1]

    # The Knight is initialized at the first block. 
    board[0][0] = 0 

    # Step counter for Knight's position. 
    pos = 1  
    
    # Check if solution exists or not. 
    if (not recurKnightTour(N, board, 0, 0, xdirection, ydirection, pos)): 
        print('Solution does not exist.')
    else: 
        printSolution(N, board)

if __name__ == "__main__":
     
    # Function Call
    KnightTour(N)

# chay mat 3phut. 






