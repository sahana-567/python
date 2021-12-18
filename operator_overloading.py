#overload operators and function using modules
class Oper:
	def __init__(self):
		self.alist=[]
	def get(self):
		n=int(input("Enter the list size:"))
		for i in range(0,n):
			ele=int(input("Enter the elements:"))
			self.alist.append(ele)
			#print(self.alist)
	def __add__(self,other):
		new_list=[]
		for i in range(0,len(self.alist)):
			new_list.append(self.alist[i]+other.alist[i])
		print(new_list)
	def __sub__(self,other):
		new_list=[]
		for i in range(0,len(self.alist)):
			new_list.append(self.alist[i]-other.alist[i])
		print(new_list)
	def __mul__(self,other):
		new_list=[]
		for i in range(0,len(self.alist)):
			new_list.append(self.alist[i]*other.alist[i])
		print(new_list)
	def __floordiv__(self,other):
		new_list=[]
		for i in range(0,len(self.alist)):
			new_list.append(self.alist[i]//other.alist[i])
		print(new_list)

#ov1=Oper()
#ov2=Oper()
