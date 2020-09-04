# class to create node
class Node:
    def __init__(self, value=None, next=None):
        self.data = value
        self.next = next


# Implementation of stack using Linked List
class Stack:
    def __init__(self, top=None):
        self.head = top
        self.count = 0

    def push(self, value):
        newNode = Node(value)
        temp = self.head
        self.head = newNode
        self.head.next = temp
        self.count += 1

    def pop_(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.count -= 1

    def top_(self):
        return self.head.data

    def isEmpty(self):
        return self.count == 0


mystack = Stack()
expression = input('Enter the expression: ')

for i in range(len(expression)):
    if (expression[i] == '(') or (expression[i] == '{') or (expression[i] == '['):
        mystack.push(expression[i])

    if (expression[i] == ')') or (expression[i] == '}') or (expression[i] == ']'):
        if mystack.isEmpty():
            print("Not balanced parenthesis")
            exit()
        if (expression[i] == ')' and mystack.top_()!='(') or (expression[i] == '}' and mystack.top_()!='{') or (expression[i] == ']' and mystack.top_()!='[') :
            print("not balanced parenthesis")
            exit()
        mystack.pop_()

if mystack.isEmpty():
    print("Yes, the parenthesis are balanced")

if not mystack.isEmpty():
    print("Unbalanced Parenthesis")

print("Program Ended")
