#Hierarchical inheritance
class Student:
	def __init__(self,usn=None,name=None,age=None):
		self.usn=usn
		self.name=name
		self.age=age
	def getdata(self):
		self.usn=input("Enter the USN :")
		self.name=input("Enter the name:")
		self.age=int(input("Enter the age:"))
	def display(self):
		print("USN=",self.usn)
		print("Name=",self.name)
		print("Age=",self.age)
class ugstudent(Student):
	def __init__(self,sem=0,fees=0,stipend=0):
		self.sem=sem
		self.fees=fees
		self.stipend=stipend
	def ugdata(self):
		self.sem=int(input("Enter the semester:"))
		self.fees=int(input("Enter the fees:"))
		self.stipend=int(input("Enter the stipend:"))
	def ugdisplay(self):
		print("Semester=",self.sem)
		print("Fees=",self.fees)
		print("Stipend=",self.stipend)
class pgstudent(Student):
	def __init__(self,sem=0,fees=0,stipend=0):
		self.sem=sem
		self.fees=fees
		self.stipend=stipend
	def pgdata(self):
		self.sem=int(input("Enter the semester:"))
		self.fees=int(input("Enter the fees:"))
		self.stipend=int(input("Enter the stipend:"))
	def pgdisplay(self):
		print("Semester=",self.sem)
		print("Fees=",self.fees)
		print("Stipend=",self.stipend)

ug=ugstudent()
pg=pgstudent()
while True:
	print("MENU")
	print("-"*60)
	print("1.UG STUDENT \n2.PG STUDENT")
	print("-"*60)
	ch=int(input("Enter your choice:"))
	if ch==1:
		ug.getdata()
		ug.ugdata()
		print("UG STUDENT DETAILS")
		print("-"*60)
		ug.display()
		ug.ugdisplay()
	elif ch==2:
		pg.getdata()
		pg.pgdata()
		print("PG STUDENT DISPLAY")
		print("-"*60)
		pg.display()
		pg.pgdisplay()

	else:
		exit(0)
