import sqlite3

connObject = sqlite3.connect("AB_CV.db")
cursorObject = connObject.cursor()

# drop table with the same name

dropTablePersonal = "DROP TABLE personal_info"
dropTableLanguage = "DROP TABLE language"
dropTableSkills = "DROP TABLE skills"
dropTableHobbies = "DROP TABLE hobbies"
dropTableInterests = "DROP TABLE interests"
dropTableCourses = "DROP TABLE courses"
cursorObject.execute(dropTableSkills)
cursorObject.execute(dropTablePersonal)
cursorObject.execute(dropTableLanguage)
cursorObject.execute(dropTableHobbies)
cursorObject.execute(dropTableInterests)
cursorObject.execute(dropTableCourses)


# create new table personal_info
createTablePersonal = "CREATE TABLE personal_info" \
                      "(first_name STRING, " \
                      "last_name STRING,"\
                      "birthday STRING,"\
                      "phone numeric(0,9)," \
                      "email STRING," \
                      "github STRING," \
                      "country STRING)"
cursorObject.execute(createTablePersonal)

# insert values to table personal_info
insertValues = "INSERT INTO personal_info VALUES" \
               "('Andrius'," \
               "'Baikštis', " \
               "'1983-09-21'," \
               "'37061687612'," \
               "'abaikstys@gmail.com'," \
               "'http://github.com/Fumitus/Andrius_Bai_CV.git'," \
               "'Lithuania')"
cursorObject.execute(insertValues)

# create new table languages
createTableLanguage = "CREATE TABLE language" \
                      "(language STRING, " \
                      "level STRING," \
                      "native BOOLEAN)"
cursorObject.execute(createTableLanguage)

# insert values languages
insertLanguage_1 = "INSERT INTO language VALUES" \
                   "('English', " \
                   "'B1 (CEFR)', " \
                   "0)"
cursorObject.execute(insertLanguage_1)

insertLanguage_2 = "INSERT INTO language VALUES" \
                   "('Russian', " \
                   "'B1 (CEFR)', " \
                   "0)"
cursorObject.execute(insertLanguage_2)

insertLanguage_3 = "INSERT INTO language VALUES" \
                   "('Lithuanian', " \
                   "'native', " \
                   "1)"
cursorObject.execute(insertLanguage_3)
connObject.commit()

# create new table skills
createTableSkills = "CREATE TABLE skills" \
                      "(object STRING, " \
                      "level STRING)"
cursorObject.execute(createTableSkills)

# insert values skills
insertSkill_1 = "INSERT INTO skills VALUES" \
                   "('Linux', " \
                   "'Can install system. " \
                "Create and manage users. " \
                "Create automatic service. Automatic start/restart on condition." \
                "Familiar with different access levels." \
                "At home have server running on Ubuntu 18.04.')"
cursorObject.execute(insertSkill_1)

insertSkill_2 = "INSERT INTO skills VALUES" \
                   "('Python3', " \
                   "'It is my first programming language. Can work with it independently.')"
cursorObject.execute(insertSkill_2)

insertSkill_3 = "INSERT INTO skills VALUES" \
                   "('Flask', " \
                   "'Can work with it independently. Create blog with quite good user registration functionality. " \
                "https://github.com/Fumitus/Baiksciai_Family_Blog/tree/Only_registered')"
cursorObject.execute(insertSkill_3)

insertSkill_4 = "INSERT INTO skills VALUES" \
                   "('GitHub', " \
                   "'Can work with it independently. https://github.com/Fumitus')"
cursorObject.execute(insertSkill_4)

insertSkill_5 = "INSERT INTO skills VALUES" \
                   "('DataBase', " \
                   "'Can work with SQLite. Familiar with PostgreSQL. Can use it on Linux environmental')"
cursorObject.execute(insertSkill_5)

insertSkill_6 = "INSERT INTO skills VALUES" \
                   "('PuTTY user', " \
                   "'pscp user. For connection using public/private key pairs. " \
                "For file transfer using pscp with -load OPTION')"
cursorObject.execute(insertSkill_6)

insertSkill_7 = "INSERT INTO skills VALUES" \
                   "('Google_user', " \
                   "'Answers usually looking on Google search if not looking in books.')"
cursorObject.execute(insertSkill_7)

insertSkill_8 = "INSERT INTO skills VALUES" \
                   "('Pycharm IDE', " \
                   "'Can work independently')"
cursorObject.execute(insertSkill_8)

insertSkill_9 = "INSERT INTO skills VALUES" \
                   "('Pycharm IDE', " \
                   "'Can work independently. Using for daily tasks.')"
cursorObject.execute(insertSkill_9)

insertSkill_10 = "INSERT INTO skills VALUES" \
                   "('MS Visual Studio Code', " \
                   "'Can work independently. Started programing with this IDE.')"
cursorObject.execute(insertSkill_10)

insertSkill_11 = "INSERT INTO skills VALUES" \
                   "('Other Skills', " \
                   "'Familiar with Anaconda, Jupyter NoteBook. pandas, numpy libraries.')"
cursorObject.execute(insertSkill_11)
connObject.commit()

# create new table hobbies
createTableHobbies = "CREATE TABLE hobbies" \
                      "(hobby STRING, " \
                      "info STRING)"
cursorObject.execute(createTableHobbies)

insertHobby_1 = "INSERT INTO hobbies VALUES" \
                   "('Windsurfing', " \
                   "'First choice hobby.')"
cursorObject.execute(insertHobby_1)

insertHobby_2 = "INSERT INTO hobbies VALUES" \
                   "('Radio control models', " \
                   "'Like to make planes. Upgrade with different FPV and/or flight controllers.')"
cursorObject.execute(insertHobby_2)

insertHobby_3 = "INSERT INTO hobbies VALUES" \
                   "('Travel', " \
                   "'Like to travel and can plan my working day by myself.')"
cursorObject.execute(insertHobby_3)
connObject.commit()

# create new table interests
createTableInterests = "CREATE TABLE interests" \
                      "(interest STRING, " \
                      "info STRING)"
cursorObject.execute(createTableInterests)

insertInterest_1 = "INSERT INTO interests VALUES" \
                   "('Artificial Intelligence', " \
                   "'Just started to study.')"
cursorObject.execute(insertInterest_1)

insertInterest_2 = "INSERT INTO interests VALUES" \
                   "('Machine learning', " \
                   "'Just started to study.')"
cursorObject.execute(insertInterest_2)
connObject.commit()

# create new table courses
createTableCourses = "CREATE TABLE courses" \
                      "(interest STRING, " \
                      "info STRING)"
cursorObject.execute(createTableCourses)

insertCourse_1 = "INSERT INTO courses VALUES" \
                   "('Artificial Intelligence', " \
                   "'Just started to study.')"
cursorObject.execute(insertCourse_1)
connObject.commit()

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
for result in queryResults_skills:
    print(result)

# Hobbies query
queryTable_hobbies = "SELECT * FROM hobbies"
queryResults_hobbies = cursorObject.execute(queryTable_hobbies)

# Print hobbies query results
print("Skill_ID, Object, Level")
for result in queryResults_hobbies:
    print(result)

connObject.close()


