class Node:
	def __init__(self, data=None, next=None):
		self.data=data
		self.next=next


class LinkedList:
	def __init__(self, head=None):
		self.head=head


	def addNode(self, value):
		newNode = Node(value)
		try:
			last=self.head
			while(last.next):
				last = last.next
			last.next = newNode

		except:
			self.head=newNode


	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp=temp.next

def printElement(x):
	if x==None:
		return
	print(x.data)
	printElement(x.next)


def printElementReverse(x):
	if x==None:
		return
	printElementReverse(x.next)
	print(x.data)



llist = LinkedList()
print('operations:\n1.add a node\n2.print linked list\n3.elements get listed\n4.elements get printed in reverse\n0.quit\n')

q = int(input('enter your choice of operation:'))

while(q!=0):
	if q==1:
		value = int(input('enter the node value: '))
		llist.addNode(value)


	if q==2:
		llist.printList()


	if q==3:
		printElement(llist.head)

	if q==4:
		printElementReverse(llist.head)


	q = int(input("enter your choice of operations:"))

print('PROGRAM FINISHED')
