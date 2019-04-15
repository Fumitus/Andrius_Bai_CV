from CV import cursorObject


class ExportQuery:
    def __init__(self, query):
        self.query = query
        results = cursorObject.execute(query)
        for result in results:
            print(result)




