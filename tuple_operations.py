<<<<<<< HEAD
 #10 operations of tuples
=======
#10 operations of tuples
>>>>>>> 808e13ac29073fefe51ab18ffde8eb08f00789a7
#LAB1
import random
while True:
	print("-"*40)
	print("TUPLE OPERATIONS")
	print("-"*40)
	print("1.Create a tuple")
	print("2.Repetation of tuple")
	print("3.Length of tuple")
	print("4.Concatenation of tuple")
	print("5.Slicing of tuple")
	print("6.Membership operation")
	print("7.Itration of tuple")
	print("8.Maximum value of tuple")
	print("9.Minimum value of tuple")
	print("10.Delete a tuple")
	print("-"*40)
	ch=int(input("Enter your choice:"))
	if ch==1:
		list1=[]
		list2=[]
		n=int(input("Enter the size of the list:"))
<<<<<<< HEAD
 		for i in range(0,n):
=======
		for i in range(0,n):
>>>>>>> 808e13ac29073fefe51ab18ffde8eb08f00789a7
			list1.append(random.randrange(0,50))
		for i in range(0,n):
			list2.append(random.randrange(0,50))
		tup1=tuple(list1)
		tup2=tuple(list2)
		print("Tuple1=",tup1)
		print("Tuple2=",tup2)
	elif ch==2:
		r=int(input("Enter no.of repetations:"))
		print("Repetation of tuple is",(tup1*r))
	elif ch==3:
		print("Length of tuple1 =",len(tup1))
		print("Length of tuple2 =",len(tup2))
	elif ch==4:
		tup=tup1+tup2
		print("Concatenation of tuple is",tup)
	elif ch==5:
		a=int(input("Enter the index:"))
		range=tup1[a]
		print("Slicing of tuple is",range)
	elif ch==6:
		char=int(input("Enter the element to be searched:"))
		m=char in tup1
		print(m)
	elif ch==7:
		for i in tup1:
			print(i)
	elif ch==8:
		print("Maximum of tuple1 is",max(tup1))
		print("Maximum of tuple2 is",max(tup2))
	elif ch==9:
		print("Minimum of tuple1 is",min(tup1))
		print("Minimum of tuple2 is",min(tup2))
	elif ch==10:
		del tup1
		print("Tuple deleted")
	else:
		print("Invalid choice!")

