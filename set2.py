while(True):
	print("====Menu====")
	print("\n1.list\n2.set\n3.exit\n")
	mainch=int(input("Enter your choice"))
	if(mainch==1):
		while(True):
			print("====Menu====")
			print("\n1.length\n2.membership\n3.count\n4.reverse\n5.repeat\n6.insert\n7.append\n8.pop\n9.remove\n10.sort\n11.exit")
			ch1=int(input("Enter your choice"))
			l=[]
			n=int(input("Enter your range"))
			for i in range(n):
				l.append(int(input()))
			print(l)
			if(ch1==1):
				print(f"The length is {len(l)}")
			elif(ch1==2):
				i=int(input("Enter element"))
				if(i in l):
					print(f"Yes {i} present in {l}")
				else:
					print(f"No {i} is not present in {l}")
			elif(ch1==3):
				ele=int(input("Enter your range"))
				l3=l.count(ele)
				print(f"The count of {ele} is {l3}")
			elif(ch1==4):
				r=l[::-1]
				print(f"The reversen of {l} is {r}")
			elif(ch1==5):
				n=int(input("How many times"))
				l2=l*n
				print(f"The {l} repeated {n} times is {l2}")
			elif(ch1==6):
				pos=int(input("enter position"))
				ele=int(input("enter element"))
				l.insert(pos,ele)
				print(f"After inserting {ele} we get {l}")
			elif(ch1==7):
				ele=int(input("enter element"))
				l.append(ele)
				print(f"After inserting {ele} we get {l}")
			elif(ch1==8):
				p=l.pop()
				print(f"After poping {p} we get {l}")
			elif(ch1==9):
				ele=int(input("enter element to remove"))
				l.remove(ele)
				print(f"After removing {ele} we get {l}")
			elif(ch1==10):
				l.sort()
				print(f"After sorting we get {l}")
			elif(ch1==11):
				break
			else:
				print("Enter valid Choice")
	elif(mainch==2):
		while(True):
			print("====Menu====")
			print("\n1.length\n2.updating whole set\n3.membership\n4.add\n5.remove\n6.union\n7.intersection\n8.difference\n9.issubset\n10.isdisjoint\n11.exit\n")
			ch1=int(input("Enter your choice"))
			s = {2,3,5,6}
			print(s)
			if(ch1==1):
	                       print(f"The length is {len(s)}")
			elif(ch1==2):
				s3=s.update([1,0,9,4,5])
				print("The concatenation is ", s3)
			elif(ch1==3):
				i=int(input("Enter element"))
				if(i in s):
					print(f"Yes {i} present in {s}")
				else:
					print(f"No {i} is not present in {s}")
			elif(ch1==4):
				ele=int(input("enter element"))
				s.add(ele)
				print(f"After adding {ele} we get {s}")
			elif(ch1==5):
				ele=int(input("enter element to remove"))
				s.remove(ele)
				print(f"After removing {ele} we get {s}")
			elif(ch1==6):
				s2={0,3,4,5}
				print(s2)
				print(f"The union is {s.union(s2)}")
			elif(ch1==7):
				s2={5,6,7,8}
				print(s2)
				print(f"The intersection is {s.intersection(s2)}")
			elif(ch1==8):
				s2={2,3,9,0}
				print(s2)
				print(f"The difference of set1-set2 is {s-s2}")
			elif(ch1==9):
				s2={2,3,4,5,6}
				if(s.issubset(s2)):
					print("Yes subset")
				else:
					print("No not a subset")
			elif(ch1==10):
				s2={1000,2000,3000,4000}
				print(s2)
				if(s.isdisjoint(s2)):
					print("Yes disjoint")
				else:
					print("No not disjoint")
			elif(ch1==11):
				break
			else:
				print("Enter valid Choice")
	elif(mainch==3):
		break
	else:
		print("Enter valid choice")
