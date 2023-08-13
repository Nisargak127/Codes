from tkinter import *
from tkinter import ttk
import validators
import mechanicalsoup
import pandas as pd



root=Tk()
root.title('OOP Assignment 2022 - 2023')

root.config(bg="skyblue")

root.minsize(1700,1000)
root.maxsize(1700,1000)




l1=Label(text="WEB SCRAPPING",font=("arial",22,"bold"),bg="skyblue").place(x=750,y=200)

l2=Label(text="ENTER AN URL: ",font=("arial",17,"bold"),bg="skyblue").place(x=350,y=350)

in1=Entry(width=50)
in1.place(x=650,y=350)

def destroy():
    root.destroy()


def extract():


    url=in1.get()
# create browser object & open URL


    browser = mechanicalsoup.StatefulBrowser()

    v=validators.url(url)
    if(v==True):
        l1=Label(text="Valid URL ",font=("arial",17,"bold"),bg="skyblue").place(x=820,y=480)
    else:
        l1=Label(text="INVALID URL ",font=("arial",17,"bold"),bg="skyblue").place(x=820,y=480) 



    browser.open(url)



   

# extract table data (the rest of the table)
    td = browser.page.find_all("td")


# tidy up and slice off non-table elements
    columns = [value.text.replace("\n", "") for value in td]
    columns = columns[0:75]
    print(columns)
#print(columns)
    column_names = ["Census year" , "Persons",'Absolute','Percentage',"Males","Females"]

    census=[]
    persons=[]
    absolute=[]
    percentage=[]
    male=[]
    female=[]
    

    for i in range(len(columns)):
        if(i==0 or i==6 or i==12  or i==18 or i==24 or i==30 or i==36 or i==42 or i==48 or i==54 or i==60 or i==66 ) :
            census.append(columns[i])


    for i in range(len(columns)):
        if(i==1 or i==7 or i==13  or i==19 or i==25 or i==31 or i==37 or i==43 or i==49 or i==55 or i==61 or i==67 ):
            persons.append(columns[i])

    for i in range(len(columns)):
        if(i==2 or i==8 or i==14  or i==20 or i==26 or i==32 or i==38 or i==44 or i==50 or i==56 or i==62 or i==68 ):
            absolute.append(columns[i])

    for i in range(len(columns)):
        if(i==3 or i==9 or i==15  or i==21 or i==27 or i==33 or i==39 or i==45 or i==51 or i==57 or i==63 or i==69 ):
            percentage.append(columns[i])

    for i in range(len(columns)):
        if(i==4 or i==10 or i==16  or i==22 or i==28 or i==34 or i==40 or i==46 or i==52 or i==58 or i==64 or i==70):
            male.append(columns[i])


    dict1={'Census':census,'Persons':persons,'Absolute':absolute,'Percentage':percentage,'Male':male,'Female':female}
    df = pd.DataFrame(data = dict1)
    df.to_csv('meghalaya.csv', encoding='utf-8', index=False)
    

    tree=ttk.Treeview(root,height=12)
    tree['columns']=("Census","Persons","Absolute","Percentage","Male","Female")

    tree.column("Census",width=50,minwidth=150)
    tree.column("Persons",anchor=W,width=150)
    tree.column("Absolute",anchor=W,width=150)
    tree.column("Percentage",anchor=W,width=150)
    tree.column("Male",anchor=W,width=150)
    tree.column("Female",anchor=W,width=200)
    

    tree.heading("Census",text="Census Year",anchor=W)
    tree.heading("Persons", text="Persons", anchor=W)
    tree.heading("Absolute", text="Absolute", anchor=W)
    tree.heading("Percentage", text="Percentage", anchor=W)
    tree.heading("Male", text="Male", anchor=W)
    tree.heading("Female", text="Female", anchor=W)
    

    
    

    for i in range(len(census)):
        tree.insert(parent='',index='end',iid=i,text=i+1,values=(census[i],persons[i],absolute[i],percentage[i],male[i],female[i]))
    
    tree.place(x=450, y=580)




b1=Button(text="Submit", bg="black",fg="white",command=extract,padx=60,pady=10).place(x=680,y=400)

b2=Button(text="Close", bg="black",fg="white",command=destroy,padx=60,pady=10).place(x=880,y=400)


root.mainloop()
