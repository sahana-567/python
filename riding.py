class employee:
	ramt=1.04
	def __init__(self,fname=None,lname=None,bs=None):
		self.fname=fname
		self.lname=lname
		self.bs=bs
	def getdata(self):
		self.fname=input("enter the fname")
		self.lname=input("enter the lname")
		self.bs=int(input("enter the bs"))
	def display(self):
		print("fullname",self.fname+self.lname)
		print("basicsalary",self.bs)
class manager(employee):
	ramt=1.05
	def dispraise(self):
		print("after raising salary:",self.bs*self.ramt)
class salesman(employee):
	ramt=1.10
	def dispraise(self):
		print("the salary:",self.bs*self.ramt)
m1=manager()
s1=salesman()
while 1:
	print("1.manager information")
	print("2.salesperson information")
	ch=int(input("enter ur choice"))
	if ch==1:
		m1.getdata()
		m1.display()
		m1.dispraise()
	elif ch==2:
		s1.getdata()
		s1.display()
		s1.dispraise()
	else:
		print("invalid")
		break;
