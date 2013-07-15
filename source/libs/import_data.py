import os
from csv_handler import CSVHandler
from cmd_handler import CMDHandler

class ImportData:
    extension_file_csv = ".csv"
    
    def __init__(self):
        """
        Contructor class Import Data class in charge to import sudokus
        data from different inputs such as csv or txt
        """
        self.csv_handler = CSVHandler()
        self.cmd_handler = CMDHandler()
    
    def read_sudoku_data_from_file(self, sudoku_file):
        """
        Read the sudoku data form files such as csv or txt
        Returns False if the data are invalid or the file was not
        able to read, return a matrix[][] wihich contains all the
        sudoku data and their sudoku size

        Keyword arguments:
        sudoku_file -- the path of the file which contains the
                       sudoku data

        """
        ext = self.get_extension_file(sudoku_file)
        matrix_sudoku = []
        if ext == self.extension_file_csv:
            matrix_sudoku = self.csv_handler.get_rows_sudoku_data(sudoku_file, ",")
        return matrix_sudoku

    def read_sudoku_data_from_line(self, line):
        """
        Read the sudoku data form a line entered form comand line
        Return a matrix[][] wihich contains the sudoku data and
        its sudoku size

        Keyword arguments:
        line -- the line string entered by the user

        """
        matrix_sudoku = self.cmd_handler.get_rows_sudoku_data(line)
        return matrix_sudoku
    
    def get_extension_file(self, filename):
        """
        Gess the extension of a given filename

        Keyword arguments:
        filename -- the filename to guess the extention

        """
        double_extensions = ['tar.gz', 'tar.bz2']
        root , ext = os.path.splitext(filename)
        if any([filename.endswith(x) for x in double_extensions]):
            root, first_ext = os.path.splitext(root)
            ext = first_ext + ext
        return ext

