base  = 3
side  = base*base

def generateBoard():

    empties = int(input("Choose your difficulty from 1 - 60: "))

    # pattern for a baseline valid solution
    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    # randomize rows, columns and numbers (of valid base pattern)
    from random import sample
    def shuffle(s): return sample(s,len(s))
    rBase = range(base)
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    # produce board using randomized baseline pattern
    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    print()
    print("First Board with Answers:")
    print("----------------------------")

    for line in board: print(line)
    print("----------------------------")
    print()



    #Creating the puzzle with empty blanks
    new_board = []
    squares = side*side
    empties = empties
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0

    print(f"First Board with {empties} Blanks:")
    print("---------------------------")
    numSize = len(str(side))
    for line in board:
        print(*(f"{n or '.':{numSize}} " for n in line))
        for i in line:
            new_board.append(i)
    # print (new_board)


    #Converting Board with 0s to -1s for solver to read
    for i in range(len(new_board)):
        if new_board[i] == 0:
            new_board[i] = -1


    # Dividing the entire list into a list containing lists of 9 variables
    def divide_chunks(l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]


    # How many elements each
    # list should have

    x = list(divide_chunks(new_board, 9))
    print("---------------------------")
    print()
    return x



