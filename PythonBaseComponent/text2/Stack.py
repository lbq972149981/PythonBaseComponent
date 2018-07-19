from inspect import stack
from mailcap import show
class myStack:
    def __init__(self, size=10):
        self._content = []
        self._size = size
        self._current = 0

    def empty(self):
        self._content = []
        self._current = 0

    def isEmpty(self):
        if not self._current:
            return True
        else:
            return False

    def setSize(self, size):
        if size<self._current:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def isFull(self):
        if self._current == self._size:
            return True
        else:
            return False

    def push(self, v):
        if len(self._content) < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print('Stack Full!')

    def pop(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop()
        else:
            print('Stack empty!')

    def show(self):
        print(self._content)

    def showRemainderSpace(self):
        print('Stack can still push ', self._size-self._current, 'elements.')

if __name__ == '__main__':
    print('Please use me as a module.')
    stack = myStack(10)
    for i in range(1,6):
        stack.push(i)
    stack.show()
    stack.showRemainderSpace();
    for i in range(0,4):
        stack.pop()
    print(stack.isEmpty())
    stack.show();
    stack.pop()
    print(stack.isEmpty())