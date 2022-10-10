import pytest
import System

username = 'calyam' #prof
password =  '#yeet'
role = 'professor'
username2 = 'hdjsr7'
password2 = 'pass1234'
studentUser = 'yted91'
studentPass = 'imoutofpasswordnames'
course = 'cloud_computing'
assignment = 'assignment1'
profUser = 'goggins'
profPass = 'augurrox'

# 1. login - System.py
# The login function takes a name and password and sets the user for the program. Verify that the correct user is created with this test, and use the json files to check that it adds the correct data to the user.
def test_login(grading_system):
    grading_system.login(username,password)
    if grading_system.usr.name != username:
        assert False
    if grading_system.usr.courses != [course]:
        assert False
    if grading_system.usr.users != System.System().load_user_db():
        assert False

# 2. check_password - System.py
# This function checks that the password is correct. Enter several different formats of passwords to verify that the password returns correctly if the passwords are the same.
def test_check_password(grading_system):
    pass1 = grading_system.check_password(username2, password2)
    pass2 = grading_system.check_password(username2, ' pass1234')
    pass3 = grading_system.check_password(username2, 'pass1234 ')
    if not pass1 or not pass2 or not pass3:
        assert False

# 3. change_grade - Staff.py
# This function will change the grade of a student and updates the database. Verify that the correct grade is changed on the correct user in the database.
def test_change_grade(grading_system):
    assignment = 'assignment1'
    grading_system.login(username, password)
    grading_system.usr.change_grade(studentUser, course, assignment, 100)
    grade = grading_system.usr.users[studentUser]['courses'][course][assignment]['grade']
    if grade != 100:
        assert False

# 4. create_assignment Staff.py
# This function allows the staff to create a new assignment. Verify that an assignment is created with the correct due date in the correct course in the database.
def test_create_assignment(grading_system):
    coding_assignment = 'coding_hw'
    grading_system.login(username, password)
    grading_system.usr.create_assignment(coding_assignment, '10/20/22', course)
    assignments = grading_system.usr.all_courses[course]['assignments']
    if coding_assignment not in assignments:
        assert False

# 5. add_student - Professor.py
# This function allows the professor to add a student to a course. Verify that a student will be added to the correct course in the database.
def test_add_student(grading_system):
    db_course = 'databases'
    grading_system.login(profUser, profPass)
    grading_system.usr.add_student(studentUser, db_course)
    classes = grading_system.usr.users[studentUser]['courses']
    if db_course not in classes:
        assert False

# 6. drop_student Professor.py
# This function allows the professor to drop a student in a course. Verify that the student is added and dropped from the correct course in the database.
def test_drop_student(grading_system):
    swe_course = 'software_engineering'
    grading_system.login(profUser, profPass)
    grading_system.usr.drop_student(studentUser, swe_course)
    classes = grading_system.usr.users[studentUser]['courses']
    if swe_course in classes:
        assert False

# 7. submit_assignment - Student.py
# This function allows a student to submit an assignment. Verify that the database is updated with the correct assignment, submission, submission dateand in the correct course.
def test_submit_assignment(grading_system):
    submit_stuff = 'nimbus is a type of cloud'
    submit_date = '10/9/22'
    grading_system.login(studentUser, studentPass)
    grading_system.usr.submit_assignment(course, assignment, submit_stuff, submit_date)
    submission = grading_system.usr.users[studentUser]['courses'][course][assignment]
    if submission['submission_date'] != submit_date or submission['submission'] != submit_stuff:
        assert False

# 8. check_ontime - Student.py
# This function checks if an assignment is submitted on time. Verify that it will return true if the assignment is on time, and false if the assignment is late.
def test_check_online(grading_system):
    hw_date = '10/31/22'
    due_date = '10/31/20'
    grading_system.login(studentUser, studentPass)
    if grading_system.usr.check_ontime(hw_date, due_date):
        assert False

# 9. check_grades - Student.py
# This function returns the users grades for a specific course. Verify the correct grades are returned for the correct user.
def test_check_grades(grading_system):
    grading_system.login(studentUser, studentPass)
    grades = grading_system.usr.check_grades(course)
    if grades['assignment2'] != 5:
        assert False

# 10. view_assignments - Student.py
# This function returns assignments and their due dates for a specific course. Verify that the correct assignments for the correct course are returned.
def test_view_assignments(grading_system):
    grading_system.login(studentUser, studentPass)
    assignments = grading_system.usr.view_assignments(course)
    if assignments['assignment1']['due_date'] != '1/3/20' or assignments['assignment2']['due_date'] != '2/3/20':
        assert False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem