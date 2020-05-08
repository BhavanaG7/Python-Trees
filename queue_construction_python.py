from collections import deque
class Queue(object):
    def __init__(self):
        self.queue=deque()

    def enqueue(self,value):
        self.queue.appendleft(value)

    def deque(self):
        if self.queue:
            return self.queue.pop()
    def __str__(self):
        if len(self.queue)>0:
            s="queue content :\n"
            s+="\n".join([str(i) for i in self.queue])
            return s
        else:
            return "Empty queue"

q=Queue()
q.enqueue("apple")
q.enqueue("banana")
q.enqueue("cherry")
print(q)

print("===================================")
print("DElete")
print(q.deque())#apple
print(q.deque())
print(q.deque())