import os
import time

import random

class Puzzle:
    def __init__(self):
        self.board = [[0]*9 for _ in range(9)]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_board(self):
        # Print the Sudoku board in the desired format
        self.clear_screen()
        separator_line = "=" * 41

        def print_separator():
            print(separator_line)

        print_separator()
        for i in range(9):
            row = []
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    row.append("|")
                if j == 0:
                    row.append(f"|| {self.board[i][j] if self.board[i][j] != 0 else ' '} ")
                else:
                    row.append(f"| {self.board[i][j] if self.board[i][j] != 0 else ' '} ")
            row.append("||")
            print("".join(row))
            if (i + 1) % 3 == 0:
                print_separator()
            else:
                print("-" * 41)

                    
    def is_valid(self, num, pos):
        row, col = pos

        # Check row
        for j in range(9):
            if self.board[row][j] == num and col != j:
                return False

        # Check column
        for i in range(9):
            if self.board[i][col] == num and row != i:
                return False

        # Check subgrid
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x*3, box_x*3 + 3):
                if self.board[i][j] == num and (i, j) != pos:
                    return False

        return True
    
    def generate_puzzle(self, fill_count):
        if (fill_count < 14 or fill_count > 63):
            raise ValueError(f"Fill count needs to be between 14 and 63")
        
        self.board = [[0]*9 for _ in range(9)]
        for _ in range(fill_count):
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            num = random.randint(1, 9)
            while not self.is_valid(num, (row, col)) or self.board[row][col] != 0:
                row = random.randint(0, 8)
                col = random.randint(0, 8)
                num = random.randint(1, 9)
            self.board[row][col] = num
            self.clear_screen()
            self.print_board()
            time.sleep(0.05)