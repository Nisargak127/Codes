while True:
    print("Menu")
    print("1. String Operations\n2. Tuple operation")
    ch=int(input("Enter your choice:"))
    if(ch==1):
        while True:
            
            print("Menu")
            print("1.Replace\n2.Swapcase\n3.Capitalize\n4.Title\n5.Startswith\n6.Exit")
            ch=int(input("Enter your choice:"))
            if(ch==1):
                try:
                    str=input("Enter string:")
                    i=input("Enter element to be relaced:")
                    r=input("Enter element:")
                    result=str.replace(i,r)
                    print("String after replacing",result)
                except:
                    print("Substring doesnt exist")
            elif(ch==2):
                str=input("Enter string:")
                print("String is:",str)
                r=str.swapcase()
                print("After swapping case",r)
            elif(ch==3):
                str=input("Enter string:")
                print("String is:",str)
                r=str.capitalize()
                print("After capitalizing",r)
            elif(ch==4):
                 str=input("Enter string:")
                 print("String is:",str)
                 r=str.title()
                 print("After title",r)
            elif(ch==5):
                 str=input("Enter string:")
                 print("String is:",str)
                 i=input("Enter element to check if it startd with")
                 r=str.startswith(i)
                 print(r)
            elif(ch==6):
                break
            else:
                break
    elif(ch==2):
        t=tuple(input("Enter tuple elements:").split())
        
        while True:
            print("Menu")
            print("1.Reversing a tuple\n2.Sorting a tuple\n3.Conversion from a list\n4.Conversion to a list\n5.Tuple Unpacking\n6.Exit")
            ch=int(input("Enter your choice"))
            if(ch==1):
                print("Tuple is: ",t)
                reversed_t = reversed(t)
                print(tuple(reversed_t)) 
            elif(ch==2):
                print("Tuple is: ",t)
                s = sorted(t)
                print("Sorted tuple",tuple(s))
            elif(ch==3):
                l=list(input("Enter the list:"))
                print("List is:",l)
                t=tuple(l)
                print("Converted list into tuple is:",t)
            elif(ch==4):
                print("Tuple is",t)
                l=list(t)
                print("Tuple converted to list is:",l)
            elif(ch==5):
                t = (1, 2, 3)
                a, b, c = t
                print(a, b, c)
            elif(ch==6):
                break
            else:
                print("Invalid choice")
    elif(ch==3):
        break
    else:
        print("Invalid choice")
