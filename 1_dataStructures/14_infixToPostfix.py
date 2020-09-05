# Without a Parenthesis in expression
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self, top=None):
        self.top = top
        self.count = 0

    def push(self, data):
        newNode = Node(data)
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

    def top_(self):
        return self.top.data

    def isEmpty(self):
        return self.count==0

    def remain(self):
        temp = self.top
        s = ''
        while temp:
            s += ' '
            s += temp.data
            temp = temp.next
        return s

mystack = Stack()
expression = input("Enter the Infix expression, delimited by space: ")
expression = expression.split(' ')
result = ''
def precedence(op):
    if op == '**':
        return 2
    elif (op == '*') or (op == '/'):
        return 1
    else:
        return 0


def comparePrecedence(a, b):
    return precedence(a) >= precedence(b)


for i in range(len(expression)):
    if (expression[i] != '+') and (expression[i] != '-') and (expression[i] != '*') and (expression[i] != '/') and (expression[i] != '**'):
        result += ' '
        result += expression[i]

    else:
        if mystack.isEmpty():
            mystack.push(expression[i])
        elif comparePrecedence(mystack.top_(),expression[i]):
            result += ' '
            result += mystack.pop_()
            while (mystack.isEmpty() == False) and (comparePrecedence(mystack.top_(),expression[i])) :
                result += ' '
                result += mystack.pop_()
            mystack.push(expression[i])
        elif not comparePrecedence(mystack.top_(),expression[i]):
            mystack.push(expression[i])


result += mystack.remain()
print(result)
