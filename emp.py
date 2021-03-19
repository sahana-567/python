d={ }
class Employee:
	def salary_slip(self,name,address,panno,basic,deduct):
		self.name=name
		self.address=address
		self.panno=panno
		self.basic=basic
		self.hra=1.157*basic
		self.da=0.25*basic
		self.cca=300
		self.pf=1800
		self.pt=200
		self.tds=10
		self.deduct=deduct
		netsal=self.basic+self.da+self.hra+self.cca-(self.pf+self.pt+self.tds+self.deduct)
		return netsal

	def accept(self):
		name=input("enter the employee  name")
		address=input("enter the addresses")
		panno=input("enter the panno")
		basic=int(input("enter the basic salary"))
		deduct=int(input("enter the deduct"))
		self.netsal=self.salary_slip(name,address,panno,basic,deduct)

	def display(self):
		print("name=" ,self.name)
		print("address=" ,self.address)
		print("panno=" ,self.panno)
		print("basic=" ,self.basic)
		print("deduct =",self.deduct)
		print("netsal:",self.netsal)
	def search(self,name):
		for k,v in d.items():
			print("k=",k)
			print("v=",v)
			if k == name:
				print("name:{0},address:{1},panno:{2}".format(v.name,v.address,v.panno))
				print("basic= ",v.basic)
				print("hra= ",v.hra)
				print("da= ",v.da)
				print("cca= ",v.cca)
				print("pf= ",v.pf)
				print("pt= ",v.pt)
				print("tds= ",v.tds)
				print("deduct= ",v.deduct)
				print("netsal= ",v.netsal)
				print(v.__dict__)
while True:
	
	print("--------------------pay band scale----------------------")
	print("1-------->enter the employee details")
	print("2--------->dispalay the details")
	print("3--------->update  the details")
	print("4---------->search")
	print("5----------->exit")
	ch=int(input("enter ur choice"))
	if ch==1:
		print("enter the employee details")
		e=Employee()
		e.accept()
	elif ch==2:
		print("-"*60)
		print("display the employee details")
		e.display()
		print("-"*60)
	elif ch==3:
		print("-"*60)
		print("update  the dictionary")
		d.update({e.name:e})
		print(d)
		print("-"*60)
	elif ch==4:
		print("-"*60)
		print("search the name of the dictionary")
		e.search(input("enter a name"))
		print(e)
		print("-"*60)
	elif ch==5:
		break

	else:
		print("*"*60)
		print("invalid")

