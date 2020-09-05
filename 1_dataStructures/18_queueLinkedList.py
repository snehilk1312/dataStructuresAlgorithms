class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def enqueue(self, data):
        newNode = Node(data)
        self.count += 1
        if self.front==None and self.rear==None:
            self.front = newNode
            self.rear = newNode
            return

        self.rear.next = newNode
        self.rear = newNode

    def dequeue(self):
        try:
            if self.count == 1:
                temp = self.front.data
                self.front = None
                self.rear = None
                self.count -= 1
                return temp
            temp = self.front
            self.front = self.front.next
            temp.next = None
            self.count -= 1
            return temp.data
        except AttributeError:
            return "Queue Empty! "

    def display(self):
        temp = self.front
        while temp:
            print(temp.data)
            temp = temp.next

    def isEmpty(self):
        return self.count == 0

    def peek(self):
        return self.front.data


myqueue = Queue()
print("\nfor enqueue press 1:\nfor dequeue press 2:\nto display queue press 3:\nis empty press 4:"
      "\nto peek at front press 5:\nto quit press 0: ")

op = int(input("Enter the operation to be performed: \n"))
while op != 0:
    if op == 1:
        data = int(input("Enter the value to be inserted: "))
        myqueue.enqueue(data)

    if op == 2:
        print(myqueue.dequeue())

    if op == 3:
        myqueue.display()

    if op == 4:
        print(myqueue.isEmpty())

    if op == 5:
        print(myqueue.peek())

    op = int(input("Enter the operation to be performed: \n"))

print("Program Finished")



