class Dunder:
	def __init__(self):
		self.l=[]

	def accept(self,other):
		n=int(input("Enter length\n"))
		for i in range(0,n):
			self.l.append(int(input("Enter list 1 numbers:")))
		for i in range(0,n):
			other.l.append(int(input("Enter list 2 numbers:")))
		print("list 1 ",self.l)
		print("list 2 ",other.l)
	def __lt__(self,other):
		for i in range(0,len(other.l)):
			print(self.l[i]<other.l[i])
			
	def __gt__(self,other):
		for i in range(0,len(other.l)):
			print(self.l[i]>other.l[i])
			
	def __le__(self,other):
		for i in range(0,len(other.l)):
			print(self.l[i]<=other.l[i])
			
	def __ge__(self,other):
		for i in range(0,len(other.l)):
			print(self.l[i]>=other.l[i])
			
	def __ne__(self,other):
		for i in range(0,len(other.l)):
			print(self.l[i]!=other.l[i])
