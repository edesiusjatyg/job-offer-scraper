import os

class CsvOperations:
    def __init__(self):
        pass

    def create_csv(self, filename: str, header: str):
        with open(filename, "w") as f:
            f.write(header+"\n")

    def check_csv(self, filename: str):
        if not os.path.exists(filename):
            print("File not found!")
            return False
        return True

    def read_csv(self, filename: str):
        if self.check_csv(filename):
            with open(filename, "r") as f:
                return f.read()
        return None
    
    def write_csv(self, filename: str, message: str):
        if self.check_csv(filename):
            with open(filename, "a") as f:
                f.write(message+"\n")
