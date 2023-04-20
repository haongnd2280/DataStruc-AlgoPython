N = 8 

def printSolution(N, sol): 
    # Cach 1: 
    for j in range(N): 
        print(sol[j], end=' ')

    # Cach 2: 
    board = [[0 for j in range(N)] for i in range(N)]
    for j in range(N): 
        board[sol[j]][j] = 1  

    for i in range(N): 
        for j in range(N): 
            print(board[i][j], end=' ')  # in chi so cac cot tuan tu theo hang tu tren xuong duoi. 
        print()  

def isValidMove(sol, x, y): 
    # Dau hai nhan biet hai diem o tren cung mot duong cheo: bon diem (x1, y1), (x2, y2) se
    # giao nhau tao thanh mot hinh vuong. Khi do: |x2 - x1| = |y2 - y1| 
    for j in range(y):  
        if sol[j] == x or abs(j - y) == abs(sol[j] - x): 
            return False 

    return True  

def NQueensProblem(N, sol, j):
    for i in range(N): 
        # Thu dat quan hau vao cac hang tu 1 den N. 
        if isValidMove(sol, i, j):
            # If is valid move, then append to sol.
            sol[j] = i 
            # Check that if there is any column left. 
            if j == N: 
                printSolution(N, sol)
            else: 
                NQueensProblem(N, sol, j + 1)

            # Chu y: Doan nay khong co backtracking, do ta xet theo tung cot mot va tung hang mot. Nghiem moi
            # se duoc ghi de vao bien sol. 

if __name__ == '__main__':
    sol = [-1 for i in range(N)]
    NQueensProblem(N, sol, 0) 

  


