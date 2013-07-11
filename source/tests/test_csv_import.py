import unittest
import sys
import csv
import os
sys.path.append( '../libs' )
from csv_import import CSVImport

class TestCSVImport(unittest.TestCase):
    
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
        csv_import = CSVImport()
        exp_val = "316578492\n" + \
                  "529134768\n" + \
                  "487629531\n" + \
                  "263415987\n" + \
                  "974863125\n" + \
                  "851792643\n" + \
                  "138947256\n" + \
                  "692351874\n" + \
                  "745286319\n"

        
        res = csv_import.get_rows_sudoku_data('testvalidcsv.csv', ',')
        self.assertEquals(exp_val, res[0][0])
        self.assertEquals(9, res[0][1])

    def test_read_sudoku_from_valid_csv(self):
        csv_import = CSVImport()
        res = csv_import.get_rows_sudoku_data('testinvalidcsv.csv', ',')
        expected = "316578492\n" + \
                   "529134768\n" + \
                   "487629531\n" + \
                   "263415987\n" + \
                   "974863125\n" + \
                   "851792643\n" + \
                   "138947256\n"

        self.assertEquals(res[0][0], expected)
        self.assertEquals(res[0][1], -1)

    def test_read_sudoku_from_non_exist_csv(self):
        csv_import = CSVImport()
        res = csv_import.get_rows_sudoku_data('non_exist.csv', ',')
        expected = [] 
        self.assertEquals(res, expected)

    def test_read_sudoku_from_empty_csv(self):
        csv_import = CSVImport()
        res = csv_import.get_rows_sudoku_data('empty.csv', ',')
        expected = [] 
        self.assertEquals(res, expected)

    def test_read_sudoku_from_csv_2_sudokus(self):
        csv_import = CSVImport()
        exp_val = "316578492\n" + \
                  "529134768\n" + \
                  "487629531\n" + \
                  "263415987\n" + \
                  "974863125\n" + \
                  "851792643\n" + \
                  "138947256\n" + \
                  "692351874\n" + \
                  "745286319\n"

        
        res = csv_import.get_rows_sudoku_data('testvalidcsv2sudokus.csv', ',')
        self.assertEquals(exp_val, res[0][0])
        self.assertEquals(exp_val, res[1][0])
        self.assertEquals(9, res[0][1])
        self.assertEquals(9, res[1][1])

if __name__ == "__main__":
    unittest.main()
