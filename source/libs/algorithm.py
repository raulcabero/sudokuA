import time

class Algorithm(object):
    
    def __init__(self, sudoku_to_solve, character):
        """Contructor of Algorithm.

        Keyword arguments:
        sudoku_to_solve -- the raw data of the sudoku to solve
        character -- the character which represents the places to be filled
        """
        
        # the start time when the sudoku starts being solve
        self.start_time = 0.0
        # the end tine when the sudoku was solved
        self.end_time = 0.0
        self.sudoku_to_solve = sudoku_to_solve
        self.character = character

    def solve_sudoku(self):
        """Return the solution for the sudoku."""
        raise Exception("Implement the method")

    def generate_sudoku(self):
        """Generate a sudoku."""
        raise Exception("Implement the method")

    def sudoku_data_is_valid(self):
        """Verify that a sudoku data to solve contains the valid format for the
           algorithm.
           
        """
        raise Exception("Implement the method")

    def get_time(self):
        """Returns the time that takes to solve the sudoku."""
        return self.end_time - self.start_time
        
    def get_sudoku_to_solve(self):
        """Returns the sudoku to solve."""
        return self.sudoku_to_solve

    def set_sudoku_to_solve(self, new_sudoku_to_solve):
        """Set a new soduku to solve.

        Keyword arguments:
        new_sudoku_to_solve -- the new sudoku to solve

        """
        self.sudoku_to_solve = new_sudoku_to_solve
        #Set to initial values the times values
        self.start_time = 0.0   
        self.end_time = 0.0    
        
    

    
