#multilevel inheretance
class Student:
	def __init__(self,usn=None,name=None,age=None):
		self.usn=usn
		self.name=name
		self.age=age
	def getdata(self):
		self.usn=input("Enter the USN:")
		self.name=input("Enter the name:")
		self.age=input("Enter the age:")
class Subject(Student):
	def __init__(self,sem=0,sub1=0,sub2=0,sub3=0,sub4=0,sub5=0):
		self.sem=sem
		self.sub1=sub1
		self.sub2=sub2
		self.sub3=sub3
		self.sub4=sub4
		self.sub5=sub5
	def subject_marks(self):
		self.sem=int(input("Enter the semester:"))
		self.sub1=int(input("Enter subject 1 marks:"))
		self.sub2=int(input("Enter subject 2 marks:"))
		self.sub3=int(input("Enter subject 3 marks:"))
		self.sub4=int(input("Enter subject 4 marks:"))
		self.sub5=int(input("Enter subject 5 marks:"))
class Result(Subject):
	def display_res(self):
		self.tot=int(self.sub1+self.sub2+self.sub3+self.sub4+self.sub5)
		self.percent=int((self.tot/500)*100)
		print("STUDENT REPORT")
		print("-"*40)
		print("USN=",self.usn)
		print("Name=",self.name)
		print("Percentage=",self.percent)
		print("-"*40)

s=Result()
s.getdata()
s.subject_marks()
s.display_res()

