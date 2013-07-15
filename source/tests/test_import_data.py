import unittest
import sys
import csv
import os
sys.path.append( '../libs' )
from import_data import ImportData

class TestImportData(unittest.TestCase):

    def setUp(self):
        # setting a valid csv file 9x9
        self.valid_csv = [['316578492'], ['529134768'], ['487629531'], ['263415987'],
                          ['974863125'], ['851792643'], ['138947256'], ['692351874'],
                          ['745286319']]
        length = len(self.valid_csv[0])

        with open('testvalidcsv.csv', 'wb') as test_file:
            csv_writer = csv.writer(test_file)
            for y in range(length):
                csv_writer.writerow([x[y] for x in self.valid_csv])

        # seeting invalid extension csv file
        self.invalid_csv_extension = [['316578492', '529134768', '487629531',
                                       '851792643', '138947256', '692351874']]
        length = len(self.invalid_csv_extension[0])

        with open('testinvalidcsvext.csv.mp5', 'wb') as test_file:
            csv_writer = csv.writer(test_file)
            for y in range(length):
                csv_writer.writerow([x[y] for x in self.invalid_csv_extension])

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
        os.remove('testinvalidcsvext.csv.mp5')
        os.remove('testinvalidcsv.csv')
        os.remove('empty.csv')
        os.remove('testvalidcsv2sudokus.csv')

    def test_get_extension_csv(self):
        import_data = ImportData()
        ext = import_data.get_extension_file('testvalidcsv.csv')
        self.assertEquals(".csv", ext)

    def test_get_extension_different_csv_double_extention(self):
        import_data = ImportData()
        ext = import_data.get_extension_file('testinvalidcsvext.csv.mp5')
        self.assertEquals(".mp5", ext)
        
    def test_get_extension_non_exist_file(self):
        import_data = ImportData()
        ext = import_data.get_extension_file('non_exist')
        self.assertEquals("", ext)

    def test_get_extension_double_extension(self):
        import_data = ImportData()
        ext = import_data.get_extension_file('file.tar.gz')
        self.assertEquals(".tar.gz", ext)
        
    def test_read_sudoku_from_valid_csv(self):
        sudoku_size = 9
        import_data = ImportData()
        exp_val = "316578492\n" + \
                  "529134768\n" + \
                  "487629531\n" + \
                  "263415987\n" + \
                  "974863125\n" + \
                  "851792643\n" + \
                  "138947256\n" + \
                  "692351874\n" + \
                  "745286319\n"
        
        sudoku = import_data.read_sudoku_data_from_file('testvalidcsv.csv')
        self.assertEquals(exp_val, sudoku[0][0])
        self.assertEquals(sudoku_size, sudoku[0][1])

    def test_read_sudoku_from_invalid_csv(self):
        expected_size = -1
        import_data = ImportData()
        sudoku = import_data.read_sudoku_data_from_file('testinvalidcsv.csv')
        self.assertEquals(sudoku[0][1], expected_size)

    def test_read_sudoku_from_non_exist_csv(self):
        import_data = ImportData()
        sudoku_is_read = import_data.read_sudoku_data_from_file('non_exist.csv')
        self.assertFalse(sudoku_is_read)

    def test_read_sudoku_from_empty_csv(self):
        import_data = ImportData()
        sudoku_is_read = import_data.read_sudoku_data_from_file('empty.csv')
        self.assertFalse(sudoku_is_read)

    def test_read_sudoku_from_csv_2_sudokus(self):
        sudoku_size = 9
        import_data = ImportData()
        exp_val = "316578492\n" + \
                  "529134768\n" + \
                  "487629531\n" + \
                  "263415987\n" + \
                  "974863125\n" + \
                  "851792643\n" + \
                  "138947256\n" + \
                  "692351874\n" + \
                  "745286319\n"
        
        sudoku = import_data.read_sudoku_data_from_file('testvalidcsv2sudokus.csv')
        self.assertEquals(exp_val, sudoku[0][0])
        self.assertEquals(exp_val, sudoku[1][0])
        self.assertEquals(sudoku_size, sudoku[0][1])
        self.assertEquals(sudoku_size, sudoku[1][1])

    def test_read_valid_sudoku_from_cmd_line(self):
        sudoku_size = 9
        input_line = "000000680000073009309000045490000000803050" + \
                      "902000000036960000308700680000028000000"
        import_data = ImportData()
        exp_result = "000000680\n" + \
                     "000073009\n" + \
                     "309000045\n" + \
                     "490000000\n" + \
                     "803050902\n" + \
                     "000000036\n" + \
                     "960000308\n" + \
                     "700680000\n" + \
                     "028000000\n"
        sudoku = import_data.read_sudoku_data_from_line(input_line)
        self.assertEquals(exp_result, sudoku[0][0])
        self.assertEquals(sudoku_size, sudoku[0][1])

    def test_read_invalid_sudoku_from_cmd_line(self):
        sudoku_size = -1
        input_line = "000000680000073009309000045490000000803050902000000036"
        import_data = ImportData()
        sudoku = import_data.read_sudoku_data_from_line(input_line)
        self.assertEquals(input_line, sudoku[0][0])
        self.assertEquals(sudoku_size, sudoku[0][1])

if __name__ == "__main__":
    unittest.main()
