import os
from csv_handler import CSVHandler

class ImportData:
    extension_file_csv = ".csv"
    
    def __init__(self):
        """
        Contructor class Import Data class in charge to import sudokus
        data from different inputs such as csv or txt
        """
        self.csv_handler = CSVHandler()
    
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
        ext = self.guess_extension(sudoku_file)
        matrix_sudoku = []
        if ext == self.extension_file_csv:
            matrix_sudoku = self.csv_handler.get_rows_sudoku_data(sudoku_file, ",")
        if len(matrix_sudoku) > 0:
            if matrix_sudoku[0][1] != -1:
                return matrix_sudoku
        return matrix_sudoku

    def guess_extension(self, filename):
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

