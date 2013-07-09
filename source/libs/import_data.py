import os
from csv_import import CSVImport

class ImportData:
    extension_file_csv = ".csv"
    
    def __init__(self):
        """
        Contructor class Import Data class in charge to import sudokus
        data from different inputs such as csv or txt
        """
        self.csv_handler = CSVImport()
    
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
        root, ext = self.guess_extension(sudoku_file)
        res = []
        if ext == self.extension_file_csv:
            res = self.csv_handler.get_rows_sudoku_data(sudoku_file, ",")
        if len(res) > 0:
            if res[0][1] != -1:
                return res
            else:
                return False
        else:
            return False

    def guess_extension(self, filename):
        """
        Gess the extension of a given filename

        Keyword arguments:
        filename -- the filename to guess the extention

        """
        double_extensions = ['tar.gz', 'tar.bz2']
        root,ext = os.path.splitext(filename)
        if any([filename.endswith(x) for x in double_extensions]):
            root, first_ext = os.path.splitext(root)
            ext = first_ext + ext
        return root, ext

