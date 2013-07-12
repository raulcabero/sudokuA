import csv

class CSVHandler:

    def get_rows_sudoku_data(self, file_path, delimeter):
        """
        Read the sudoku data form a csv file
        Returns a matrix[][] which contain all the sudoku
        data into the csv file and their size

        Keyword arguments:
        file_path -- the path of the file which contains the
                     sudoku data
        delimeter -- the separator for data in the csv file               

        """
        
        sudoku_data_from_csv = []
        try:
            csvfile = open(file_path, 'rb')
            spam_reader = csv.reader(csvfile, delimiter=delimeter, quotechar='|')
            for row in spam_reader:
                sudoku_data_from_csv.append(row)
            sudoku_data_from_csv = self.get_sudoku_raws_data_from_csv_rows(sudoku_data_from_csv)
        except Exception:
            sudoku_data_from_csv = []
        return sudoku_data_from_csv

    def get_sudoku_raws_data_from_csv_rows(self, csv_rows):
        """
        Given the rows form the csv file it converts the
        each row in a valid row entry for the sudoku solver
        Returns a matrix[][] which contain the sudoku data
        in each row and their size of the sudoku

        Keyword arguments:
        csv_rows -- the rows into a csv file, each row in the csv file
                    represents a complete sudoku data to solve
                    
        """
        
        matrix_sudoku = []
        for row in csv_rows:
            matrix_sudoku.append(self.get_sudoku_raw_data(row))
        return matrix_sudoku
        

    def get_sudoku_raw_data(self, csv_sudoku):
        """
        Given a row form the csv file it converts the row
        in a valid row entry for the sudoku solver.
        Each row in the csv file represents a complete data for
        a sudoku to solve
        Returns an array[] which contain the sudoku data
        in the row and the size of the sudoku

        Keyword arguments:
        csv_sudoku -- A row of the csv file, it represents a complete
                      sudoku data to solve  
        
        """
        result = []
        sudoku_row_data = ""
        size = -1
        for data in csv_sudoku:
            sudoku_row_data = sudoku_row_data + data + "\n"
            if size == -1:
                size = len(data)
            elif size != len(data):
                size = -1
                break
        if len(csv_sudoku) != size:
            size = -1        
        result.append(sudoku_row_data)
        result.append(size)
        return result
