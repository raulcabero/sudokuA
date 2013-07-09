import unittest # pragma: no cover
import sys # pragma: no cover
import csv # pragma: no cover
import os # pragma: no cover
sys.path.append( '../libs' ) # pragma: no cover
from import_data import ImportData # pragma: no cover

class TestImportData(unittest.TestCase): # pragma: no cover

    def setUp(self):
        # setting a valid csv file 9x9
        self.valid_csv = [['316578492'],['529134768'],['487629531'],['263415987'],
                          ['974863125'],['851792643'],['138947256'],['692351874'],
                          ['745286319']]
        length = len(self.valid_csv[0])

        with open('testvalidcsv.csv', 'wb') as test_file:
            csv_writer = csv.writer(test_file)
            for y in range(length):
                csv_writer.writerow([x[y] for x in self.valid_csv])

        # seeting invalid extension csv file
        self.invalid_csv_extension = [['316578492','529134768','487629531',
                                       '851792643','138947256','692351874']]
        length = len(self.invalid_csv_extension[0])

        with open('testinvalidcsvext.csv.mp5', 'wb') as test_file:
            csv_writer = csv.writer(test_file)
            for y in range(length):
                csv_writer.writerow([x[y] for x in self.invalid_csv_extension])

        # setting invalid data in csv file
        self.invalid_csv_data = [['316578492'],['529134768'],['487629531'],['263415987'],
                                 ['974863125'],['851792643'],['138947256']]
                                 
        length = len(self.invalid_csv_data[0])

        with open('testinvalidcsv.csv', 'wb') as test_file:
            csv_writer = csv.writer(test_file)
            for y in range(length):
                csv_writer.writerow([x[y] for x in self.invalid_csv_data])


        # setting empty data in csv file
        f = open("empty.csv", "w")
        f.close

        # setting csv file with 2 sudokus
        self.valid_csv = [['316578492','316578492'],['529134768','529134768'],['487629531','487629531'],['263415987','263415987'],
                          ['974863125','974863125'],['851792643','851792643'],['138947256','138947256'],['692351874','692351874'],
                          ['745286319','745286319']]
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

    def test_guess_extension_csv(self):
        import_data = ImportData()
        root, ext = import_data.guess_extension('testvalidcsv.csv')
        self.assertEquals(".csv",ext)

    def test_guess_extension_different_csv_double_extention(self):
        import_data = ImportData()
        root, ext = import_data.guess_extension('testinvalidcsvext.csv.mp5')
        self.assertEquals(".mp5",ext)
        
    def test_guess_extension_non_exist_file(self):
        import_data = ImportData()
        root, ext = import_data.guess_extension('non_exist')
        self.assertEquals("",ext)

    def test_guess_extension_double_extension(self):
        import_data = ImportData()
        root, ext = import_data.guess_extension('file.tar.gz')
        self.assertEquals(".tar.gz",ext)
        
    def test_read_sudoku_from_valid_csv(self):
        import_data = ImportData()
        exp_val = """316578492
529134768
487629531
263415987
974863125
851792643
138947256
692351874
745286319
"""
        
        res = import_data.read_sudoku_data_from_file('testvalidcsv.csv')
        self.assertEquals(exp_val,res[0][0])
        self.assertEquals(9,res[0][1])

    def test_read_sudoku_from_valid_csv(self):
        import_data = ImportData()
        res = import_data.read_sudoku_data_from_file('testinvalidcsv.csv')
        self.assertFalse(res)

    def test_read_sudoku_from_non_exist_csv(self):
        import_data = ImportData()
        res = import_data.read_sudoku_data_from_file('non_exist.csv')
        self.assertFalse(res)

    def test_read_sudoku_from_empty_csv(self):
        import_data = ImportData()
        res = import_data.read_sudoku_data_from_file('empty.csv')
        self.assertFalse(res)

    def test_read_sudoku_from_csv_2_sudokus(self):
        import_data = ImportData()
        exp_val = """316578492
529134768
487629531
263415987
974863125
851792643
138947256
692351874
745286319
"""
        
        res = import_data.read_sudoku_data_from_file('testvalidcsv2sudokus.csv')
        self.assertEquals(exp_val,res[0][0])
        self.assertEquals(exp_val,res[1][0])
        self.assertEquals(9,res[0][1])
        self.assertEquals(9,res[1][1])


if __name__ == "__main__": # pragma: no cover
    unittest.main()
