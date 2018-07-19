class myQueue:
    def __init__(self, size=10):
        self._content = []
        self._size = size
        self._current = 0

    def setSize(self, size):
        if size < self._current:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def put(self, v):
        if self._current<self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print('The queue is full!')

    def get(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop(0)
        else:
            print('The queue is empty!')

    def show(self):
        if self._content:
            print(self._content)
        else:
            print('The queue is empty!')

    def empty(self):
        self._content = []

    def isEmpty(self):
        if not self._content:
            return True
        else:
            return False

    def isFull(self):
        if self._current == self._size:
            return True
        else:
            return False


if __name__ == '__main__':
    Que = myQueue(10)
    for i in range(5):
        Que.put(i)
    Que.show()
    print( Que.isEmpty())
    print( Que.isFull())
    Que.put('hello')
    Que.show()
    print(Que.get())
    Que.show()
    Que.setSize(4)
    Que.show();
    Que.setSize(9)
    Que.show()