class student:
	def __init__(self,usn=None,name=None,age=None):
		self.usn=usn
		self.name=name
		self.age=age
	def getdata(self):
		self.usn=input("enter the usn")
		self.name=input("enter the name")
		self.age=input("enter the age")
	def display(self):
		print("USN NO:", self.usn)
		print("NAME:",self.name)
		print("AGE:",self.age)
class UG(student):
	def __init__(self,sem=None,fee=None,stiphend=None):
		super().__init__(self)
		self.sem=sem
		self.fee=fee
		self.stiphend=stiphend
	def ugdata(self):
		self.getdata()
		self.sem=input("enter the sem:")
		self.fee=input("enter the fee:")
		self.stiphend=input("enter the stiphend:")
	def ugdisplay(self):
		self.display()
		print("UG sem:",self.sem)
		print("UG fee:",self.fee)
		print("UG stiphend:",self.stiphend)
class PG(student):
	def __init__(self,sem=None,fee=None,stiphend=None):
		super().__init__(self)
		self.sem=sem
		self.fee=fee
		self.stiphend=stiphend
	def pgdata(self):
		self.getdata()
		self.sem=input("enter the sem:")
		self.fee=input("enter the fee:")
		self.stiphend=input("enter the stiphend:")
	def pgdisplay(self):
		self.display()
		print("PG sem:",self.sem)
		print("PG fee:",self.fee)
		print("PG stiphend:",self.stiphend)
while 1:
	print("*"*60)
	print("             HIERARICAL INHERITANCE            ")
	print("*"*60)
	print("1.create UG\n 2.create PG\n 3.display UG data\n 4.display PG data")
	ch=int(input("Enter your choice"))
	if ch==1:
		s1=UG()
		s1.ugdata()
	elif ch==2:
		s2=PG()
		s2.pgdata()
	elif ch==3:
		s1.ugdisplay()
		print(s1.__dict__)
	elif ch==4:
		s2.pgdisplay()
		print(s2.__dict__)
	else:
		print("invalid choice")
		break;

