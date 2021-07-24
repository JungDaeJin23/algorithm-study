class Node:
    def __init__(self, data, n=None):
        self.data = data
        self.next = n


def crateLinkedQueue():
    global front, rear
    front = rear = None


def Qpeek():
    global front
    return front.data


def printQ():
    global front
    f = front
    s = ""
    while f:
        s += f.item + " "
        f = f.next
    return s


def isEmpty():
    global front
    return front is None


def enQueue(data):
    global front, rear
    new_node = Node(data)
    if isEmpty():
        front = new_node
    else:
        rear.next = new_node
    rear = new_node


def deQueue():
    global front, rear
    if isEmpty():
        return None
    data = front.data
    front = front.next
    # ** why is this needed? **
    # 없어도 동작은 같음 하지만 명확히 하기 위해서 rear 또한 None으로 지정한다.
    if isEmpty():
        rear = None
    return data