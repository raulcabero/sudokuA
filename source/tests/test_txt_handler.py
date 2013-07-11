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
        self.pathname = os.path.dirname(file)
        # create an file to test the existing file case
        myFile = open(self.pathname + '/test_exist_file.txt', 'w')
        myFile.write("te")
        myFile.close()

    def tearDown(self):
        os.remove(self.pathname + '/test_exist_file.txt')

    def test_the_name_file_increments_when_the_same_file_exist(self):
        res = self.txt_handler.get_file_name(self.pathname + "/", 'test_exist_file.txt', 0)
        self.assertEquals('test_exist_file1.txt', res)

    def test_the_name_file_is_the_same_when_the_file_not_exist(self):
        res = self.txt_handler.get_file_name(self.pathname + "/", 'test_not_exist_file.txt', 0)
        self.assertEquals('test_not_exist_file.txt', res)

    def test_write_sudoku_returns_true_file_has_been_write(self):
        res = self.txt_handler.write_sudoku(self.pathname + "/", 'test_not_exist_file.txt', "test")
        os.remove(self.pathname + '/test_not_exist_file.txt')
        self.assertTrue(res)

    def test_write_sudoku_writes_the_specified_line(self):
        line_to_write = "test\n" + \
                        "this is a test"
        self.txt_handler.write_sudoku(self.pathname + "/", \
                                     'test_write_specified_line.txt', line_to_write)
        file_written = open(self.pathname+"/" + 'test_write_specified_line.txt', "r")
        content = file_written.readlines()
        res = ""
        for l in content :
            res = res + l
        file_written.close()
        os.remove(self.pathname + '/test_write_specified_line.txt')
        self.assertEquals(res,line_to_write)

if __name__ == "__main__":
    unittest.main()
