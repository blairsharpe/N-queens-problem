'''
Created on Jul 7, 2017

@author: bsharpe

Algorithm:
1) Start in the leftmost column
2) If all queens are placed
    return true
3) Try all rows in the current column.  Do following for every tried row.
    a) If the queen can be placed safely in this row then mark this [row, 
        column] as part of the solution and recursively check if placing  
        queen here leads to a solution.
    b) If placing queen in [row, column] leads to a solution then return 
        true.
    c) If placing queen doesn't lead to a solution then umark this [row, 
        column] (Backtrack) and go to step (a) to try other rows.
3) If all rows have been tried and nothing worked, return false to trigger 
    backtracking.
'''
from ChessBoard import ChessBoard
from Stack import Stack


ChessBoard_object = ChessBoard()
Stack_object = Stack()

list_of_positions = [ 
                    ["8H", "8G", "8F", "8E", "8D", "8C", "8B", "8A"],
                    ["7H", "7G", "7F", "7E", "7D", "7C", "7B", "7A"],
                    ["6H", "6G", "6F", "6E", "6D", "6C", "6B", "6A"],
                    ["5H", "5G", "5F", "5E", "5D", "5C", "5B", "5A"],
                    ["4H", "4G", "4F", "4E", "4D", "4C", "4B", "4A"],
                    ["3H", "3G", "3F", "3E", "3D", "3C", "3B", "3A"],
                    ["2H", "2G", "2F", "2E", "2D", "2C", "2B", "2A"],
                    ["1H", "1G", "1F", "1E", "1D", "1C", "1B", "1A"]
                    ]               

def SolveNQueens():

# When you want to move down to the next row, you decrease
# When you want to move to the next column you increase cursor_colum by 1    
    place_verification = False
    cursor_colum = 0
    cursor_row = 7

    while(cursor_colum != 8):
    # We go until we completed all columns
           
        while(cursor_row <= -1):
                         
            popped_value = Stack_object.pop()
            cursor_colum, cursor_row = popped_value
            ChessBoard_object.RemoveQueen(position=list_of_positions[cursor_colum][cursor_row])
            cursor_row -= 1
      
        # 1) Start in the leftmost column, try all the rows in the current column
        place_verification = ChessBoard_object.placeQueen(position=list_of_positions[cursor_colum][cursor_row])     
          
        # If we can place then we put that coordinate unto the stack and place the queen
        if(place_verification == True):
              
            package = (cursor_colum, cursor_row)
            Stack_object.push(package)
            cursor_row = 7
            cursor_colum += 1 
              
        # If False, we move to the next row   
        else:
            cursor_row -= 1  
            
SolveNQueens()
ChessBoard_object.PrintBoard()
print("\nThe following is a solution:")
values = Stack_object.list_of_coordinates()
for c, r in values:
    print(list_of_positions[c][r], end=" | ")

        

    
        
        
  
        
        
        
