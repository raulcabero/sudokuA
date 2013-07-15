import unittest
import sys
import csv
import os
sys.path.append( '../libs' )
from cmd_handler import CMDHandler

class TestCMDHandler(unittest.TestCase):

    def setUp(self):
        self.cmd_handler = CMDHandler()

    def test_sudoku_is_read_in_correct_format(self):
        input_line = "000000680000073009309000045490000000803050" + \
                      "902000000036960000308700680000028000000"
        exp_result = "000000680\n" + \
                     "000073009\n" + \
                     "309000045\n" + \
                     "490000000\n" + \
                     "803050902\n" + \
                     "000000036\n" + \
                     "960000308\n" + \
                     "700680000\n" + \
                     "028000000\n"
        sudoku = self.cmd_handler.get_rows_sudoku_data(input_line)
        self.assertEquals(exp_result, sudoku[0][0])

    def test_sudoku_is_read_correct_size(self):
        sudoku_size = 9
        input_line = "000000680000073009309000045490000000803050" + \
                      "902000000036960000308700680000028000000"
        exp_result = "000000680\n" + \
                     "000073009\n" + \
                     "309000045\n" + \
                     "490000000\n" + \
                     "803050902\n" + \
                     "000000036\n" + \
                     "960000308\n" + \
                     "700680000\n" + \
                     "028000000\n"
        sudoku = self.cmd_handler.get_rows_sudoku_data(input_line)
        self.assertEquals(sudoku_size, sudoku[0][1])

    def test_format_corect_when_invalid_sudoku_is_read(self):
        input_line = "000000680000073009309000045490000000803050902000000036"
        sudoku = self.cmd_handler.get_rows_sudoku_data(input_line)
        self.assertEquals(input_line, sudoku[0][0])

    def test_format_corect_when_invalid_sudoku_is_read(self):
        sudoku_size = -1
        input_line = "000000680000073009309000045490000000803050902000000036"
        sudoku = self.cmd_handler.get_rows_sudoku_data(input_line)
        self.assertEquals(sudoku_size, sudoku[0][1])

if __name__ == "__main__":
    unittest.main()
