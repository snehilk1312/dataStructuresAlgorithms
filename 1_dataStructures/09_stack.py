class stack:
	def __init__(self, maxsize):
		self.top=-1
		self.myStack=[None]*maxsize
		self.max = maxsize

	def insert(self, data):
		if self.top+1==self.max:
			print('stack overflow !')
			return
		self.top+=1
		self.myStack[self.top] = data


	def display(self):
		for i in range(0, self.top+1):
			print(self.myStack[i])


	def pop_(self):
		if self.top==-1:
			print('Stack is Empty.')
			return
		self.top-=1

	def top_(self):
		print(self.myStack[self.top])

	def length(self):
		print(self.top+1)

maxsize = int(input('enter the maxsize of stack: '))
a = stack(maxsize)
# print(a.myStack)
q = int(input('Enter the operation to be performed: '))

while(q!=0):
	if q==1:
		n = int(input('Enter the element to be inserted:'))
		a.insert(n)

	if q==2:
		a.display()


	if q==3:
		a.pop_()

	if q==4:
		a.top_()


	if q==5:
		a.length()

	q = int(input('enter the operation to be performed: '))


print('operation  terminated')
# print(a.myStack)
