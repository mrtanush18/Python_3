# __enter__ and __exit__ magic methods
# __enter__ and __exit__ methods are used along with the ‘with’ block in python. The ‘with’ block in python is used to open and close the file object or any other objects that have a close method.

class WriteFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
    def log(self, text):
        self.file.write(text+'n')
    def __enter__(self):
        self.file = open(self.file_name, "a+")
        return self    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
with WriteFile(r"filename.txt") as log_file:
    log_file.log("Hello")
    log_file.log("there")

# When the class is invoked with the file name ‘filename.txt’ the __enter__ method implicitly creates a text file. After executing the commands in the text file the __exit__ method is implicitly invoked to close the file object. In this way, we can use the __enter__ and __exit__ magic methods. These methods can also be used to open and close a database connection.