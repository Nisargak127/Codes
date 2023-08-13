from dund import *
obj1=Dunder()
obj2=Dunder()
obj1.accept(obj2)

while True:
	print("1.Less Than\n2.Greater Than\n3.Less than equal to\n4.Greater than equal to\n5.Not equal to\n")
	ch=int(input("Enter Choice\n"))
	if ch==1:
		obj1<obj2
	elif ch==2:
		obj1>obj2
	elif ch==3:
		obj1<=obj2
	elif ch==4:
		obj1>=obj2
	elif ch==5:
		obj1!=obj2
