#Given a string represnting the student's gpa, convert to a float 
#and raise ValueError if the given gpa is not between 0 and 4.
#	string -> float  
def convertGPA(gpa):
	gpa = float(gpa)
	if(gpa < 0 or gpa > 4):
		raise ValueError
	return gpa


#Calculate the average gpa of the given list. Return -1 if list is empty.
#	list -> float  
def calculateAverage(gpas):
	if(len(gpas) == 0):
		return -1
	sum = 0
	for gpa in gpas:
		sum += gpa
	return sum / len(gpas)