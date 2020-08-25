class Node:
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


class Stack:
	def __init__(self, top=None):
		self.top = top


	def push(self, data):
		newNode = Node(data)
		newNode.next = self.top
		self.top=newNode


	def pop_(self):
		temp =self.top
		self.top = self.top.next
		temp.next = None


	def display(self):
		temp = self.top
		while(temp):
			print(temp.data)
			temp=temp.next


	def top_(self):
		print(self.top.data)


myStack = Stack()

q = int(input('enter the operation to be performed: '))
while(q!=0):
	if q==1:
		myStack.push(int(input('enter the element to be pushed: ')))

	if q==2:
		myStack.pop_()

	if q==3:
		myStack.top_()
	if q==4:
		myStack.display()

	q = int(input('enter the operation to be performed: '))


print('program terminated ! ')
