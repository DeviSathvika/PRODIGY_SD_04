def print_grid(grid):
    """Prints the Sudoku grid in a user-friendly format."""
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(grid[i][j], end=" ")
        print()

def find_empty(grid):
    """Finds an empty cell (represented by 0) in the grid."""
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)  # row, col
    return None

def is_valid(grid, num, pos):
    """Checks if placing 'num' at 'pos' is a valid move."""
    # Check row
    for i in range(9):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(9):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False

    return True

def solve(grid):
    """Solves the Sudoku puzzle using backtracking."""
    find = find_empty(grid)
    if not find:
        return True  # Puzzle solved

    row, col = find

    for num in range(1, 10):
        if is_valid(grid, num, (row, col)):
            grid[row][col] = num

            if solve(grid):  # Recursively try to solve
                return True

            grid[row][col] = 0  # Backtrack if the solution is invalid

    return False  # No solution found

# Example Sudoku puzzle (0 represents empty cells)
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Unsolved Sudoku:")
print_grid(grid)

if solve(grid):
    print("\nSolved Sudoku:")
    print_grid(grid)
else:
    print("No solution exists.")