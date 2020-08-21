class Node:
	def __init__(self,data=None,prev=None,next=None):
		self.data=data
		self.prev=prev
		self.next=next



class DoublyLinkedList:
	def __init__(self):
		self.header = Node()
		self.trailer= Node()
		# creating sentinels
		self.header.next = self.trailer
		self.trailer.prev = self.header
		self.size = 0


	def __len__(self):
		return self.size


	def is_empty(self):
		return self.size==0

	def insert_between(self,data, prev, next):
		newNode = Node(data,prev,next)
		prev.next=newNode
		next.prev=newNode
		self.size+=1

	def display(self):
		print('Traversal in forrward Direction: ')
		temp = self.header
		while(temp):
			print(temp.data)
			last = temp
			temp=temp.next

		print('Traversal in Backward Direction: ')
		while(last):
			print(last.data)
			last = last.prev
dlist = DoublyLinkedList()
print('operations:')
q = int(input('enter the choice: '))
while(q!=0):
	if q==1:
		a= int(input())
		# here function will act as inserting at last
		dlist.insert_between(a,dlist.trailer.prev,dlist.trailer)
	if q==3:
		a=int(input())
		# here function will act as inserting at start
		dlist.insert_between(a, dlist.header, dlist.header.next)

	if q==2:
		dlist.display()
	q = int(input('enter the choice: '))




