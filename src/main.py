import pymysql
from os import get_terminal_size


class Main(object):
    def __init__(self):
        print("-" * get_terminal_size().columns)
        print("Welcome to the Program!".center(get_terminal_size().columns))
        print("-" * get_terminal_size().columns)
        self.db = db = pymysql.connect("localhost", "root", "tanmay03", "Case_Study_4")
        self.cursor = db.cursor()

    def run(self):
        pass


if __name__ == "__main__":
    app = Main()
    app.run()
