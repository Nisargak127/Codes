d=dict()
class employee():
        def input(self):
                self.name=input("Enter the name of the Employee\n")
                self.address=input("Enter the address of the employee\n")
                self.pan=input("Enter the Pan number of the employee\n")
                self.bs=int(input("Enter the basic salary of the employee\n"))
                self.tds=int(input("Enter the tds of the employee\n"))
                self.phra=int(input("Enter HRA %\n"))
                self.pda=int(input("Enter DA %\n"))
                self.hra=(self.bs*self.phra)/100
                self.da=(self.bs*self.pda)/100
                self.tax=int(input("Enter tax %\n"))
                self.pf=int(input("Enter PF amount\n"))
                self.lic=int(input("Enter the lic amount\n"))
                self.hl=int(input("Enter the house loan amount\n"))
                self.gross=self.bs+self.hra+self.da
                self.deduct=((self.gross*self.tax)/100)+self.pf+self.lic+self.hl
                self.net=self.gross-self.deduct
                self.update()
        def update(self):
                d.update({self.name:{
                                "Name":self.name,
                                "Address":self.address,
                                "Pan":self.pan,
                                "Basic Salary":self.bs,
                                "TDS":self.tds,
                                "HRA":self.hra,
                                "DA":self.da,
                                "Gross Salary":self.gross,
                                "Deductions":self.deduct,
                                "Net Salary":self.net
                        }})
        def search(self,name):
                flag=0
                for key in d:
                        if key==name:
                                print("Employee Found")
                                print(key,d[key])
                                flag=1
                if flag==0:
                        print("Employee not found")
        def printemp(self):
                for key in d:
                        print(key,d[key])
class emplyoee1(employee):
        em=employee()
        while True:
                ch=int(input("1.Enter the Employee Details\n2.Search For the Employee\n3.Display all Employees\n"))
                if ch==1:
                        em.input()
                elif  ch==2:
                        name=input("Enter the name to be searched\n")
                        em.search(name)
                elif ch==3:
                        em.printemp()
                else:
                        print("Thank you")
