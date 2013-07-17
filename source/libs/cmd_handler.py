import math

class CMDHandler:

    invalid_sudoku_size = -1

    def get_rows_sudoku_data(self, data):
        """
        Get the sudoku data and the size from the data introduced by the user
        from comand line.
        Returns a matrix[][] which contains the sudoku in the correct format
        to solve and the size of the sudoku to solve

        Keyword arguments:
        data -- the string which contains the sudoku in a line entered
                by cmd line

        """
        sudoku_data = []
        sudokus = []
        new_data = ""
        for character in data:
            if character != '\n' and character != " ":
                new_data = new_data + character
        size_sudoku = math.sqrt(len(new_data))
        if size_sudoku % 1 > 0:
            size_sudoku = self.invalid_sudoku_size
        else:
            size_sudoku = int(size_sudoku)
            new_data = self.add_new_lines(new_data, size_sudoku)
        sudoku_data.append(new_data)
        sudoku_data.append(size_sudoku)
        sudokus.append(sudoku_data)
        return sudokus

    def add_new_lines(self, data, add_in_character_num):
        """
        Given a sudoku data it adds new lines to the data in
        order to disting each row of the sudoku to solve
        Returns the data of sudoku with the correct format to solve the sudoku

        Keyword arguments:
        data -- the string which contains the sudoku in a line entered
                by cmd line
        add_in_character_num -- the integer which represents the position where
                                a new line must be added to the data of sudoku

        """
        new_data = ""
        for i in range(0, len(data)):
            if i % add_in_character_num == 0 and i != 0:
                new_data = new_data + "\n" + data[i]
                continue
            new_data = new_data + data[i]
        return new_data + "\n"
        
        
