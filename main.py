'''
OOP I
- A class is an ideas
- Manifastation of the idea is an object

attributes > variable - temporaly storage of data
parametors > variable
An object, it is a vaiable that contains variables that data

'''
class Student:
	'''Constructor: first function that is execute when an object is created'''
	
	def __init__(self, name, surname, contacts ):
		self.stud_name = name # attribute (stud_name) assigned value of parametor(name)
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
def get_stud_data():
	stname= input("Name: ")
	stsurname= input("Surname: ")
	stcontacts= input("Contacts: ")

	return stname, stsurname, stcontacts
	
student_list = []
stud_object1 = Student("Look","Moses", "123456789")
stud_object2 = Student("Joseph","Luke", "321456987")
student_list.append(stud_object1)
student_list.append(stud_object2)

stname, stsurname, stcontacts = get_stud_data()
student_list.append(Student(stname, stsurname, stcontacts))

# print(stud_object1.get_fullnames())
# print(stud_object2)
for stud in student_list:
	print(stud)

numb = []

numb.append(5)
n = 8
numb.append(n)