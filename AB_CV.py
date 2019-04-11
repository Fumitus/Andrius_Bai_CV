import sqlite3

connObject = sqlite3.connect("AB_CV.db")
cursorObject = connObject.cursor()

# drop table with the same name

dropTablePersonal = "DROP TABLE personal_info"
dropTableLanguage = "DROP TABLE language"
dropTableSkills = "DROP TABLE skills"
dropTableHobbies = "DROP TABLE hobbies"
cursorObject.execute(dropTableSkills)
cursorObject.execute(dropTablePersonal)
cursorObject.execute(dropTableLanguage)
cursorObject.execute(dropTableHobbies)


# create new table personal_info
createTablePersonal = "CREATE TABLE personal_info" \
                      "(id INT PRIMARY KEY NOT NULL, " \
                      "first_name STRING, " \
                      "last_name STRING,"\
                      "birthday STRING,"\
                      "phone numeric(0,9)," \
                      "email STRING," \
                      "github STRING," \
                      "country STRING)"
cursorObject.execute(createTablePersonal)

# insert values to table personal_info
insertValues = "INSERT INTO personal_info VALUES" \
               "(1," \
               "'Andrius'," \
               "'Baikštis', " \
               "'1983-09-21'," \
               "'37061687612'," \
               "'abaikstys@gmail.com'," \
               "'http://github.com/Fumitus/Andrius_Bai_CV.git'," \
               "'Lithuania')"
cursorObject.execute(insertValues)

# create new table languages
createTableLanguage = "CREATE TABLE language" \
                      "(id INT PRIMARY KEY NOT NULL, " \
                      "language STRING, " \
                      "level STRING," \
                      "native BOOLEAN)"
cursorObject.execute(createTableLanguage)

# insert values languages
insertLanguage_1 = "INSERT INTO language VALUES" \
                   "(1, " \
                   "'English', " \
                   "'B1 (CEFR)', " \
                   "0)"
cursorObject.execute(insertLanguage_1)

insertLanguage_2 = "INSERT INTO language VALUES" \
                   "(2, " \
                   "'Russian', " \
                   "'B1 (CEFR)', " \
                   "0)"
cursorObject.execute(insertLanguage_2)

insertLanguage_3 = "INSERT INTO language VALUES" \
                   "(3, " \
                   "'Lithuanian', " \
                   "'native', " \
                   "1)"
cursorObject.execute(insertLanguage_3)
connObject.commit()

# create new table skills
createTableSkills = "CREATE TABLE skills" \
                      "(id INT PRIMARY KEY NOT NULL, " \
                      "object STRING, " \
                      "level STRING)"
cursorObject.execute(createTableSkills)

# insert values skills
insertSkill_1 = "INSERT INTO skills VALUES" \
                   "(1, " \
                   "'Linux', " \
                   "'Can install system. " \
                "Create and manage users. " \
                "Create automatic service. Automatic start/restart on condition." \
                "Familiar with different access levels." \
                "At home have server running on Ubuntu 18.04.')"
cursorObject.execute(insertSkill_1)

insertSkill_2 = "INSERT INTO skills VALUES" \
                   "(2, " \
                   "'Python3', " \
                   "'It is my first programming language. Can work with it independently.')"
cursorObject.execute(insertSkill_2)

insertSkill_3 = "INSERT INTO skills VALUES" \
                   "(3, " \
                   "'Flask', " \
                   "'Can work with it independently. Create blog with quite good user registration functionality. " \
                "https://github.com/Fumitus/Baiksciai_Family_Blog/tree/Only_registered')"
cursorObject.execute(insertSkill_3)

insertSkill_4 = "INSERT INTO skills VALUES" \
                   "(4, " \
                   "'GitHub', " \
                   "'Can work with it independently. https://github.com/Fumitus')"
cursorObject.execute(insertSkill_4)

insertSkill_5 = "INSERT INTO skills VALUES" \
                   "(5, " \
                   "'DataBase', " \
                   "'Can work with SQLite. Familiar with PostgreSQL. Can use it on Linux environmental')"
cursorObject.execute(insertSkill_5)

insertSkill_6 = "INSERT INTO skills VALUES" \
                   "(6, " \
                   "'PuTTY user', " \
                   "'pscp user. For connection using public/private key pairs. " \
                "For file transfer using pscp with -load OPTION')"
cursorObject.execute(insertSkill_6)

insertSkill_7 = "INSERT INTO skills VALUES" \
                   "(7, " \
                   "'Google_user', " \
                   "'Answers usually looking on Google search if not looking in books.')"
cursorObject.execute(insertSkill_7)

insertSkill_8 = "INSERT INTO skills VALUES" \
                   "(8, " \
                   "'Pycharm IDE', " \
                   "'Can work independently')"
cursorObject.execute(insertSkill_8)

insertSkill_9 = "INSERT INTO skills VALUES" \
                   "(9, " \
                   "'Pycharm IDE', " \
                   "'Can work independently. Using for daily tasks.')"
cursorObject.execute(insertSkill_9)

insertSkill_10 = "INSERT INTO skills VALUES" \
                   "(10, " \
                   "'MS Visual Studio Code', " \
                   "'Can work independently. Started programing with this IDE.')"
cursorObject.execute(insertSkill_10)

insertSkill_11 = "INSERT INTO skills VALUES" \
                   "(11, " \
                   "'Other Skills', " \
                   "'Familiar with Anaconda, Jupyter NoteBook. pandas, numpy libraries.')"
cursorObject.execute(insertSkill_11)

connObject.commit()

# create new table hobbies
createTableSkills = "CREATE TABLE hobbies" \
                      "(id INT PRIMARY KEY NOT NULL, " \
                      "hobby STRING, " \
                      "link STRING)"
cursorObject.execute(createTableSkills)

insertHobby_1 = "INSERT INTO hobbies VALUES" \
                   "(1, " \
                   "'Windsurfing', " \
                   "'First choice.')"
cursorObject.execute(insertHobby_1)

insertHobby_2 = "INSERT INTO hobbies VALUES" \
                   "(2, " \
                   "'Radio control models', " \
                   "'Like to make planes. Upgrade with different FPV and/or flight controllers.')"
cursorObject.execute(insertHobby_2)

insertHobby_3 = "INSERT INTO hobbies VALUES" \
                   "(3, " \
                   "'Travel', " \
                   "'Like to travel and can plan my working day by myself.')"
cursorObject.execute(insertHobby_3)

# select from DB

queryTable_personal_info = "SELECT first_name, last_name, birthday, phone, email, github, country FROM personal_info"
queryResults_personal_info = cursorObject.execute(queryTable_personal_info)

# Print personal query results
print("First name, Last name, Born On, Phone number, email, git_repo_CV, Living place")
for result in queryResults_personal_info:
    print(result)
print("")

queryTable_language = "SELECT * FROM language"
queryResults_language = cursorObject.execute(queryTable_language)

# Print language query results

print("LanguageID, Language, Level, is_native?")
for result in queryResults_language:
    print(result)

# Skills query
queryTable_skills = "SELECT * FROM skills"
queryResults_skills = cursorObject.execute(queryTable_skills)

# Print skills query results

print("Skill_ID, Object, Level")
for result in queryResults_language:
    print(result)

connObject.close()


