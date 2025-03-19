import time 
import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")


def is_valid_state(board: list[list[int]],row:int,col:int,new_num:str)-> bool:
    for i in range(9):
        if board[row][i]==new_num or board[i][col]==new_num:
            return False
    subgrid_row,subgrid_col=(row//3)*3,(col//3)*3
    for i in range(3):
        for j in range(3):
            if board[subgrid_row+i][subgrid_col+j]==new_num:
                return False     
    return True

def print_board(board: list[list[int]])->None:
    clear_console()
    for idx,row in enumerate(board):
        if idx%3==0 and idx!=0:
            print("-"*18)
        print(" ".join(row[0:3])+"|"+" ".join(row[3:6])+"|"+" ".join(row[6:9]))
    time.sleep(0.001)    

def is_empty_cell(board: list[list[int]]):
    for i in range(9):
        for j in range(9):
            if board[i][j]==".":
                return i,j
    return None        
    

def solve_sudoku(board:list[list[int]])-> None:
    print_board(board)
    empty=is_empty_cell(board)
    if not empty:
        return True
    row,col=empty
    for sol in range(1,10):
        if is_valid_state(board,row,col,str(sol)):
            board[row][col]=str(sol)
            print_board(board)
            if solve_sudoku(board):
                return True
        board[row][col]="."  
        print_board(board)  
    return False    

if __name__=="__main__":
    
    board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
    
    start_time=time.perf_counter()
    
    if solve_sudoku(board):
        print("Sudoku board solvable")
    else:
        print("Sudoku board not solvable")   
    
    end_time=time.perf_counter()
    total_time=end_time-start_time
    print(f"Total time taken to solve is {total_time:.2f}s")        