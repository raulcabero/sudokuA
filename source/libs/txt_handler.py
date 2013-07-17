import os
import math
class TXTHandler:
    
    def write_sudoku(self, path, file_name, string_to_write):
        """
        Write a sodoku in a txt file 
        Returns True if the data has been written successfully
        otherwise return False

        Keyword arguments:
        path -- the path of the directory where the file will be created
        file_name -- the file name of the file that will contain the
                     sudoku data
        string_to_write -- the sudoku data to write in the txt file
                       
        """
        sudoku_was_write = False
        if os.path.exists(path):
            try:
                my_file = open(path+file_name, 'w')
                my_file.write(string_to_write)
                my_file.close()
                sudoku_was_write = True
            except:
                sudoku_was_write = False
        return sudoku_was_write


    def get_sudoku_data(self, file_name):
        """
        Given the a txt file it converts the
        each row in a valid row entry for the sudoku solver
        Returns a matrix[][] which contain the sudoku data
        and its size

        Keyword arguments:
        res -- contains the sudoku and its size
        sudoku -- contains the lines for the sudoku
        sudoku1 -- contains the lines for the sudoku without spaces
        file_string -- used for reading the txt file lines
        sep -- used as separator in order to mark the end of a sudoku
        size_sudoku -- stores the sudoku's size

        """
        res = []      
        sudoku = ""
        sudoku1 = ""
        sep = '\n' 
        
        file_string = file(file_name).readlines()
        #print 'hola', file_string
        #print len(file_string)
        
        for line in range(0, len(file_string)):
            #print file_string[line]
            sudoku = sudoku + file_string[line]
            sudoku1 = sudoku1 + file_string[line].strip('\n')
            if file_string[line] == sep or line == len(file_string)-1:
                #print 'test'
                aux = []
                sudoku = sudoku.strip('\n')
                aux.append(sudoku)
                size_sudoku = math.sqrt(len(sudoku1))                       
                if size_sudoku % 1 > 0:
                    size_sudoku = -1
                if size_sudoku != 0:
                    aux.append(int(size_sudoku))
                    res.append(aux)
                sudoku = ""
                sudoku1 = ""
            #print line
        #print len (res)
        return res

#txt_handler = TXTHandler()
#print txt_handler.get_sudoku_data('sudoku1.txt')
