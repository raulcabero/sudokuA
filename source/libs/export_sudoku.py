from txt_handler import TXTHandler

class ExportSudoku:
    
    def __init__(self):
        """
        Contructor class ExportSudoku class in charge to export sudokus
        data to differents outputs such as txt , cmdline
        
        """

        # option value when the export must be in cmd line
        self.export_to_cmd_line = "cmd line"
        # option value when the export must be in cmd line
        self.export_to_txt = "txt"
        # handler to write to txt files
        self.txt_handler = TXTHandler()

    def export_sudoku(self, sudoku_matrix, type_file, path, name_file):
        """
        Export the sudoku to a given export type such as txt file
        Return True if the sudoku was successfully exported otherwise
        return False

        Keyword arguments:
        sudoku_matrix -- the matrix which contains the sudoku data
                         to export
        type_file -- the type where the file will be exported e.g txt
        path -- the path where the sudoku will be exported
        name_export -- the name of the file where the sudoku will be
                       exported

        """
        sudoku_matrix = self.get_format_sudoku(sudoku_matrix)
        sudoku_exported = False
        if type_file == self.export_to_cmd_line :
            print sudoku_matrix
            sudoku_exported = True
        if type_file == self.export_to_txt:
            sudoku_exported = self.txt_handler.write_sudoku(path,
                              name_file, sudoku_matrix)
        return sudoku_exported
            
    def get_format_sudoku(self, sudoku_matrix):
        """
        Return a line string which contain the sudoku with the
        expected format to be exported

        Keyword arguments:
        sudoku_matrix -- the matrix which contains the sudoku data
                         to export

        """
        size_sudoku = len(sudoku_matrix)
        line_to_export = ""
        row = " "
        sep = ""
        for i in range (0, size_sudoku):
            for j in range(0, size_sudoku):
                if (j % 3 == 0 and j > 0):
                    row = row + "|"+" "
                row = row + sudoku_matrix[i][j] + " "
            if (i % 3 == 0 and i > 0):
                for h in range (0, size_sudoku):
                    if (h % 3 == 0 and h > 0):
                        sep = sep + " + -"
                    else:
                        sep = sep + " -"
                line_to_export = line_to_export + sep + "\n"  
                sep = ""
            line_to_export = line_to_export+ row + "\n"  
            row = " "
        return line_to_export

