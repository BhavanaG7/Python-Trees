class Stack():
    def __init__(self):
        self.list=list()

    def push(self,value):
        self.list.append(value)

    def pop(self):
        if self.list:
            self.list.pop()

    def len(self):
        return len(self.list)

    def is_empty(self):
        return len(self.list)==0

    def top(self):
        if len(self.list)>0:
            return self.list[-1]
        else:
            return None

    def __repr__(self):
        if len(self.list)>0:
            s="\n".join([str(i) for i in self.list[::-1]])
            return s
        else:
            return "Empty List"

print("Stack Construction :")

stack=Stack()

print("is_empty")
print(stack.is_empty())
print("---------------------------------------")
print("top if empty:",stack.top())
print("---------------------------------------")
print("len of stack :",stack.len())
print("---------------------------------------")
print("Content of stack:")
print(stack)

stack.push("A")
stack.push("B")
stack.push("C")
stack.push("D")

print("---------------------------------------")
print("After Adding elements :")
print("is_empty")
print(stack.is_empty())
print("---------------------------------------")
print("top if empty:",stack.top())
print("---------------------------------------")
print("len of stack :",stack.len())

print("---------------------------------------")
print("Content of stack:")
print(stack)