while True:
    print("Menu")
    print("1. List Operations\n2. Set operations")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        l=list(input("Enter elements:").split())
        while True:
            print("Menu")
            print("1.Reverse\n2.Sort\n3.Decreasing order\n4.Append\n5.Extend\n6.Exit")
            ch=int(input("Enter your choice:"))
            if(ch==1):
                print("List is",l)
                l.reverse()
                print("Reversed list:",l)
            elif(ch==2):
                print("List is",l)
                l.sort()
                print("sorted list:",l)
            elif(ch==3):
                print("List is",l)
                l.sort(reverse=True)
                print("Decreasing order of the list:",l)
            elif(ch==4):
                print("List is",l)
                i=input("Enter element to append:")
                l.append(i)
                print("List after appending:",l)
            elif(ch==5):
                print("List is",l)
                l2=list(input("Enter elements to extend the list").split())
                l.extend(l2)
                print("List after extending:",l)
            elif(ch==6):
                break
            else:
                print("Invalid choice")
    elif(ch==2):

        while True:
            print("Menu")
            print("1.Issuperset\n2.Disjoint\n3.Convert set to list\n4.Issubset\n5.Frozenset\n6.Exit")
            ch=int(input("Enter your choice:"))
            if(ch==1):
                s1=set(input("Enter elements of the set").split())
                s2=set(input("Enter elements of the set").split())
                s1.issuperset(s2)
                print(s1)
            elif(ch==2):
                s1=set(input("Enter elements of the set").split())
                s2=set(input("Enter elements of the set").split())
                s1.isdisjoint(s2)
                print(s1)
            elif(ch==3):
                s1=set(input("Enter elements of the set").split())
                my_list = list(s1)
                print(my_list)
            elif(ch==4):
                s1=set(input("Enter elements of the set").split())
                s2=set(input("Enter elements of the set").split())
                s2.issubset(s1)
                print(s2)
            elif(ch==5):
                s1=set(input("Enter elements of the set").split())
                my_frozenset = frozenset(s1)
            elif(ch==6):
                break
            else:
                print("Invalid choice")
    elif(ch==3):
        break
    else:
        print("Invalid choice")
