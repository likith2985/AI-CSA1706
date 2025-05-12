def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nq_util(board, col, n, solutions):
    if col >= n:
        solution = []
        for i in range(n):
            row_str = ""
            for j in range(n):
                row_str += "Q " if board[i][j] == 1 else ". "
            solution.append(row_str.strip())
        solutions.append(solution)
        return True 

    res = False
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            res = solve_nq_util(board, col + 1, n, solutions) or res 

            board[i][col] = 0

    return res

def solve_8_queens():
    n = 8
    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    solve_nq_util(board, 0, n, solutions)

    if not solutions:
        print("Solution does not exist")
        return []

  
    return solutions

if __name__ == "__main__":
    all_solutions = solve_8_queens()
    if all_solutions:
        print(f"Found {len(all_solutions)} solutions for the 8-Queen problem.")
        print("Showing the first solution as an example:")
        for row_str in all_solutions[0]:
            print(row_str)

