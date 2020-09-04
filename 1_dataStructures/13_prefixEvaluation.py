class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top
        self.count = 0
    def push(self, value):
        newNode = Node(value)
        temp = self.top
        self.top = newNode
        self.top.next = temp
        self.count += 1

    def pop_(self):
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.count -= 1
        return temp.data

    def isEmpty(self):
        return self.count==0


mystack = Stack()
expression = input("Enter the prefix expression with space as delimiter: ")
expression = expression.split(' ')
expression = expression[::-1]    # added this to postfix evaluation
for i in range(len(expression)):
    try:
        temp = float(expression[i])
        mystack.push(expression[i])
    except ValueError:
        operator = expression[i]
        operand2 = mystack.pop_()
        operand1 = mystack.pop_()
        result = eval(f'{operand2}{operator}{operand1}')  # here we have changed wrt postfix evaluation
        mystack.push(result)
print(mystack.pop_())
