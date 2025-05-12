"""
This program solves cryptarithmetic puzzles.
A cryptarithmetic puzzle is an arithmetic puzzle where letters are substituted for digits.
The goal is to find the digit corresponding to each letter such that the given
arithmetic equation holds true. Each letter must represent a unique digit, and the
leading digit of a multi-digit number cannot be zero.

Example: SEND + MORE = MONEY
"""

import itertools

def solve_cryptarithmetic(puzzle_str):
    """
    Solves a cryptarithmetic puzzle.

    Args:
        puzzle_str (str): The puzzle in string format, e.g., "SEND + MORE = MONEY".
                          It can also handle multiple operands on the left side,
                          e.g., "WORD1 + WORD2 + WORD3 = RESULT".

    Returns:
        str: A string describing the solution if found (e.g., "Solution: S=9, E=5, ... -> 9567 + 1085 = 10652"),
             or a message indicating no solution was found or if the puzzle is invalid.
    """
    try:
        # Normalize and parse the puzzle string
        puzzle_str = puzzle_str.replace(" ", "").upper()
        if puzzle_str.count("=") != 1:
            return "Invalid puzzle format: Must contain exactly one '=' sign."

        left_side, right_side = puzzle_str.split("=")
        if not right_side:
            return "Invalid puzzle format: Result part cannot be empty."
        
        operand_words = left_side.split("+")
        if not all(operand_words) or not operand_words:
             return "Invalid puzzle format: Operand parts cannot be empty."

        result_word = right_side
        all_words = operand_words + [result_word]

        # Collect unique letters
        unique_letters = sorted(list(set("".join(all_words))))

        if len(unique_letters) > 10:
            return f"Invalid puzzle: Too many unique letters ({len(unique_letters)}). Only 10 digits (0-9) are available."

        # Identify leading letters of multi-digit numbers (cannot be zero)
        first_letters_of_multi_digit_words = set()
        for word in all_words:
            if len(word) > 1:
                first_letters_of_multi_digit_words.add(word[0])

        digits = range(10)
        
        # Try all permutations of digits for the unique letters
        for p in itertools.permutations(digits, len(unique_letters)):
            letter_to_digit_map = dict(zip(unique_letters, p))
            
            # Constraint: Leading letters of multi-digit numbers cannot be zero
            has_leading_zero_issue = False
            for first_letter in first_letters_of_multi_digit_words:
                if letter_to_digit_map[first_letter] == 0:
                    has_leading_zero_issue = True
                    break
            if has_leading_zero_issue:
                continue

            # Convert words to numbers using the current mapping
            try:
                operand_values = []
                for word in operand_words:
                    num_str = "".join(str(letter_to_digit_map[char]) for char in word)
                    operand_values.append(int(num_str))
                
                result_str = "".join(str(letter_to_digit_map[char]) for char in result_word)
                result_value = int(result_str)

                # Check if the arithmetic equation holds
                if sum(operand_values) == result_value:
                    # Format the solution string
                    solution_map_str = ", ".join(f"{k}={v}" for k, v in sorted(letter_to_digit_map.items()))
                    
                    num_operands_str = " + ".join(str(val) for val in operand_values)
                    equation_with_numbers = f"{num_operands_str} = {result_value}"
                    
                    return f"Solution: {{ {solution_map_str} }} -> {equation_with_numbers}"
            except ValueError: # Should not happen if logic is correct, but as a safeguard
                continue
                
        return "No solution found."
    except Exception as e:
        return f"An unexpected error occurred: {str(e)}"

if __name__ == "__main__":
    puzzles_to_solve = [
        "SEND + MORE = MONEY",
        "TWO + TWO = FOUR",
        "EAT + THAT = APPLE",
        "A + B = C", # Simple case, many solutions
        "WRONG + WRONG = RIGHT", # Known puzzle
        "SO + MANY + MORE + MEN + SEEM + TO + SAY + THAT + THEY + MAY + SOON + TRY + TO + STAY + AT + HOME + SO + AS + TO + SEE + OR + HEAR + THE + SAME + ONE + MAN + TRY + TO + MEET + THE + TEAM + ON + THE + MOON + AS + HE + HAS + AT + THE + OTHER + TEN = TESTS" # Very long, likely too many unique letters
    ]

    for puzzle in puzzles_to_solve:
        print(f"Solving: {puzzle}")
        solution = solve_cryptarithmetic(puzzle)
        print(solution)
        print("-" * 30)

    # Example with 10 unique letters that has a known solution
    # DONALD + GERALD = ROBERT (D=5, O=2, N=6, A=4, L=8, G=1, E=9, R=7, B=3, T=0)
    # 526485 + 197485 = 723970 -> This is incorrect. The famous solution is D=5, O=2, N=6, A=4, L=8, G=1, E=9, R=7, B=3, T=0
    # DONALD (526485) + GERALD (197485) != ROBERT (723970)
    # The actual solution for DONALD + GERALD = ROBERT is:
    # D=5, O=2, N=6, A=4, L=8, G=1, E=9, R=7, B=3, T=0
    #   526485
    # + 197485
    # --------
    #   723970  -- This is not ROBERT (723970) if R=7, O=2, B=3, E=9, R=7, T=0. It should be 723970.
    # Let's recheck the famous solution for DONALD + GERALD = ROBERT
    # D=5, O=2, N=6, A=4, L=8, G=1, E=9, R=7, B=3, T=0.
    # DONALD = 526485
    # GERALD = 197485
    # ROBERT = 723970
    # 526485 + 197485 = 723970. This is correct. R=7, O=2, B=3, E=9, R=7, T=0. ROBERT = 723970.
    # The letters are D,O,N,A,L, G,E,R,B,T. All unique and 10 of them.
    # My code should find this if it's correct.

    print("Solving: DONALD + GERALD = ROBERT")
    solution_donald = solve_cryptarithmetic("DONALD + GERALD = ROBERT")
    print(solution_donald)
    print("-" * 30)

    print("Solving: CROSS + ROADS = DANGER") # 9 unique letters
    solution_cross = solve_cryptarithmetic("CROSS + ROADS = DANGER")
    print(solution_cross)
    print("-" * 30)


