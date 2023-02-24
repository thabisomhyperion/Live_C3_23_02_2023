'''
Inheritance:
Super Class - parent class - can exist without a child
Sub Class - child class - cannote exist without a parent

constructor function - first function that is executed when an object is created
'''
class Student:
	'''Constructor: first function that is execute when an object is created'''

	def __init__(self, name, surname, contacts):
		self.stud_name = name  # attribute (stud_name) assigned value of parametor(name)
		self.stud_surname = surname
		self.stud_contacts = contacts

	def get_contact(self):
		return self.stud_contacts

	def get_fullnames(self):
		return f"{self.stud_surname} {self.stud_name}"

	def __str__(self):
		return f"""--------------
Student Name: {self.stud_name}
Student Surname: {self.stud_surname}
Student Contact: {self.stud_contacts}
-------------"""


#Child class 
class PostGrad(Student):
	'''Constructor'''
	def __init__(self, stud_name, surname, contacts, qualification):
		super().__init__(stud_name, surname, contacts) # This is the constructor of the parent(Student). Invoking/ executing the constructor of the parent
		self.stud_qualf = qualification

	#Overidding, This is when a function from the parent is being redifined in the child class
	def __str__(self):
		return f"""--------------
Student Name: {self.stud_name}
Student Surname: {self.stud_surname}
Student Contact: {self.stud_contacts}
Student Qualification: {self.stud_qualf}
-------------"""

stud1 = ""


student_type = input("Enter type of a student(student or postgrad): ").lower()
if student_type == 'student':
	stud1 = Student('Lucas', 'Refilwe', '142536748596')
elif student_type == 'postgrad':
	stud1 = PostGrad("Alfred", 'Freddy', '2536475896', 'Software Engineering')

print(stud1)