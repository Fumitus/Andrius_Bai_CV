from CV import cursorObject


class ExportQuery:
    def __init__(self, query):
        self.query = query
        data = cursorObject.execute(query).fetchall()

        for i in data:
            print(i)

