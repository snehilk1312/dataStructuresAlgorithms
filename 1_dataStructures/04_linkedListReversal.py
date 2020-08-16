class Node:
	# initializes a node
	def __init__(self, data=None, next=None):
		self.data = data
		self.next = next


class LinkedList:
	# initializes Linked List
	def __init__(self, head=None):
		self.head = head

	# prints the LinkedList
	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data)
			temp = temp.next

	# add nodes at beginning
	def addNode(self, data):
		newNode = Node(data)
		temp = self.head
		newNode.next = temp
		self.head = newNode


	# reverses the linked list
	def reverse(self):
		current = self.head
		prev = None
		while(current!=None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev


llist = LinkedList()
print('operations:\n1.add a node\n2.print linked list\n3.reverse the linked list\n0.quit\n')

q = int(input('enter your choice of operation:'))

while(q!=0):
	if q==1:
		value = int(input('enter the node value: '))
		llist.addNode(value)


	if q==2:
		llist.printList()


	if q==3:
		llist.reverse()


	q = int(input("enter your choice of operations:"))

print('PROGRAM FINISHED')
