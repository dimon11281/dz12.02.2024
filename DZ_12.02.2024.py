class DbList:
    class Node:
        element = None
        nextNode = None
        prevNode = None

        def __init__(self, element, nextNode = None, prevNode = None):
            self.element = element
            self.nextNode = nextNode
            self.previous_node = prevNode

    head = None
    tail = None
    lengthNode = 0

    def addNode(self, element):
        self.lengthNode += 1
        if self.head is None:
            self.head = self.Node(element)
            return element
        elif self.tail is None:
            self.tail = self.Node(element, None, self.head)
            self.head.nextNode = self.tail
            return element
        else:
            self.tail = self.Node(element, None, self.tail)
            self.tail.previous_node.nextNode = self.tail
            return element

    def delNode(self, index, reverse = False):
        if index == 0:
            el = self.head.element
            self.head = self.head.nextNode
            self.head.prevNode = None
            return el
        elif index == self.lengthNode-1:
            el = self.tail.element
            self.tail = self.tail.prevNode
            self.tail.nextNode = None
            return el
        elif reverse:
            i = self.lengthNode - 1
            node = self.tail
            while i != index:
                node = node.prevNode
                i -= 1
            el = node.element
            node.prevNode.nextNode, node.nextNode.prevNode = node.nextNode, node.prevNode
            del node
            return el
        else:
            i = 0
            node = self.head
            while i != index:
                node = node.prevNode
                i += 1
            el = node.element
            node.prevNode.nextNode, node.nextNode.prevNode = node.nextNode, node.prevNode
            del node
            return el


    def deleteNode(self, index):
        if self.head:
            if index > self.lengthNode // 2:
                el = self.delNode(index, reverse=True)
                return el
            else:
                el = self.delNode(index, reverse=False)
                return el

    def __iter__(self):
        node = self.head

        while node:
            yield node.element
            node = node.nextNode


dbList = DbList()
h1 = dbList.addNode(8)
h2 = dbList.addNode(91)
h3 = dbList.addNode(0)
h4 = dbList.addNode(3)
h5 = dbList.addNode(7)

h6 = dbList.deleteNode(3)
#
for e in dbList:
    print(e)










