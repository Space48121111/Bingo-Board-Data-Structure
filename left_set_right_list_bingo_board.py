from __future__ import annotations
from typing import NamedTuple


input = '''\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
'''

'''
output:
4512 has_won: full row/column marked
[14 21 17 24  4] sum(unmarked) * marked

range(5) i j [j * 5 + i]

'''
class Board(NamedTuple):
    # key/index: val

    # instances:
    board_ints: list[int]
    board_left: set[int]

    @classmethod
    # factory function that will affect the class states
    # Board.parse instead of instances self.parse
    def parse(cls, board: str) -> Board:
        board_ints = [int(s) for s in board.split()] # between space
        # list: can repeat
        # set: unordered, exclusive, unique
        board_left = set(board_ints)
        return cls(board_ints, board_left)

    @property
    # interface of fget, fset, fdel, docstring
    # non-writable instances
    def has_won(self) -> bool:
        for i in range(5):
            for j in range(5):
                # out of loop for column
                if self.board_ints[i * 5 + j] in self.board_left:
                    break
            else:
                return True
            for i in range(5):
                if self.board_ints[j * 5 + i] in self.board_left:
                    break
            else:
                return True
        else:
            return False

first, *rest = input.split('\n\n')
boards = [Board.parse(board) for board in rest]
first_ints = [int(s) for s in first.split(',')]

def get_num() -> int:
    seen = set()
    last_winner = -1
    for num in first_ints:
        for board in boards:
                board.board_left.discard(num)
        '''
        for board in boards:
            if board.has_won:
                return sum(board.board_left) * num
        '''
        for i, board in enumerate(boards):
            if i not in seen and board.has_won:
                print(seen, board.board_left, num)
                last_winner = sum(board.board_left) * num
                seen.add(i)
    return last_winner

print(get_num())









# end
