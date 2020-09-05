# Circular Queue
class Queue:
    def __init__(self, size=10):
        self.front = -1
        self.rear = -1
        self.arr = [None]*size
        self.maxsize = size

    def isFull(self):
        return ((self.rear+1) % self.maxsize) == self.front % self.maxsize

    def isEmpty(self):
        return (self.front == -1) and (self.rear == -1)

    def enqueue(self, data):
        if self.isFull():
            print("Queue is Full !")
            return
        if self.isEmpty():
            # incrementing front and rear by 1
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1
        self.arr[self.rear % self.maxsize] = data

    def dequeue(self):
        if self.isEmpty():
            return "Nothing in queue!"
        temp = self.arr[self.front % self.maxsize]
        self.front += 1
        if self.front > self.rear:
            # print(self.front, self.rear)
            self.front = -1
            self.rear = -1
            return self.isEmpty()
        return temp

    def showIndex(self):
        print(f"\nFront:{self.front}\nRear:{self.rear}")

    def display(self):
        if self.isEmpty():
            print("Empty")
            return
        for i in range(self.front, self.rear+1):
            print(self.arr[i % self.maxsize], end='\t')
        print('\n')

    def peek(self):
        return self.arr[self.front]


myqueue = Queue()
print("\nfor enqueue press 1:\nfor dequeue press 2:\nto display queue press 3:\nis empty press 4:"
      "\nis full press 5:\nto peek at front press 6:\nto show index press 7:\nto quit press 0: ")

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
        print(myqueue.isFull())

    if op == 6:
        print(myqueue.peek())

    if op == 7:
        myqueue.showIndex()
    op = int(input("Enter the operation to be performed: \n"))

print("Program Finished")


