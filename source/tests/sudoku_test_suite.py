from coverage import coverage

cov = coverage()
cov.start()

import unittest
from test_backtraking_algorithm import TestBacktrakingAlgorithm
from test_norvig_algorithm import TestNorvigAlgorithm
from test_brute_force_algorithm import TestBruteForceAlgorithm
from test_xml_config import TestXmlConfig
from test_import_data import TestImportData
from test_csv_handler import TestCSVHandler
from test_txt_handler import TestTXTHandler
from test_export_sudoku import TestExportSudoku
from test_bit_handler import TestBitHandler
from test_sudoku_generator import TestSudokuGenerator
from test_cmd_handler import TestCMDHandler


if __name__ =="__main__":

    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestBacktrakingAlgorithm))
    suite.addTest(unittest.makeSuite(TestNorvigAlgorithm))
    suite.addTest(unittest.makeSuite(TestBruteForceAlgorithm))
    suite.addTest(unittest.makeSuite(TestXmlConfig))
    suite.addTest(unittest.makeSuite(TestImportData))
    suite.addTest(unittest.makeSuite(TestCSVHandler))
    suite.addTest(unittest.makeSuite(TestTXTHandler))
    suite.addTest(unittest.makeSuite(TestExportSudoku))
    suite.addTest(unittest.makeSuite(TestBitHandler))
    suite.addTest(unittest.makeSuite(TestSudokuGenerator))
    suite.addTest(unittest.makeSuite(TestCMDHandler))

    unittest.TextTestRunner(verbosity=2).run(suite)

    cov.stop()
    cov.html_report(directory='covhtml')
