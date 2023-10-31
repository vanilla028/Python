
# 스택(Stack)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "스택이 비어 있습니다."

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "스택이 비어 있습니다."

# 스택 객체 생성
stack = Stack()

# 데이터 추가
stack.push(1)
stack.push(2)
stack.push(3)

# 데이터 꺼내기
print(stack.pop())  # 3
print(stack.pop())  # 2
print(stack.pop())  # 1


# 큐(Queue)
from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return "큐가 비어 있습니다."

# 큐 객체 생성
queue = Queue()

# 데이터 추가
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

# 데이터 꺼내기
print(queue.dequeue())  # 1
print(queue.dequeue())  # 2
print(queue.dequeue())  # 3
