#Valid Sudoku
from collections import defaultdict
def is_valid_sudoku(board: list[list[str]])-> bool:
    squares=defaultdict(set)
    row_set=defaultdict(set)
    col_set=defaultdict(set)
    for row_idx,row in enumerate(board):
        for col_idx,col in enumerate(board[row_idx]):
            if board[row_idx][col_idx] == ".":
                continue
            if board[row_idx][col_idx] not in row_set[(row_idx,col_idx)]:
                row_set[(row_idx,col_idx)].add(board[row_idx][col_idx])
            elif board[row_idx][col_idx] in row_set[(row_idx,col_idx)]:
                return False   
            
            if board[col_idx][row_idx] not in col_set[(col_idx,row_idx)] :
                col_set[(col_idx,row_idx)].add(board[col_idx][row_idx])
            elif board[col_idx][row_idx] in col_set[(col_idx,row_idx)] :
                return False  
            
            if board[row_idx][col_idx] in squares[(row_idx//3,col_idx//3)]:
                return False
            elif board[row_idx][col_idx] not in squares[(row_idx//3,col_idx//3)]:
                squares[(row_idx//3,col_idx//3)].add(board[row_idx][col_idx])
                       
    return True        
            
if __name__=="__main__":
 board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
 
 print(is_valid_sudoku(board))
    
    