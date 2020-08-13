class Node:
	def __init__(self,value=None,next_node=None):
		self.value = value
		self.next_node = next_node


class LinkedList:
	def __init__(self, head=None):
		self.head = head

	def printList(self):
		temp = self.head
		while(temp!=None):
			print(temp.value)
			temp = temp.next_node


	def node_at_beg(self,value):
		new_node = Node(value)
		new_node.next_node = self.head
		self.head = new_node


	def node_at_mid(self, value, pos):
		new_node = Node(value)
		count = 0
		last = self.head
		while(count<pos-1):
			last = last.next_node
			count+=1
		temp = last.next_node
		last.next_node = new_node
		new_node.next_node=temp

	def node_at_end(self,value):
		new_node = Node(value)

		if self.head==None:
			self.head = new_node
			return

		last = self.head
		while(last.next_node!=None):
			last = last.next_node
		last.next_node = new_node

	def delete_at_pos(self,pos):
		if pos==0:
			self.head=self.head.next_node
			return
		count=0
		last = self.head
		while(count<pos-1):
			last=last.next_node
			count+=1
		temp = last.next_node
		count1 = 0
		last1 = self.head
		while(count1<pos):
			last1 = last1.next_node
			count1+=1
		temp1 = last1.next_node
		# print(last.value,temp.value,last1.value,temp1.value)
		last.next_node = temp1


	def delete_first_occurence(self,value):
		last=self.head
		count = 0
		while(last.value!=value and last.next_node!=None):
			last = last.next_node
			count+=1
		self.delete_at_pos(count)


	def length_ll(self):
		try:

			last = self.head
			count=0
			while(last.next_node):
				last = last.next_node
				count+=1
			print(count+1)
		except:
			print(0)
print('initializing a linked list object')
llist = LinkedList()

print('1:insert_at_beg\n2:insert at end\n3:node at mid\n4:print list\n5:delete at pos\n6:delete 1st occ\n7:lenth of ll\n0:to quit')
operation = int(input('enter the key for operation:'))

while(operation!=0):
	if operation==1:
		a = int(input('enter the value:'))
		llist.node_at_beg(a)
	if operation==2:
		a = int(input('enter the value:'))
		llist.node_at_end(a)
	if operation==3:
		a = int(input('enter the value:'))
		pos = int(input('enter the pos:'))
		llist.node_at_mid(a,pos)
	if operation==4:
		llist.printList()
	if operation==5:
		a = int(input('enter the value:'))
		llist.delete_at_pos(a)
	if operation==6:
		a = int(input('enter the value:'))
		llist.delete_first_occurence(a)
	if operation==7:
		llist.length_ll()
	operation = int(input('again enter key:'))

llist.printList()

