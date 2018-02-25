class ChessBoard(object):
    
    def __init__(self):
        # This is an dictionary to hold the chess table and it's value
        self.boardArray = {
                 1 : { 1: [0,''] , 2: [0,''], 3: [0,''], 4: [0,''], 5: [0,''], 6: [0,''], 7: [0,''] , 8: [0,'']},
                 2 : { 1: [0,''] , 2: [0,''], 3: [0,''], 4: [0,''], 5: [0,''], 6: [0,''], 7: [0,''] , 8: [0,'']},  
                 3 : { 1: [0,''] , 2: [0,''], 3: [0,''], 4: [0,''], 5: [0,''], 6: [0,''], 7: [0,''] , 8: [0,'']},
                 4 : { 1: [0,''] , 2: [0,''], 3: [0,''], 4: [0,''], 5: [0,''], 6: [0,''], 7: [0,''] , 8: [0,'']},
                 5 : { 1: [0,''] , 2: [0,''], 3: [0,''], 4: [0,''], 5: [0,''], 6: [0,''], 7: [0,''] , 8: [0,'']},
                 6 : { 1: [0,''] , 2: [0,''], 3: [0,''], 4: [0,''], 5: [0,''], 6: [0,''], 7: [0,''] , 8: [0,'']},
                 7 : { 1: [0,''] , 2: [0,''], 3: [0,''], 4: [0,''], 5: [0,''], 6: [0,''], 7: [0,''] , 8: [0,'']},
                 8 : { 1: [0,''] , 2: [0,''], 3: [0,''], 4: [0,''], 5: [0,''], 6: [0,''], 7: [0,''] , 8: [0,'']},
            }
    # Populates the board with the queen, insuring that it will not be attacked.
    def placeQueen(self, delete_boolean=False, position=None):

        check=0; operation=1; verify_value=0; place_value ='Q'
         
        if delete_boolean == True:
            check = 1; operation = -1; verify_value='Q'; place_value = ''     
            
        #Check to make sure we can unpack the tuple
        if(len(position)> 2):
            return(False)
        # Unpack the tuple to evaluate row and column respectively
        row, col = tuple((position).lower())
        
        # Map to numbers between (1-5)
        row = int(row); col = ord(col) - 96
        
        #check boundaries
        if(8 < row < 1 | 8 < col < 1):
            return(False)
    
        # Verify Variable: check 
        verify = self.boardArray[col][row][check]
        
        # Check if the player may place here 
        if verify == verify_value:
            
            #Place the Queen in the position given
            self.boardArray[col][row][1] = place_value
            
            # When a Queen is placed the whole row and column is taken
            for i in range(1,9):
                self.boardArray[i][row][0] += operation
                self.boardArray[col][i][0] += operation
            
            # We then create the diagonals
            pattern_list = [(9,9,1,1),(0,0,-1,-1),(9,0,+1,-1),(0,9,-1,+1)]
            for i in range(0,4):
                row_temp, col_temp = row, col
                row_condition, col_condition, row_operation, col_operation = pattern_list[i]
                while(row_temp != row_condition and col_temp != col_condition):
         
                    self.boardArray[col_temp][row_temp][0] += operation
                    (row_temp, col_temp) = (row_temp + row_operation, col_temp + col_operation)
            return(True)
        
        else:
            return(False)

    def RemoveQueen(self, position):
        
        self.placeQueen(delete_boolean=True, position=position)
        
    #Print the boards values
    def PrintBoard(self):
        print("="*60)
        for col_temp in self.boardArray:
            print("\n")
            for row_temp in self.boardArray[col_temp]:
                if(self.boardArray[col_temp][row_temp][1] != ''):
                    print(self.boardArray[col_temp][row_temp][1], end="\t")
                else:
                    print("0", end="\t")
        print("\n","="*60)  
        



            
        