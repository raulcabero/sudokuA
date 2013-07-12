import unittest
import sys
import csv
import os
sys.path.append( '../libs' )
from csv_handler import CSVHandler

class TestCSVHandler(unittest.TestCase):
    
    def setUp(self):
        # setting a valid csv file 9x9
        self.valid_csv = [['316578492'], ['529134768'], ['487629531'],
                          ['263415987'], ['974863125'], ['851792643'],
                          ['138947256'], ['692351874'], ['745286319']]
        length = len(self.valid_csv[0])

        with open('testvalidcsv.csv', 'wb') as test_file:
            csv_writer = csv.writer(test_file)
            for y in range(length):
                csv_writer.writerow([x[y] for x in self.valid_csv])

        # setting invalid data in csv file
        self.invalid_csv_data = [['316578492'], ['529134768'], ['487629531'],
                                 ['263415987'], ['974863125'], ['851792643'],
                                 ['138947256']]
                                 
        length = len(self.invalid_csv_data[0])

        with open('testinvalidcsv.csv', 'wb') as test_file:
            csv_writer = csv.writer(test_file)
            for y in range(length):
                csv_writer.writerow([x[y] for x in self.invalid_csv_data])


        # setting empty data in csv file
        f = open("empty.csv", "w")
        f.close()

        # setting csv file with 2 sudokus
        self.valid_csv = [['316578492', '316578492'], ['529134768', '529134768'],
                          ['487629531', '487629531'], ['263415987', '263415987'],
                          ['974863125', '974863125'], ['851792643', '851792643'],
                          ['138947256', '138947256'], ['692351874', '692351874'],
                          ['745286319', '745286319']]
        length = len(self.valid_csv[0])

        with open('testvalidcsv2sudokus.csv', 'wb') as test_file:
            csv_writer = csv.writer(test_file)
            for y in range(length):
                csv_writer.writerow([x[y] for x in self.valid_csv])

    def tearDown(self):
        os.remove('testvalidcsv.csv')
        os.remove('testinvalidcsv.csv')
        os.remove('empty.csv')
        os.remove('testvalidcsv2sudokus.csv')

    def test_read_sudoku_from_valid_csv(self):
        sudoku_size = 9
        csv_import = CSVHandler()
        exp_val = "316578492\n" + \
                  "529134768\n" + \
                  "487629531\n" + \
                  "263415987\n" + \
                  "974863125\n" + \
                  "851792643\n" + \
                  "138947256\n" + \
                  "692351874\n" + \
                  "745286319\n"

        
        sudoku = csv_import.get_rows_sudoku_data('testvalidcsv.csv', ',')
        self.assertEquals(exp_val, sudoku[0][0])
        self.assertEquals(sudoku_size, sudoku[0][1])

    def test_read_sudoku_from_valid_csv(self):
        sudoku_invalid_size = -1
        csv_import = CSVHandler()
        sudoku = csv_import.get_rows_sudoku_data('testinvalidcsv.csv', ',')
        expected = "316578492\n" + \
                   "529134768\n" + \
                   "487629531\n" + \
                   "263415987\n" + \
                   "974863125\n" + \
                   "851792643\n" + \
                   "138947256\n"

        self.assertEquals(sudoku[0][0], expected)
        self.assertEquals(sudoku[0][1], sudoku_invalid_size)

    def test_read_sudoku_from_non_exist_csv(self):
        csv_import = CSVHandler()
        sudoku = csv_import.get_rows_sudoku_data('non_exist.csv', ',')
        expected = [] 
        self.assertEquals(sudoku, expected)

    def test_read_sudoku_from_empty_csv(self):
        expected = []
        csv_import = CSVHandler()
        sudoku = csv_import.get_rows_sudoku_data('empty.csv', ',') 
        self.assertEquals(sudoku, expected)

    def test_read_sudoku_from_csv_2_sudokus(self):
        sudoku_size = 9
        csv_import = CSVHandler()
        exp_val = "316578492\n" + \
                  "529134768\n" + \
                  "487629531\n" + \
                  "263415987\n" + \
                  "974863125\n" + \
                  "851792643\n" + \
                  "138947256\n" + \
                  "692351874\n" + \
                  "745286319\n"

        
        sudoku = csv_import.get_rows_sudoku_data('testvalidcsv2sudokus.csv', ',')
        self.assertEquals(exp_val, sudoku[0][0])
        self.assertEquals(exp_val, sudoku[1][0])
        self.assertEquals(sudoku_size, sudoku[0][1])
        self.assertEquals(sudoku_size, sudoku[1][1])

if __name__ == "__main__":
    unittest.main()
