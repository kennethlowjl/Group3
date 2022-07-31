base  = 3
side  = base*base


def generateBoard():
    empties = 0
    while True:
        try:
            empties = int(input("Choose your difficulty from 1 - 60: "))

        except ValueError:
            print("Invalid input")
            continue
        if empties in range(1, 61):
            break
        print("Invalid input")
    if empties == range(1,61):
        return empties

    def pattern(r,c): return (base*(r%base)+r//base+c)%side

    from random import sample
    def shuffle(s): return sample(s,len(s))
    rBase = range(base)
    rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
    cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
    nums  = shuffle(range(1,base*base+1))

    board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
    print()
    print("First Board with Answers:")
    print("----------------------------")

    for line in board: print(line)
    print("----------------------------\n")

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

    for i in range(len(new_board)):
        if new_board[i] == 0:
            new_board[i] = -1

    def divide_chunks(l, n):
        # looping till length l
        for i in range(0, len(l), n):
            yield l[i:i + n]

    x = list(divide_chunks(new_board, 9))
    print("---------------------------\n")
    return x



