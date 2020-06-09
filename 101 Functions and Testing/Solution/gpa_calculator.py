'''
  Write a program to calculate the average GPA of the class.
  Your program should prompt the user for the number of students
  in the class and then prompt the user for the GPA of each of
  the students.
  =================================================================
  Example runs:
  
  Enter number of students: 3
  Student 1 GPA: 3.0
  Student 2 GPA: 2.0
  Student 3 GPA: 4.0
  Average GPA: 3.0
  
  Enter number of students: 0
  Can not calculate average of 0 student GPAs.
  =================================================================
  Complete and unit test the functions in funcs.py before writing
  your main method (3 unit tests per method). After testing the 
  functions, write your main method and diff test the results 
  (3 diff tests).
'''

from funcs import *

def main():
	gpas = []
	num_students = int(input("Enter number of students: "))
	for student_num in range(num_students):
		request_string = "Student " + str(student_num) + " GPA: "
		gpa = input(request_string)
		gpas.append(convertGPA(gpa))
	average_gpa = calculateAverage(gpas)
	if(average_gpa != -1):
		print("Average GPA: " + str(average_gpa))
	else:
		print("Can not calculate average of 0 student GPAs.")
	
if __name__ == '__main__':
	main()
