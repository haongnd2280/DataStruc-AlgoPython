# Approach: Form a recursive function, which will follow a path and check if the path reaches the 
# destination or not. If the path does not reach the destination then backtrack and try other paths.
import random  

# Maze size. 
N = 5

def mazeInitialization(N): 
    maze = [[random.randint(0, 1) for j in range(N)] for i in range(N)]
    maze[0][0] = 1
    maze[N - 1][N - 1] = 1 

    # Bo sung them. 
    maze[N - 2][N - 1] = 1
    maze[N - 1][N - 2] = 1

    return maze 

# Function to print solution matrix. 
def printSolution(N, sol): 
    for i in range(N): 
        for j in range(N): 
            print(sol[i][j], end=' ')
        print()   

# Function to check if (x, y) is a valid move. 
def isValidMove(maze, x, y): 
    if (x >= 0 and x < N and y >= 0 and y < N and maze[x][y] == 1):
        return True   

    return False 

def mazeBacktracking(maze, sol, x, y, xdirection, ydirection, N, count): 
    for i in range(len(xdirection)):
        x_new = x + xdirection[i]
        y_new = y + ydirection[i]

        # Check if (x_new, y_new) is a valid move. 
        if isValidMove(maze, x_new, y_new): 
            # add (x_new, y_new) into solution matrix. 
            sol[x_new][y_new] = 1 
            
            # Check if (x_new, y_new) is the destination. 
            if x_new == N - 1 and y_new == N - 1: 
                count += 1
                print('Path %d: ' %(count))
                printSolution(N, sol)
            else: 
                count = mazeBacktracking(maze, sol, x_new, y_new, xdirection, ydirection, N, count)

            # Backtracking step: 
            sol[x_new][y_new] = 0
    
    return count 

# Recursive function to solve maze problem. 
def MazeProblem(N):
    # Initilize maze. 
    maze = mazeInitialization(N)

    # Initilize solution matrix. 
    sol = [[0 for j in range(N)] for i in range(N)]

    # Direction move.
    xdirection = [0, 1]
    ydirection = [1, 0]

    # solution count
    count = 0

    # The rat starts at the first square. 
    sol[0][0] = 1

    # Print the maze first. 
    print('Maze: ')
    printSolution(N, maze)

    # start to find the path. 
    count = mazeBacktracking(maze, sol, 0, 0, xdirection, ydirection, N, count)

    if count == 0: 
        print('The path has no solution.')

# Bat dau chuong trinh: 
MazeProblem(N)



    





