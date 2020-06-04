# -*- coding: utf-8 -*-
from CV.insert import InsertValues, CreateTables
from CV import connObject, DropTable
from CV.export_results import ExportQuery
import pdfkit


def export_cv():
    options = {

        'margin-top': '0.751in',
        'margin-right': '0.751in',
        'margin-left': '0.751in',
        'margin-bottom': '0.751in',
        'encoding': "UTF-8",
        'custom-header': [('Accept_Encoding', 'gzip')],
        '--header-html': 'CV/cv_header.html',
        'no-outline': None
    }
    pdfkit.from_file('CV/AB_CV.html', 'CV/AB_CV.pdf', options=options)


def main():
    # drop table with the same name
    DropTable("DROP TABLE IF EXISTS personal_info")
    DropTable("DROP TABLE IF EXISTS courses")
    DropTable("DROP TABLE IF EXISTS language")
    DropTable("DROP TABLE IF EXISTS skills")
    DropTable("DROP TABLE IF EXISTS hobbies")

    # create new table personal_info
    CreateTables.create_table_personal_info()

    # create new table courses
    CreateTables.create_table_courses()

    # create new table languages
    CreateTables.create_table_language()

    # create new table skills
    CreateTables.create_table_skills()

    # create new table hobbies
    CreateTables.create_table_hobbies()

    # insert values to table personal_info
    # 'first_name', 'last_name', 'birthday' in format YYYY-mm-dd,
    # 'phone', 'email', 'github repository', 'country' living place
    InsertValues.insert_personal_values('Andrius', 'Baikštis',
                                        '1983-09-21', '37061687612',
                                        'abaikstys@gmail.com', 'linkedin.com/in/andrius-baikštis-5b43081a1',
                                        'Lithuania')

    # insert values courses
    InsertValues.insert_courses_values('Kaunas Coding School',
                                      'https://www.vilniuscoding.lt/mokymai/python-mokymai-kaune/',
                                      'From 2018 October to 2018 December')

    InsertValues.insert_courses_values('Edureka',
                                      'https://www.edureka.co/software-testing',
                                      'From 2019 July')

    # insert values languages 'Language', 'Level', 'Is native' 0 or 1
    InsertValues.insert_language_values('English', 'B1 (CEFR)', 0)
    InsertValues.insert_language_values('Russian', 'B1 (CEFR)', 0)
    InsertValues.insert_language_values('Lithuanian', 'native', 1)

    # insert values skills
    InsertValues.insert_skills_values('Linux',
                                      'Can work with it independently.')

    InsertValues.insert_skills_values('Windows',
                                      'Can work with it independently.')

    InsertValues.insert_skills_values('Python3',
                                      'It is my first programming language. Can work with it independently.')

    InsertValues.insert_skills_values('Java',
                                      'It is my second programming language. '
                                      'Enouth skills to create code for automated web testing.')

    InsertValues.insert_skills_values('Flask',
                                      'Can work with it independently.')

    InsertValues.insert_skills_values('Django',
                                      'Can work with it independently.')

    InsertValues.insert_skills_values('GitHub',
                                      'Can work with it independently. '
                                      'https://github.com/Fumitus?tab=repositories')

    InsertValues.insert_skills_values('DataBase',
                                      'Can work with SQLite, MySQL, MariaDB independently.')

    InsertValues.insert_skills_values('PuTTY user',
                                      'Can work with it independently.')
    InsertValues.insert_skills_values('Docker_user',
                                      'Can work with it independently.')

    InsertValues.insert_skills_values('Google_user',
                                      'Answers usually looking on Google search if not looking in books.')

    InsertValues.insert_skills_values('Pycharm IDE', 'Can work independently. Using for daily tasks.')

    InsertValues.insert_skills_values('MS Visual Studio Code',
                                      'Can work independently. Started programing with this IDE.')

    InsertValues.insert_skills_values('Other Skills',
                                      'Familiar with Anaconda, Jupyter NoteBook. pandas, numpy libraries.')

    InsertValues.insert_skills_values('Risk analysis',
                                      'Have working experience with FMEA risk analysis methodology')

    InsertValues.insert_skills_values('Software tester',
                                      'Can create automated tests')

    # insert hobbies values
    InsertValues.insert_hobby_values('Windsurfing', 'First choice.')
    InsertValues.insert_hobby_values('Radio control models',
                                     'Like to make planes. Upgrade with different FPV and/or flight controllers.')
    InsertValues.insert_hobby_values('Travel', 'Like to plan our family trips by myself.')

    # select from DB and print results

    ExportQuery("SELECT * FROM personal_info")
    ExportQuery("SELECT * FROM courses")
    ExportQuery("SELECT * FROM language")
    ExportQuery("SELECT * FROM skills")
    ExportQuery("SELECT * FROM hobbies")

    export_cv()

    connObject.close()
