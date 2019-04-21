from CV import cursorObject, connObject


class InsertValues:
    """Insert data to database(DB).
    Data to put into DB is supplied in _CV.py"""
    @staticmethod
    def insert_language_values(*args):
        language = args[0]
        level = args[1]
        native = args[2]
        cursorObject.execute("INSERT INTO language VALUES(:language, :level, :native)",
                             {'language': language, 'level': level, 'native': native})
        return connObject.commit()

    @staticmethod
    def insert_personal_values(*args):
        first_name = args[0]
        last_name = args[1]
        birthday = args[2]
        phone = args[3]
        email = args[4]
        github = args[5]
        country = args[6]
        cursorObject.execute("INSERT INTO personal_info VALUES"
                             "(:first_name, :last_name, :birthday, "
                             ":phone, :email, :github, :country)",
                             {'first_name': first_name, 'last_name': last_name, 'birthday': birthday,
                              'phone': phone, 'email': email, 'github': github, 'country': country})
        return connObject.commit()

    @staticmethod
    def insert_skills_values(*args):
        object = args[0]
        level = args[1]
        cursorObject.execute("INSERT INTO skills VALUES"
                     "(:object, "
                     ":level)",
                     {'object': object, 'level': level})
        return connObject.commit()

    @staticmethod
    def insert_hobby_values(*args):
        hobby = args[0]
        link = args[1]
        cursorObject.execute("INSERT INTO hobbies VALUES(:hobby, :link)",
                             {'hobby': hobby, 'link': link})
        return connObject.commit()


class CreateTables:
    """Create tables for SQLite database"""
    @staticmethod
    def create_table_personal_info():
        create_table_personal = "CREATE TABLE personal_info" \
                              "(first_name STRING, " \
                              "last_name STRING," \
                              "birthday STRING," \
                              "phone numeric(0,9)," \
                              "email STRING," \
                              "github STRING," \
                              "country STRING)"
        return cursorObject.execute(create_table_personal)

    @staticmethod
    def create_table_language():
        create_table_language = """CREATE TABLE language \
                          (language STRING,  \
                          level STRING, \
                          native BOOLEAN)"""
        return cursorObject.execute(create_table_language)

    @staticmethod
    def create_table_skills():
        create_table_skills = "CREATE TABLE skills" \
                            "(object STRING, " \
                            "level STRING)"
        return cursorObject.execute(create_table_skills)

    @staticmethod
    def create_table_hobbies():
        create_table_skills = "CREATE TABLE hobbies" \
                            "(hobby STRING, " \
                            "link STRING)"
        cursorObject.execute(create_table_skills)