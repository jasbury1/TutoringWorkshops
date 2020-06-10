
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
    first_name = ""
    last_name = ""
    student_id = None
    major = ""
    units_completed = 0
    grade_points = 0

    def __init__(self, first_name, last_name, stu_id):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = stu_id
        

    def __repr__(self):
        return ("Student: {0} {1} {2} {3}".format(self.first_name, 
            self.last_name, self.student_id, self.major))

    def update_grade_points(self, units, grade):
        gp = 0
        if(grade.upper() == 'A'):
            gp = 4
        elif(grade.upper() == 'B'):
            gp = 3
        elif(grade.upper() == 'C'):
            gp = 2
        elif(grade.uppder() == 'D'):
            gp = 1
        else:
            gp = 0

        self.grade_points += gp
        self.units_completed += units

    def calculate_gpa(self):
        return float(self.grade_points / self.units_completed)

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

    def __init__(self, college_name):
        self.college_name = college_name
        students = []

    def add_student(self, student):
        self.students.append(student)

    def get_highest_gpa(self):
        highest_gpa = -1
        student = None

        for s in self.students:
            if s.calculate_gpa() > highest_gpa:
                student = s
                highest_gpa = s.calculate_gpa()
       
        return student

def main():
    stu1 = Student("James", "Asbury", 34534980)
    stu1.major = "Computer Science"
    stu1.units_completed = 80
    stu1.grade_points = 280

    print(stu1)
    print("{}'s GPA: {}".format(stu1.first_name, stu1.calculate_gpa()))
    stu1.update_grade_points(4, 'B')
    print("{}'s GPA: {}".format(stu1.first_name, stu1.calculate_gpa()))

    ceng = College("College of Engineering")
    ceng.add_student(stu1)

    print(ceng.get_highest_gpa())


if __name__ == '__main__':
    main()
