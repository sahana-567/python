import os
from operator_overloading import *
#os.system('clear')
ov1=Oper()
ov2=Oper()
ov1.get()
ov2.get()
while True:
	print("-"*40)
	print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Floor Division")
	ch=int(input("Enter your choice:"))
	print("-"*40)
	if ch==1:
		ov1+ov2
	elif ch==2:
		ov1-ov2
	elif ch==3:
		ov1*ov2
	elif ch==4:
		ov1//ov2
	else:
		exit()

