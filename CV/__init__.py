import sqlite3


connObject = sqlite3.connect("CV.db")
cursorObject = connObject.cursor()


class DropTable:
    """Drop data base tables if exists"""
    def __init__(self, name):
        self.name = name
        cursorObject.execute(name)