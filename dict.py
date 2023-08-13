my_dict = {'name': 'John', 'age': 28, 'country': 'USA'}
print(my_dict)
while True:
    print("Menu")
    print("1.Add a new key-value pair\n2.Delete a key-value pair\n3.Checking if a key exist\n4.Getting all keys or values\n5.Clearing a dictionary\n6.Exit")
    ch=int(input("Enter your choice:"))
    if(ch==1):
       x=input("Enter the key:")
       y=input("Enter the value:")
       my_dict[x] = y 
       print("After adding a new key-value:",my_dict)
    elif(ch==2):
        try:
            k=input("Enter the key to delete")
            del my_dict[k]
            print(my_dict)
        except:
            print("The key doesn't exist")
    elif(ch==3):
        name=input("Enter key to check if it exist")
        if name in my_dict:
            print('The key exists in the dictionary')
        else:
            print("Key not found")
    elif(ch==4):
        keys = my_dict.keys()
        print("keys:",keys)
        values = my_dict.values()
        print("Values:",values)
    elif(ch==5):
        my_dict.clear()
        print("Dictionary:",my_dict)
    elif(ch==6):
        break
    else:
        print("Invalid choice")
