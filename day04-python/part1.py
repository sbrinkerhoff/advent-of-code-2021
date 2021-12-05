#!/usr/bin/env python3

i = [x.strip() for x in open("day04.txt", "r").readlines()]


class bingo:
    def __init__(self, board):
        self.board = board
        self.mask = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

    def mark_ball(self,number):
        for count, board_line in enumerate(self.board):
            for count2, board_number in enumerate(board_line):
                #print(f"{count2}x{board_number}")
                if int(board_number) == int(number):
                    #print("setting mask value")
                    self.mask[count][count2] = 1
    
    def calculate_is_winner(self):
        winner = False
        for mask_line in self.mask:
            if sum(mask_line) == 5:
                winner = True
        # check the columns
        for x in range(5):
            if sum([self.mask[y][x] for y in range(5)]) == 5:
                winner = True
        return winner
    
    def calculate_value(self):
        sum = 0
        for line_number, line in enumerate(self.mask):
            for line_number2, line_value in enumerate(line):
                if line_value == 0:
                    sum += int(self.board[line_number][line_number2])
        return sum
        
    
balls = i[0].split(",")

boards = []
line_numbers = []
count = 0
for line in i[1:]:
    #print(count)
    #print(f"{line}")
    count +=1
    if count == 1:
        continue
    
    line_numbers.append(line.split())
    
    if count == 6:
        boards.append(bingo(line_numbers.copy()))
    
        count = 0
        line_numbers = []



winner = None
final_ball = None

for item in balls:
    print(item)
    for board_id, board in enumerate(boards):
        if not winner:
            board.mark_ball(item)
        if board.calculate_is_winner() and not winner:
            print("Winner is board {}".format(board_id))
            winner = board_id
            final_ball = item
            
sum = boards[winner].calculate_value()
print(f"Board sum is: {sum}")
print(f"Final ball is: {final_ball}")
print(f"Final ball value is: {int(final_ball)*int(final_ball)}")
