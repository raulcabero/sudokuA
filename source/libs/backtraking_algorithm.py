import time

from algorithm import Algorithm

class BacktrakingAlgorithm(Algorithm):
    
    def __init__(self, sudoku_to_solve, empty_spot_char):
        """Constructor BacktrakingAlgorithm which solve a sudoku using
           Algorithm Backtraking.

        Keyword arguments:
        sudoku_to_solve -- the string raw data of the sudoku to solve
        empty_spot_char -- the string character which represents the place to need
                     filled in the sudoku
        
        """   
        super(BacktrakingAlgorithm, self).__init__(sudoku_to_solve, empty_spot_char)
        # a matrix[][] which contain the soduku to solve 
        self.grid = self.get_grid_values(sudoku_to_solve)

    def solve_sudoku(self):
        """Returns the solution to sudoku in a matrix[][] using the
           Backtraking Algorithm.
           
        """
        # validate is the sudoku raw data is valid
        if self.sudoku_data_is_valid() == False:
            raise Exception("The sudoku input is incorrect")
        # starts the timing of the sudoku solution
        self.start_tim = time.clock()
        # starts the bactraking algoritm
        if not self.is_sudoku_solve(self.grid):
            raise Exception("The sudoku could not be solved")
        # stop the timing
        self.end_time = time.clock()
        return self.grid
   
    def get_grid_values(self, grid_sudoku):
        """Converts a string sudoku raw data in a matrixm.
           Returns a matrix [][]
           
           Keyword arguments:
           grid_sudoku -- the string raw data of the sudoku to solve
            
        """
        chars = [c for c in grid_sudoku if c in self.digits\
                 or c in self.empty_spot_char]
        new_grid_sudoku = []  # the new matrix [][]    
        value = -1  # the current row in the new matrix [][]
        for i in range (0, len(chars)):
            if i/self.size_sudoku > value:
                new_grid_sudoku.append([])
                value = i / self.size_sudoku
            new_grid_sudoku[value].append(chars[i])
        return new_grid_sudoku
    
    def is_sudoku_solve(self, grid_sudoku):
        """Solve sudoku using Backtraking Algorithm.
           Returns a matrix[][] which contains the solution to Sudoku
           
           Keyword arguments:
           grid_sudoku -- the matrix[][] of the sudoku to solve
            
        """
        # current row of the grid_sudoku matrix
        row = 0
        # current col of the grid_sudoku matrix
        col = 0
        # flag to see if a location does not have a value
        unassigned_location = False
        # if there is no unassigned location, sudoku is solved
        row, col, unassigned_location = self.find_unassigned_location\
                                        (grid_sudoku)
        if not unassigned_location:
            return True  # sudoku solve success
        for num in range (1 ,self.size_sudoku + 1):
            # looks if the num is good to replace an empty place
            if (self.is_safe(grid_sudoku, row, col, num)):
                # make tentative assigement
                grid_sudoku[row][col] = str(num)
                # return if success
                if(self.is_sudoku_solve(grid_sudoku)):
                    return True
                # failure unmake & try again
                else:
                    grid_sudoku[row][col] = str(self.empty_spot_char)        
        return False
     
    def find_unassigned_location(self, grid_sudoku):
        """Searches the grid to find an entry that is still unassigned. If          
           found, the reference parameters row, col will be set the location
           that is unassigned, and true is returned plus the current row and
           col of the unassigned location. If no unassigned entries remain,
           false is returned.
           
           Keyword arguments:
           grid_sudoku -- the matrix[][] of the sudoku to solve
            
        """
        for row in range (0, self.size_sudoku):
            for col in range (0, self.size_sudoku):
                if (grid_sudoku[row][col] == self.empty_spot_char):
                    return row, col, True
        return row, col, False

    def used_in_row(self, grid_sudoku, row_sudoku,num):
        """Returns boolean which indicates whether any assigned entry
           in the specified row matches the given number..
           
           Keyword arguments:
           grid_sudoku -- the matrix[][] of the sudoku to solve
           row_sudoku -- the row of the sudoku to perform the search
           num -- the number to verify if it is already in the specified row
            
        """
        for col in range(0, self.size_sudoku):
            if (grid_sudoku[row_sudoku][col] == str(num)):
                return True
        return False

    def used_in_col(self, grid_sudoku, col_sudoku,num):
        """Returns a boolean which indicates whether any assigned entry
           in the specified column matches the given number.
           
           Keyword arguments:
           grid_sudoku -- the matrix[][] of the sudoku to solve
           col_sudoku -- the col of the sudoku to perform the search
           num -- the number to verify if it is already in the specified col
            
        """
        for row in range (0, self.size_sudoku):
            if (grid_sudoku[row][col_sudoku] == str(num)):
                return True
        return False

    def used_in_box(self, grid_sudoku, box_start_row, box_start_col, num):
        """Returns a boolean which indicates whether any assigned entry
           within the specified 3x3 box matches the given number.

           Keyword arguments:
           grid_sudoku -- the matrix[][] of the sudoku to solve
           box_start_row -- the start row of the square 3x3
           box_start_col -- the start col of the square 3x3
           num -- the number to verify if it is already in the specified
                  square 3x3
                  
        """
        for row in range(0, 3):
            for col in range(0, 3):
                if(grid_sudoku[row + box_start_row] [col + box_start_col] == str(num)):
                    return True
        return False

    def is_safe(self, grid, row, col, num):
        """Check if 'num' is not already placed in current row, current column
           and current 3x3 box.
           Returns a boolean which indicates whether it will be legal to assign
           num to the given row,col location

           Keyword arguments:
           grid -- the matrix[][] of the sudoku to solve
           row --  the row to perform the search
           col --  the col to perform the search
           num --  the number to verify if it is already in the specified
                   square 3x3, specified col and specified row
                  
        """
        return not self.used_in_row(grid, row, num)\
               and not self.used_in_col(grid, col, num)\
               and not self.used_in_box(grid, row - row % 3, col - col % 3, num)

    
    def printGrid(self, grid):
        """Print a grid

           Keyword arguments:
           grid -- the matrix[][] of the sudoku to print
                  
        """
        for row in range(0, self.size_sudoku):
            print grid[row]

