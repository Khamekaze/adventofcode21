class Board:

    def __init__(self):
        self.matrix = [[0 for x in range(5)] for y in range(5)]
        self.bingo_checks = [[0 for x in range(5)] for y in range(5)]
        self.bingo = False
        self.index = 0
        self.winning_num = 0
        self.unmarked_sum = 0

    def get_bingo(self):
        return self.bingo

    def set_index(self, index):
        self.index = index

    def check_current_num(self, num):
        for y in range(5):
            for x in range(5):
                if self.matrix[y][x] == str(num):
                    self.bingo_checks[y][x] = 1

        #Check rows
        for y in range(5):
            row_hits = 0
            for x in range(5):
                if self.bingo_checks[y][x] == 1:
                    row_hits += 1
                if row_hits == 5:
                    self.bingo = True
                    self.winning_num = num
                    break

        #Check cols
        for x in range(5):
            col_hits = 0
            for y in range(5):
                if self.bingo_checks[y][x] == 1:
                    col_hits += 1
                if col_hits == 5:
                    self.bingo = True
                    self.winning_num = num
                    break

        return self.bingo

    def calculate_unmarked_sum(self):
        sum = 0
        for y in range(5):
            for x in range(5):
                if self.bingo_checks[y][x] == 0:
                    sum = sum + int(self.matrix[y][x], base=10)
        self.unmarked_sum = sum
        return sum


def check_boards(boards, numbers):
    index = 0
    winning_board = Board()
    while index < len(numbers):
        for b in boards:
            bingo = b.check_current_num(numbers[index])
            if bingo:
                index = len(numbers)
                winning_board = b
                break
        index += 1
    return winning_board


def check_last_winning_board(boards, numbers):
    index = 0
    last_winning_board = Board()
    while index < len(numbers):
        for i in range(len(boards)):
            board = boards[i]
            if board.bingo == False:
                bingo = board.check_current_num(numbers[index])
                if bingo:
                    last_winning_board = board
        index += 1

    return last_winning_board.index


def create_boards():
    boards = []
    with open('inputs/day4/day4_boards_compressed.txt') as file:
        lines = file.readlines()
        board_index = 0
        while board_index < (len(lines)):
            new_board = Board()
            for y in range(5):
                current_line = lines[y + board_index]
                nums = current_line.split()
                for x in range(5):
                    new_board.matrix[y][x] = nums[x]
            boards.append(new_board)
            board_index += 5

    for i in range(len(boards)):
        boards[i].set_index(i)
    return boards


def read_numbers():
    nums = []
    with open('inputs/day4/day4_input.txt') as file:
        line = file.readlines()
        numbers = line[0].split(',')
        nums = [0] * len(numbers)
        for i in range(len(numbers)):
            num = int(numbers[i], base=10)
            nums[i] = num

    return nums


if __name__ == '__main__':
    boards = create_boards()
    nums = read_numbers()
    winning_board = check_boards(boards, nums)
    winning_num = winning_board.winning_num
    unmarked_sum = winning_board.calculate_unmarked_sum()
    final_score = winning_num * unmarked_sum
    print('Final score for winning board: ' + str(final_score))

    last_winning_board_index = check_last_winning_board(boards, nums)
    last_winning_board = boards[last_winning_board_index]
    last_winning_num = last_winning_board.winning_num
    last_unmarked_sum = last_winning_board.calculate_unmarked_sum()
    last_final_score = last_winning_num * last_unmarked_sum
    print('Last final score: ' + str(last_final_score))
