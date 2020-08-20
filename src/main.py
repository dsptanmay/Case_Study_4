import pymysql
from os import get_terminal_size


class Main(object):
    def __init__(self):
        print("-"*get_terminal_size().columns)
        print("Welcome to the Program!".center(get_terminal_size().columns))
        print("-"*get_terminal_size().columns)
        with pymysql.connect("localhost","root","Case_Study_4","tanmay03") as db:
            self.cursor = db.cursor()

    def run():
        pass

if __name__ == '__main__':
    app = Main()
    app.run()
