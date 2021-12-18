d={}
class Employee:
	def salary(self,name,addr,pan,basic,tds,deduct):
		self.name=name
		self.addr=addr
		self.pan=pan
		self.basic=basic
		self.tds=tds
		self.deduct=deduct
		self.hra=0.5*self.basic
		self.da=0.8*self.basic
		self.gross=self.basic+self.hra+self.da
		self.netsal=self.gross-self.deduct
		#return self.gross
		#return self.netsal

	def __init__(self):
		name=input("Enter the name:")
		addr=input("Enter the address:")
		pan=input("Enter pan no:")
		basic=int(input("Enter basic sal:"))
		tds=int(input("Enter tds:"))
		deduct=int(input("Enter deduct:"))
		self.salary(name,addr,pan,basic,tds,deduct)
	def display(self):
		print("Name=",self.name)
		print("Address=",self.addr)
		print("PAN=",self.pan)
		print("Basic=",self.basic)
		print("TDS=",self.tds)
		print("Deduct=",self.deduct)
		print("Gross salary=",self.gross)
		print("Net Salary=",self.netsal)
	def search(self,name):
		for k,v in d.items():
			if k==name:
				print("Employee found")
				print(v.__dict__)
				break
			else:
				print("Employee not found")
while True:
	print("1.Enter employee details\n2.Update employee details")
	print("3.Display employee details\n4.Search for an employee")
	ch=int(input("Enter your choice:"))
	print("-"*40)
	if ch==1:
		e=Employee()
		print("Details entered successfully")
		print("-"*40)
	elif ch==2:
		d.update({e.name:e})
		print("Update successful",d)
		print("-"*40)
	elif ch==3:
		e.display()
		print("-"*40)
	elif ch==4:
		name=input("Enter the name:")
		e.search(name)
	else:
		print("Invalid choice")

