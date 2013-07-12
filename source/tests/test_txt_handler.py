import unittest
import sys
import os
sys.path.append( '../libs' )
from txt_handler import TXTHandler

class TestTXTHandler(unittest.TestCase):

    def setUp(self):
        self.txt_handler = TXTHandler()
        # get the pathdir where the application is running
        file = sys.argv[0]
        self.path_name = os.path.dirname(file) + "/"
        # create an file to test the existing file case
        my_file = open(self.path_name + 'test_exist_file.txt', 'w')
        my_file.write("te")
        my_file.close()

    def tearDown(self):
        os.remove(self.path_name + 'test_exist_file.txt')

    def test_the_name_file_increments_when_the_same_file_exist(self):
        file_name = self.txt_handler.get_file_name(self.path_name, 'test_exist_file.txt', 0)
        self.assertEquals('test_exist_file1.txt', file_name)

    def test_the_name_file_is_the_same_when_the_file_not_exist(self):
        file_name = self.txt_handler.get_file_name(self.path_name, 'test_not_exist_file.txt', 0)
        self.assertEquals('test_not_exist_file.txt', file_name)

    def test_write_sudoku_returns_true_file_has_been_write(self):
        sudoku_was_written = self.txt_handler.write_sudoku(self.path_name, 'test_not_exist_file.txt', "test")
        os.remove(self.path_name + 'test_not_exist_file.txt')
        self.assertTrue(sudoku_was_written)

    def test_write_sudoku_writes_the_specified_line(self):
        line_to_write = "test\n" + \
                        "this is a test"
        self.txt_handler.write_sudoku(self.path_name ,
                                     'test_write_specified_line.txt', line_to_write)
        file_written = open(self.path_name + 'test_write_specified_line.txt', "r")
        content = file_written.readlines()
        line_written = ""
        for line in content :
            line_written = line_written + line
        file_written.close()
        os.remove(self.path_name + 'test_write_specified_line.txt')
        self.assertEquals(line_written,line_to_write)

if __name__ == "__main__":
    unittest.main()
