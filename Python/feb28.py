# File Handling
"""
Mode1       Name        Description                                                             Mode2   Name
r           read        Opens the file for reading operation only                               t       Text    #default
                        Returns the FileDoesNotExist if the file does not exist
                        Places the cursor at the begining of the file
                        Does not erase the content of the file at the time of opening

w           write       Opens the file for writing only                                         b       Binary
                        Creates the file if the file does not exist
                        Clears the entire content of the file at the time of opening
                        Cursor is placed at the begining of the file.

a           append      Opens the file for writing only
                        Creates the file if the file does not exist
                        Does not clear the content of the file
                        Cursor is placed at the end of the file.

x           Exclusive   Creates the file if does not exist
            Create      Returns the FileAlreadyExists Error if the file is already existing
                        Allows write operation only

r+          Read Plus   Opens the file for reading & writing both
                        Returns the FileDoesNotExist if the file does not exist
                        Places the cursor at the begining of the file
                        Does not erase the content of the file at the time of opening

w+          Write Plus  Opens the file for writing and reading both
                        Creates the file if the file does not exist
                        Clears the entire content of the file at the time of opening
                        Cursor is placed at the begining of the file.

a           Append Plus Opens the file for writing & reading both
                        Creates the file if the file does not exist
                        Does not clear the content of the file
                        Cursor is placed at the end of the file.
"""
# Syntax:
# name_of_file_pointer = open("file_name_with_extension_and_full_path", "Mode1Mode2")

# File Created: first.txt