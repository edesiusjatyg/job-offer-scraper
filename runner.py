import os
from selenium import webdriver


RESULT_FILENAME = "result.csv"

def check_csv(filename: str):
    if not os.path.exists(filename):
        print("File not found")
        return False
    return True

def write_csv(filename: str, message: str):
    with open(filename, "a") as f:
        f.write(message+"\n")

def main():
    check_csv(RESULT_FILENAME)

if __name__ == "__main__":
    main()
