import random

N = 9

# Function to print the Sudoku grid
def printGrid(grid):
    print("   1 2 3   4 5 6   7 8 9")  # Print column numbers
    for row in range(N):
        if row % 3 == 0 and row != 0:
            print("   " + "-" * 21)  # Print horizontal separator
        print(row + 1, "|", end=" ")  # Print row number
        for col in range(N):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")  # Print vertical separator
            if grid[row][col] == 0:
                print("_", end=" ")  # Display underscore for empty cells
            else:
                print(grid[row][col], end=" ")
        print("|")

# Function to check if a number can be placed in a cell
def isSafe(grid, row, col, num):
    # Check if the number exists in the row or column
    if num in grid[row] or num in [grid[i][col] for i in range(N)]:
        return False

    # Check if the number exists in the 3x3 grid
    startRow, startCol = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False

    return True

# Function to solve the Sudoku puzzle using backtracking
def solveSudoku(grid):
    empty_cell = findEmptyCell(grid)
    if not empty_cell:
        return True

    row, col = empty_cell

    for num in range(1, 10):
        if isSafe(grid, row, col, num):
            grid[row][col] = num

            if solveSudoku(grid):
                return True

            grid[row][col] = 0

    return False

# Function to find the first empty cell in the grid
def findEmptyCell(grid):
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return i, j
    return None

# Function to check if the Sudoku puzzle is valid
def isValidSudoku(grid):
    for i in range(N):
        row_check = [False] * N
        col_check = [False] * N

        for j in range(N):
            if grid[i][j] != 0:
                if row_check[grid[i][j] - 1]:
                    return False  # Duplicate in row
                row_check[grid[i][j] - 1] = True

            if grid[j][i] != 0:
                if col_check[grid[j][i] - 1]:
                    return False  # Duplicate in column
                col_check[grid[j][i] - 1] = True

    for i in range(0, N, 3):
        for j in range(0, N, 3):
            subgrid_check = [False] * N
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if grid[row][col] != 0:
                        if subgrid_check[grid[row][col] - 1]:
                            return False  # Duplicate in subgrid
                        subgrid_check[grid[row][col] - 1] = True

    return True  # Sudoku is valid

# Function to generate a random Sudoku puzzle
def generateRandomSudoku():
    grid = [[0] * N for _ in range(N)]

    # Fill the diagonal 3x3 subgrids with random values
    for i in range(0, N, 3):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for row in range(i, i + 3):
            for col in range(i, i + 3):
                while not isSafe(grid, row, col, nums[0]):
                    random.shuffle(nums)
                grid[row][col] = nums.pop(0)

    solveSudoku(grid)

    # Remove random cells to create the puzzle
    num_to_remove = random.randint(30, 59)  # Adjust the number of cells to remove as desired
    while num_to_remove > 0:
        row = random.randint(0, N - 1)
        col = random.randint(0, N - 1)
        if grid[row][col] != 0:
            grid[row][col] = 0
            num_to_remove -= 1

    return grid

# Main function
def main():
    grid = generateRandomSudoku()
    solved_grid = [row[:] for row in grid]  # Copy the grid for validation
    solveSudoku(solved_grid)

    print("Randomly Generated Sudoku Puzzle:")
    printGrid(grid)

    wrong_attempts = 0

    while True:
        row, col, num = map(int, input("Enter row (1-9), column (1-9), and number (1-9) or 0 to exit: ").split())

        if row == 0 or col == 0 or num == 0:
            break

        row -= 1
        col -= 1

        if row < 0 or row >= N or col < 0 or col >= N or num < 1 or num > 9:
            print("Invalid input. Please try again.")
            continue

        if grid[row][col] != 0:
            print("Cell already filled. Please try again.")
            continue

        grid[row][col] = num
        if not isValidSudoku(grid):
            print("Invalid Sudoku! Correct your input.")
            grid[row][col] = 0  # Reset the cell if it makes the Sudoku invalid
            wrong_attempts += 1

            if wrong_attempts >= 3:
                print("Three wrong attempts. Showing the solution:")
                printGrid(solved_grid)
                break

        print("Updated Sudoku Puzzle:")
        printGrid(grid)

        # Check if the puzzle is solved
        if all(all(cell != 0 for cell in row) for row in grid):
            print("Congratulations! You solved the Sudoku puzzle. You are the winner!")
            break

if __name__ == "__main__":
    main()
