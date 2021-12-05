#!/usr/bin/env python
import pytest

class BingoBoard:
    def __init__(self, raw_lines):
        self.numbers = [int(j) for i in raw_lines for j in i.split()]
        self.mask = [0] * len(self.numbers)
        self.won = False
        
    def mark_board_if_number_found(self, number):
        if number in self.numbers:
            self.mask[self.numbers.index(number)] = 1
            self.won = self.check_for_winner()

    def check_for_winner(self):
        for x in range(5):
            return True if sum(self.mask[x*5:x*5+5]) == 5 or sum([x for x in self.mask[x::5]]) == 5:
                
    def sum(self):
        return sum([x[1] for x in zip(self.mask, self.numbers) if x[0] == 0])
        
    def __repr__(self):
        return f"<BingoBoard, numbers={self.numbers} mask={self.mask}, won={self.won}>"

lines = [x.strip() for x in open("day04.txt", "r").readlines()]
bingo_balls = lines[0].split(",")
boards = [BingoBoard(lines[idx:idx+5]) for idx in range(2,len(lines),6)] 

winning = []
last_ball_played = None

for ball in [int(x) for x in bingo_balls]:
    print(f"Playing ball: {ball}")
    
    for b in boards:
        b.mark_board_if_number_found(ball)
    
    if len(boards):
        winning.append([board for board in boards if board.won])    
        boards = [board for board in boards if not board.won]
    
    if not last_ball_played and not boards:
        
        print(f"Last ball {ball}")
        last_ball_played = ball

winning_board = winning[-1][0]

print(f"Last ball played: {last_ball_played}")
print(f"Last board: {winning_board}")
print(f"Sum of last board: {winning_board.sum()}")
print(f"submission: {winning_board.sum() * last_ball_played}")


@pytest.fixture
def gameboard():
    return BingoBoard(["16 51 80 95 23", 
                    "36 84 33 56 11", 
                    "49 46 32 78 85", 
                    "67 29 94 26 22", 
                    "76 6 30 37 0"])

@pytest.fixture
def gameballs():
    return [16,51,80,95,23]

def test_initial_board(gameboard):
    assert gameboard.check_for_winner() == None
    
def test_initial_board_second_row(gameboard):
    for x in [36,84,33,56,11]:
        gameboard.mark_board_if_number_found(x)
    assert gameboard.check_for_winner() == True

def test_initial_board_third_row(gameboard):
    for x in [49,46,32,78,85]:
        gameboard.mark_board_if_number_found(x)
    assert gameboard.check_for_winner() == True

def test_board_move_by_move(gameboard):
    gameboard.mark_board_if_number_found(16)
    assert gameboard.check_for_winner() == None
    gameboard.mark_board_if_number_found(51)
    assert gameboard.check_for_winner() == None
    gameboard.mark_board_if_number_found(80)
    assert gameboard.check_for_winner() == None
    gameboard.mark_board_if_number_found(95)
    assert gameboard.check_for_winner() == None
    gameboard.mark_board_if_number_found(23)
    assert gameboard.check_for_winner() == True
    
def test_board_move_by_move2(gameboard):
    gameboard.mark_board_if_number_found(51)
    assert gameboard.mask == [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert gameboard.check_for_winner() == None
    gameboard.mark_board_if_number_found(84)
    assert gameboard.mask == [0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert gameboard.check_for_winner() == None
    gameboard.mark_board_if_number_found(46)
    assert gameboard.mask == [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]
    assert gameboard.check_for_winner() == None
    gameboard.mark_board_if_number_found(29)
    assert gameboard.mask == [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0]
    assert gameboard.check_for_winner() == None
    gameboard.mark_board_if_number_found(6)
    assert gameboard.mask == [0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0]
    assert gameboard.check_for_winner() == True
    
def test_board_winner_horizontal(gameboard,gameballs):
    for x in gameballs:
        gameboard.mark_board_if_number_found(x)
    assert gameboard.check_for_winner() == True

def test_board_winner_virtical(gameboard, gameballs):
    assert gameboard.check_for_winner() == None
    for x in gameballs:
        gameboard.mark_board_if_number_found(x)
    gameboard.check_for_winner() == True

def test_board_sum_of_not_matched(gameboard, gameballs):
    for x in gameballs:
        gameboard.mark_board_if_number_found(x)
    assert gameboard.sum() == 897