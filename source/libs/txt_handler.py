import os
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
            file_name = self.get_file_name(path, file_name, 0)
            try:
                myFile = open(path+file_name, 'w')
                myFile.write(string_to_write)
                myFile.close()
                sudoku_was_write = True
            except:
                sudoku_was_write = False
        return sudoku_was_write

    def get_file_name(self, path, file_name, number_file):
        """
        Returns a non-exist file name. If the given file name already
        exists it add a number to the end the file and if the new file
        name does not exist return that name

        Keyword arguments:
        path -- the path of the directory where the file will be created
        file_name -- the file name of the file that will contain the
                     sudoku data
        number_file -- the start number that will be added to the end of
                       the file
                       
        """
        if not os.path.isfile(path + file_name):
            file_name_to_write =  file_name
        else:
            new_number_file = number_file + 1
            new_file_name = file_name[0:(len(file_name)-4)] + str(new_number_file)+'.txt'
            if not os.path.isfile(path + new_file_name):
                file_name_to_write =  new_file_name
            else:
                file_name_to_write = self.get_file_name(path, file_name, new_number_file)
        return file_name_to_write


