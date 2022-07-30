from pprint import pprint
from sudokugenerator import*
import csv
import time

empty_squares = 0
valid_num_placed = 0
num_of_backtrack = 0
num_of_guess = 0


def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    # keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):  # range(9) is 0, 1, 2, ... 8
            if puzzle[r][c] == -1:
                return r, c

    return None, None  # if no spaces in the puzzle are empty (-1)


def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at the row/col of the puzzle is a valid guess
    # returns True or False

    # for a guess to be valid, then we need to follow the sudoku rules
    # that number must not be repeated in the row, column, or 3x3 square that it appears in

    # let's start with the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False  # if we've repeated, then our guess is not valid!

    # now the column
    # col_vals = []
    # for i in range(9):
    #     col_vals.append(puzzle[i][col])
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # and then the square
    row_start = (row // 3) * 3  # 10 // 3 = 3, 5 // 3 = 1, 1 // 3 = 0
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    global empty_squares
    global valid_num_placed, num_of_backtrack, num_of_guess

    # solve sudoku using backtracking!
    # our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    # return whether a solution exists
    # mutates puzzle to be the solution (if solution exists)

    # step 1: choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # step 1.1: if there's nowhere left, then we're done because we only allowed valid inputs
    if row is None:  # this is true if our find_next_empty function returns None, None
        return True

        # step 2: if there is a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):  # range(1, 10) is 1, 2, 3, ... 9
        # step 3: check if this is a valid guess
        num_of_guess += 1
        if is_valid(puzzle, guess, row, col):
            # step 3.1: if this is a valid guess, then place it at that spot on the puzzle
            puzzle[row][col] = guess
            valid_num_placed += 1

            # step 4: then we recursively call our solver!
            if solve_sudoku(puzzle):
                empty_squares += 1
                return True

        # step 5: if not valid or if nothing gets returned true, then we need to backtrack and try a new number
        puzzle[row][col] = -1
        num_of_backtrack += 1
    # step 6: if none of the numbers that we try work, then this puzzle is UNSOLVABLE!!
    return False


if __name__ == '__main__':
    print("Welcome to Group 3's Sudoku Generator and Independent Solver Program. This program aims to generate a set of Sudoku Puzzle to be solved by our Program Solver. It will then generate statistics and write it into a CSV file. Please choose a difficulty from 1 - 60 for the amount of blanks (grid without numbers) you want in the puzzle.")

    while True:
        question_board = generateBoard()
        input("Press Enter to continue...")
        print("===================================================================\n")
        print("Solution by Solver:")
        start = time.time()
        solve_sudoku(question_board)
        end = time.time()
        pprint(question_board)
        print()
        time_taken = round((end - start)*10000000)
        print(f"Time taken: {time_taken} ns")
        print(f"Valid number placed in cell = {valid_num_placed}")
        print(f"Number of backtracks = {num_of_backtrack}")
        print(f"Number of guesses made = {num_of_guess}")
        print(f"For {empty_squares} empty Squares\n")
        with open('statistics.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)

            with open('statistics.csv', 'a') as f:
                writer = csv.writer(f, delimiter=',')
                data = [[empty_squares], [time_taken], [valid_num_placed], [num_of_backtrack], [num_of_guess]]
                writer.writerow(data)
        if num_of_backtrack > 2400:
            print("The difficulty is very high. Suggest decreasing the difficulty. ")
        elif num_of_backtrack > 890:
            print("The difficulty is a little high. Suggest decreasing the difficulty. ")
        elif num_of_backtrack > 250:
            print("The difficulty is a little low. Suggest increasing the difficulty. ")
        else:
             print("The difficulty is a very low. Suggest increasing the difficulty. ")

        while True:
            answer = str(input('Do you want to run the program again? (y/n): '))
            if answer in ('y', 'n'):
                break
            print("invalid input.")
        if answer == 'y':
            empty_squares = 0
            valid_num_placed = 0
            num_of_backtrack = 0
            num_of_guess = 0
            print("\n\n")
            continue
        else:
            print("\nThank you for using our Sudoku Program. Goodbye!")
            break
