import unittest 
import sys 
sys.path.append( '../libs' ) 
from backtraking_algorithm import BacktrakingAlgorithm 

class TestBacktrakingAlgorithm(unittest.TestCase): 
    def setUp(self):
        pass

        ################ Test correct solution sudoku ################

    def test_verify_solution_easy_sudoku_empty_values_with_zero(self):
        raw_sudoku  = ("000000680\n" + \
                       "000073009\n" + \
                       "309000045\n" + \
                       "490000000\n" + \
                       "803050902\n" + \
                       "000000036\n" + \
                       "960000308\n" + \
                       "700680000\n" + \
                       "028000000\n")
        sudoku_test_solve = BacktrakingAlgorithm(raw_sudoku, "0")
        square_result = [['1', '7', '2', '5', '4', '9', '6', '8', '3'],
                         ['6', '4', '5', '8', '7', '3', '2', '1', '9'],
                         ['3', '8', '9', '2', '6', '1', '7', '4', '5'],
                         ['4', '9', '6', '3', '2', '7', '8', '5', '1'],
                         ['8', '1', '3', '4', '5', '6', '9', '7', '2'],
                         ['2', '5', '7', '1', '9', '8', '4', '3', '6'],
                         ['9', '6', '4', '7', '1', '5', '3', '2', '8'],
                         ['7', '3', '1', '6', '8', '2', '5', '9', '4'],
                         ['5', '2', '8', '9', '3', '4', '1', '6', '7']]
        self.assertEquals(square_result, sudoku_test_solve.solve_sudoku())

    def test_verify_solution_easy_sudoku_empty_values_with_dot(self):
        raw_sudoku  = ("3.65.84..\n" + \
                       "52.......\n" + \
                       ".87....31\n" + \
                       "..3.1..8.\n" + \
                       "9..863..5\n" + \
                       ".5..9.6..\n" + \
                       "13....25.\n" + \
                       ".......74\n" + \
                       "..52.63..\n")
        sudoku_test_solve = BacktrakingAlgorithm(raw_sudoku, ".")
        square_result = [['3', '1', '6', '5', '7', '8', '4', '9', '2'],
                         ['5', '2', '9', '1', '3', '4', '7', '6', '8'],
                         ['4', '8', '7', '6', '2', '9', '5', '3', '1'],
                         ['2', '6', '3', '4', '1', '5', '9', '8', '7'],
                         ['9', '7', '4', '8', '6', '3', '1', '2', '5'],
                         ['8', '5', '1', '7', '9', '2', '6', '4', '3'],
                         ['1', '3', '8', '9', '4', '7', '2', '5', '6'],
                         ['6', '9', '2', '3', '5', '1', '8', '7', '4'],
                         ['7', '4', '5', '2', '8', '6', '3', '1', '9']];
          
        self.assertEquals(square_result, sudoku_test_solve.solve_sudoku()) 

        ############ Test convertion sudoku raw to matrix ############
        
    def test_convert_raw_sudoku_matrix_empty_values_dot(self):
        raw_sudoku  = (".923.....\n" + \
                       "....8.1..\n" + \
                       ".........\n" + \
                       "1.7.4....\n" + \
                       ".......65\n" + \
                       "8........\n" + \
                       ".6.5.2...\n" + \
                       "4.....7..\n" + \
                       "...9.....\n")
        sudoku_test_convert = BacktrakingAlgorithm("092300000", ".")
        square_result = [['.', '9', '2', '3', '.', '.', '.', '.', '.'],
                         ['.', '.', '.', '.', '8', '.', '1', '.', '.'],
                         ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                         ['1', '.', '7', '.', '4', '.', '.', '.', '.'],
                         ['.', '.', '.', '.', '.', '.', '.', '6', '5'],
                         ['8', '.', '.', '.', '.', '.', '.', '.', '.'],
                         ['.', '6', '.', '5', '.', '2', '.', '.', '.'],
                         ['4', '.', '.', '.', '.', '.', '7', '.', '.'],
                         ['.', '.', '.', '9', '.', '.', '.', '.', '.']];

        self.assertEquals(square_result,
                          sudoku_test_convert.get_grid_values(raw_sudoku))

    def test_convert_raw_sudoku_matrix_empty_values_0(self):
        raw_sudoku  = ("092300000\n" + \
                       "000080100\n" + \
                       "000000000\n" + \
                       "107040000\n" + \
                       "000000065\n" + \
                       "800000000\n" + \
                       "060502000\n" + \
                       "400000700\n" + \
                       "000900000\n")
        sudoku_test_convert = BacktrakingAlgorithm("092300000", "0")
        square_result = [['0', '9', '2', '3', '0', '0', '0', '0', '0'],
                         ['0', '0', '0', '0', '8', '0', '1', '0', '0'],
                         ['0', '0', '0', '0', '0', '0', '0', '0', '0'],
                         ['1', '0', '7', '0', '4', '0', '0', '0', '0'],
                         ['0', '0', '0', '0', '0', '0', '0', '6', '5'],
                         ['8', '0', '0', '0', '0', '0', '0', '0', '0'],
                         ['0', '6', '0', '5', '0', '2', '0', '0', '0'],
                         ['4', '0', '0', '0', '0', '0', '7', '0', '0'],
                         ['0', '0', '0', '9', '0', '0', '0', '0', '0']];

        self.assertEquals(square_result,
                          sudoku_test_convert.get_grid_values(raw_sudoku))

        ############ Test validation unassigned location ############
        
    def test_find_unassigned_location_returns_false_when_no_empty_place(self):
        sudoku_test_unassigned = BacktrakingAlgorithm("092300000", ".")
        square = [['3', '5', '6', '5', '7', '8', '4', '6', '1'],
                  ['5', '2', '2', '2', '1', '4', '9', '3', '2'],
                  ['2', '8', '7', '5', '2', '1', '2', '3', '1'],
                  ['3', '8', '3', '3', '1', '2', '2', '8', '8'],
                  ['9', '2', '1', '8', '6', '3', '7', '7', '5'],
                  ['4', '5', '1', '6', '9', '3', '6', '1', '1'],
                  ['1', '3', '2', '5', '9', '2', '2', '5', '3'],
                  ['5', '9', '2', '3', '2', '1', '4', '7', '4'],
                  ['6', '8', '5', '2', '1', '6', '3', '8', '7']];
        row, col, bol = sudoku_test_unassigned.find_unassigned_location(square)
        self.assertFalse(bol)
    
    def test_find_unassigned_location_returns_correct_place_unassigned_value_with_dot_as_empty(self):
        sudoku_test_unassigned = BacktrakingAlgorithm("092300000", ".")
        square = [['3', '5', '6', '5', '7', '8', '4', '6', '1'],
                  ['5', '2', '2', '2', '1', '4', '9', '3', '2'],
                  ['2', '8', '7', '5', '2', '1', '2', '3', '1'],
                  ['3', '8', '3', '.', '1', '2', '2', '8', '.'],
                  ['9', '2', '1', '8', '6', '3', '7', '.', '5'],
                  ['4', '5', '1', '6', '9', '.', '6', '.', '.'],
                  ['1', '3', '2', '5', '.', '.', '2', '5', '.'],
                  ['5', '9', '2', '3', '.', '.', '.', '7', '4'],
                  ['6', '8', '5', '2', '.', '6', '3', '.', '.']];
        row, col, bol = sudoku_test_unassigned.find_unassigned_location(square)
        self.assertEquals(3, row)
        self.assertEquals(3, col)
        self.assertTrue(bol)

    def test_find_unassigned_location_returns_correct_place_unassigned_value(self):
        sudoku_test_unassigned = BacktrakingAlgorithm("092300000", "0")
        square = [['3', '5', '6', '5', '7', '8', '4', '6', '1'],
                  ['5', '2', '2', '2', '1', '4', '9', '3', '2'],
                  ['2', '8', '7', '5', '2', '1', '2', '3', '1'],
                  ['3', '8', '3', '0', '1', '2', '2', '8', '0'],
                  ['9', '2', '1', '8', '6', '3', '7', '0', '5'],
                  ['4', '5', '1', '6', '9', '0', '6', '0', '0'],
                  ['1', '3', '2', '5', '0', '0', '2', '5', '0'],
                  ['5', '9', '2', '3', '0', '0', '0', '7', '4'],
                  ['6', '8', '5', '2', '0', '6', '3', '0', '0']];
        row, col, bol = sudoku_test_unassigned.find_unassigned_location(square)
        self.assertEquals(3, row)
        self.assertEquals(3, col)
        self.assertTrue(bol)

        ############## Test validation nun used in row ##############

    def test_return_true_if_num_is_already_in_row(self):
        sudoku_test_row = BacktrakingAlgorithm("092300000","0")
        square = [['3', '0', '6', '5', '0', '8', '4', '0', '0'],
                  ['5', '2', '0', '0', '0', '4', '0', '0', '0'],
                  ['0', '8', '7', '0', '0', '1', '0', '3', '1'],
                  ['0', '0', '3', '0', '1', '2', '0', '8', '0'],
                  ['9', '0', '0', '8', '6', '3', '0', '0', '5'],
                  ['0', '5', '0', '0', '9', '0', '6', '0', '0'],
                  ['1', '3', '0', '0', '0', '0', '2', '5', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '7', '4'],
                  ['0', '0', '5', '2', '0', '6', '3', '0', '0']];
        self.assertTrue(sudoku_test_row.used_in_row(square, 4, 3))

    def test_return_false_if_num_is_not_in_row(self):
        sudoku_test_row = BacktrakingAlgorithm("092300000","0")
        square = [['3', '0', '6', '5', '0', '8', '4', '0', '0'],
                  ['5', '2', '0', '0', '0', '4', '0', '0', '0'],
                  ['0', '8', '7', '0', '0', '1', '0', '3', '1'],
                  ['0', '0', '3', '0', '1', '2', '0', '8', '0'],
                  ['9', '0', '0', '8', '6', '3', '0', '0', '5'],
                  ['0', '5', '0', '0', '9', '0', '6', '0', '0'],
                  ['1', '3', '0', '0', '0', '0', '2', '5', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '7', '4'],
                  ['0', '0', '5', '2', '0', '6', '3', '0', '0']];
        self.assertFalse(sudoku_test_row.used_in_row(square, 8, 9))

        ############## Test validation nun used in col ##############

    def test_return_true_if_num_is_already_in_col(self):
        sudoku_test_col = BacktrakingAlgorithm("092300000","0")
        square = [['3', '0', '6', '5', '0', '8', '4', '0', '0'],
                  ['5', '2', '0', '0', '0', '4', '0', '0', '0'],
                  ['0', '8', '7', '0', '0', '1', '0', '3', '1'],
                  ['0', '0', '3', '0', '1', '2', '0', '8', '0'],
                  ['9', '0', '0', '8', '6', '3', '0', '0', '5'],
                  ['0', '5', '0', '0', '9', '0', '6', '0', '0'],
                  ['1', '3', '0', '0', '0', '0', '2', '5', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '7', '4'],
                  ['0', '0', '5', '2', '0', '6', '3', '0', '0']];
        self.assertTrue(sudoku_test_col.used_in_col(square, 5, 8))

    def test_return_false_if_num_is_not_in_col(self):
        sudoku_test_box = BacktrakingAlgorithm("092300000","0")
        square = [['3', '0', '6', '5', '0', '8', '4', '0', '0'],
                  ['5', '2', '0', '0', '0', '0', '0', '0', '0'],
                  ['0', '8', '7', '0', '0', '1', '0', '3', '1'],
                  ['0', '0', '3', '0', '1', '0', '0', '8', '0'],
                  ['9', '0', '0', '8', '6', '3', '0', '0', '5'],
                  ['0', '5', '0', '0', '9', '0', '6', '0', '0'],
                  ['1', '3', '0', '0', '0', '0', '2', '5', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '7', '4'],
                  ['0', '0', '5', '2', '0', '6', '3', '0', '0']];
        self.assertFalse(sudoku_test_box.used_in_col(square, 8, 9))    

        ############ Test validation nun used in box 3x3  ############ 

    def test_return_true_if_num_is_already_in_box(self):
        sudoku_test_box = BacktrakingAlgorithm("092300000", "0")
        square = [['1', '4', '8'], ['2', '7', '6'], ['5', '3', '0']]
        self.assertTrue(sudoku_test_box.used_in_box(square, 0, 0, 1))

    def test_return_false_if_num_is_not_in_box(self):
        sudoku_test_box = BacktrakingAlgorithm("092300000", "0")
        square = [['1', '4', '8'], ['2', '7', '6'], ['5', '3', '0']]
        self.assertFalse(sudoku_test_box.used_in_box(square, 0, 0, 9))    

        ########## Test validation correct format sudoku data ##########
                
    def test_soduku_to_solve_only_contains_numbers(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm("092300000\n" + \
                                                         "000080100\n" + \
                                                         "000000000\n" + \
                                                         "107040000\n" + \
                                                         "000000065\n" + \
                                                         "800000000\n" + \
                                                         "060502000\n" + \
                                                         "400000700\n" + \
                                                         "000900000\n", "0")
                
        self.assertTrue(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_cannot_contain_letters(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm("092300000\n" + \
                                                         "000080100\n" + \
                                                         "000000000\n" + \
                                                         "107040000\n" + \
                                                         "000000A65\n" + \
                                                         "800000000\n" + \
                                                         "060502000\n" + \
                                                         "400000C00\n" + \
                                                         "000900000\n", "0")
                
        self.assertFalse(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_cannot_contain_dot_as_empty_value_if_the_empty_value_is_zero(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm("092300000\n" + \
                                                         "....80100\n" + \
                                                         "...000000\n" + \
                                                         "107040000\n" + \
                                                         "..0..0465\n" + \
                                                         "800000000\n" + \
                                                         "060502000\n" + \
                                                         "400000200\n" + \
                                                         "000900000\n", "0")
                
        self.assertFalse(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_not_contain_spaces_as_empty_value_if_the_empty_value_is_zero(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm(" 923     \n" + \
                                                         "    8 1  \n" + \
                                                         "      1  \n" + \
                                                         "1 7 4    \n" + \
                                                         "      465\n" + \
                                                         "8        \n" + \
                                                         " 6 5 2   \n" + \
                                                         "4     2  \n" + \
                                                         "   9     \n", "0")
                
        self.assertFalse(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_is_valid_when_contains_81_numbers(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm("092300000\n" + \
                                                         "000080100\n" + \
                                                         "000000000\n" + \
                                                         "107040000\n" + \
                                                         "000000065\n" + \
                                                         "800000000\n" + \
                                                         "060502000\n" + \
                                                         "400000700\n" + \
                                                         "000900000\n", "0")
                
        self.assertTrue(sudoku_test_only_numbers.sudoku_data_is_valid())


    def test_soduku_to_solve_is_invalid_when_contains_less_than_81_numbers(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm("092300000\n" + \
                                                         "000080100\n" + \
                                                         "000000000\n" + \
                                                         "107040000\n" + \
                                                         "000000065\n" + \
                                                         "800000000\n" + \
                                                         "060502000\n", "0")
                
        self.assertFalse(sudoku_test_only_numbers.sudoku_data_is_valid())

    def test_soduku_to_solve_is_invalid_when_contains_more_than_81_numbers(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm("092300000\n" + \
                                                         "000080100\n" + \
                                                         "000000000\n" + \
                                                         "107040000\n" + \
                                                         "000000065\n" + \
                                                         "800000000\n" + \
                                                         "060502000\n" + \
                                                         "400000700\n" + \
                                                         "000900000\n" + \
                                                         "000000065\n" + \
                                                         "060502000\n", "0")

    def test_soduku_to_solve_is_valid_when_characters_to_replace_are_dot(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm(".923.....\n" + \
                                                         "....8.1..\n" + \
                                                         ".........\n" + \
                                                         "1.7.4....\n" + \
                                                         ".......65\n" + \
                                                         "8........\n" + \
                                                         ".6.5.2...\n" + \
                                                         "4.....7..\n" + \
                                                         "...9.....\n", ".")

    def test_soduku_to_solve_is_valid_when_characters_to_replace_are_porcentage(self):
        sudoku_test_only_numbers  = BacktrakingAlgorithm("%923%%%%%\n" + \
                                                         "%%%%8%1%%\n" + \
                                                         "%%%%%%%%%\n" + \
                                                         "1%7%4%%%%\n" + \
                                                         "%%%%%%%65\n" + \
                                                         "8%%%%%%%%\n" + \
                                                         "%6%5%2%%%\n" + \
                                                         "4%%%%%7%%\n" + \
                                                         "%%%9%%%%%\n", "%")
                
        self.assertTrue(sudoku_test_only_numbers.sudoku_data_is_valid())

if __name__ == "__main__":
    unittest.main()
    
