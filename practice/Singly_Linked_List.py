# 연결 리스트(Linked List) --> 데이터를 동적으로 추가 및 삭제할 때 유용한 자료 구조.
# 숫자 데이터를 저장하는 단일 연결 리스트 만들기

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# 연결 리스트 생성
my_linked_list = LinkedList()

# 데이터 추가
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

# 연결 리스트 출력
my_linked_list.display()
