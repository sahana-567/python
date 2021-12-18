#10 operations on strings
#LAB1
str1=input("Enter string 1:")
str2=input("Enter string 2:")
while True:
	print("-"*40)
	print("STRING OPERATIONS")
	print("-"*40)
	print("1.Repetation of String")
	print("2.Length of String")
	print("3.Concatenation of String")
	print("4.Reversing of string")
	print("5.Range Slicing")
	print("6.Slicing of string")
	print("7.String membership")
	print("8.Counting no. of occurrences in a string")
	print("9.capitalize a string")
	print("10.Spliting a string")
	print("11.Exit")
	print("-"*40)
	ch=int(input("Enter your choice:"))
	if ch==1:
		r=int(input("enter no. of repetations:"))
		print("repetation of the string is",(str1*r))
	if ch==2:
		print("Length of str1 is",len(str1))
		print("Length of str2 is",len(str2))
	if ch==3:
		str=str1+str2
		print("concatenation of string is",str)
	if ch==4:
		rev=str1[::-1]
		print("Reverse of a string is",rev)
	if ch==5:
		a=int(input("Enter starting index:"))
		b=int(input("Enter ending index:"))
		range=str1[a:b]
		print("range slicing of string is",range)
	if ch==6:
		a=int(input("Enter index:"))
		range=str1[a]
		print("Slicing of string is",range)
	if ch==7:
		char=input("enter the character to be searched:")
		m=char in str1
		print(m)
	if ch==8:
		char=input("Enter a character:")
		occr=str1.count(char)
		print("No.of occurences is",occr)
	if ch==9:
		print("Capital of the string1 is",str1.upper())
	if ch==10:
		print("splitting of the string2 is",str2.split())
	if ch==11:
		exit(0)
