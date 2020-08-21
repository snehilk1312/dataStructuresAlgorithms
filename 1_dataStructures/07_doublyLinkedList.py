import gc

class Node:
	def __init__(self, data=None, prev=None, next=None):
		self.data=data
		self.prev=prev
		self.next=next


class DoublyLinkedList:
	def __init__(self, head=None):
		self.head = head


	def addFront(self, data=None):
		newNode = Node(data)
		if self.head==None:
			self.head=newNode
		else:
			self.head.prev = newNode
			newNode.next = self.head
			self.head = newNode


	def display(self):
		print('Traversal in forrward Direction: ')
		temp = self.head
		while(temp):
			print(temp.data)
			last = temp
			temp=temp.next

		print('Traversal in Backward Direction: ')
		while(last):
			print(last.data)
			last = last.prev


	def addAfter(self, data, x):
		newNode = Node(data)
		newNode.next = x.next
		newNode.prev = x
		temp = x.next
		x.next = newNode
		if temp!=None:
			temp.prev = newNode


	def addBefore(self,data,x):
		newNode = Node(data)
		newNode.next=x
		newNode.prev =x.prev
		temp = x.prev
		x.prev = newNode
		if temp!=None:
			temp.next = newNode


	def addEnd(self,data):
		newNode = Node(data)
		temp=self.head
		if self.head==None:
			self.head=newNode
			return
		while(temp.next):
			temp =temp.next
		temp.next=newNode
		newNode.prev = temp


	def delNode(self, x):
		if x==self.head:
			self.head = x.next


		if  x.next!=None:
			x.next.prev = x.prev

		if x.prev!=None:
			x.prev.next = x.next
		# calling to free memory of those objects having 0 reference
		gc.collect()

dlist = DoublyLinkedList()
print('operations:')

q = int(input('enter the choice: '))
while(q!=0):
	if q==1:
		a= int(input())
		dlist.addFront(a)

	if q==2:
		dlist.display()

	if q==3:
		dlist.addAfter(int(input()),dlist.head.next.next)

	if q==4:
		dlist.addBefore(int(input()),dlist.head.next)

	if q==5:
		dlist.addEnd(int(input()))
	q = int(input('enter the choice: '))


dlist.delNode(dlist.head)
dlist.delNode(dlist.head.next)
dlist.delNode(dlist.head.next)
dlist.display()
