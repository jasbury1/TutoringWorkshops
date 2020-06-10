
'''
  This class will be used to represent a college student
  =================================================================

  The following shows an example of how we want to create students

  stu = Student("James", "Asbury", 12496940)

  new classes are created using a string first name, string last name, 
  and an integer student_id. These are the parameters our __init__
  will need.

  Each student also has the following:
  - Major
  - Units completed
  - Grade points

  =================================================================
'''

class Student:
    # TODO Step 1: Here's the class data. Add the missing 3 class members
    # described in the class description
    first_name = ""
    last_name = ""
    student_id = None

    # TODO Step 2: Complete the init by setting our classes last name,
    # and id to the parameters passed in as arguments to the init
    def __init__(self, first_name, last_name, stu_id):
        self.first_name = first_name
        pass

    # TODO step 3: Complete the repr so that we can print out the students
    # last name, ID, and major as well
    def __repr__(self):
        return ("Student: {0}".format(first_name))


    # TODO Step 4 Complete the following function that adds a class grade and
    # units to our running total
    # if the string 'A' is passed in as a grade, grade points should go
    # up by 4. 'B' is 3, 'C' is 2, 'D' is 1, 'F' is 0
    def update_grade_points(self, units, grade):
        pass

    #TODO Step 5: Write a calculate GPA function that returns the result of dividing
    # grade points by total units
    def calculate_gpa(self):
        pass

'''
  This class will be used to represent a college at cal poly
  =================================================================

  Complete the functionality

  =================================================================
'''

class College:
    college_name = ""
    students = []
    num_students = 0

    # TODO Step 6: Init takes a college name
    def __init__(self):
        pass

    # TODO Step 7: Write a method to add a student object to our list
    def add_student(self, student):
        pass

    # TODO Step 8: Write a method to go through the list 'students' and
    # return the student with the highest GPA
    def get_highest_gpa(self):
        pass

def main():
    # TODO: Uncomment these lines once you've implemented their functionality

    #stu1 = Student("James", "Asbury", 34534980)
    #stu1.major = "Computer Science"
    #stu1.units_completed = 80
    #stu.grade_points = 280

    #print(stu1)
    #print("{}'s GPA: {}".format(stu1.first_name, stu1.calculate_gpa()
    #stu1.update_grade_points(4, "B")
    #print("{}'s GPA: {}".format(stu1.first_name, stu1.calculate_gpa()

    # TODO: Create a few more Student objects
    # TODO: Create a College object and add all of our students to the college.
    # TODO: Make sure the get_highest_gpa function works!


if __name__ == '__main__':
    main()
