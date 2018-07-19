import stack
import unittest
class TestStack(unittest.TestCase):
    def setUp(self):
        self.fp = open('D:\\test_Stack_result.txt', 'a+')

    def tearDown(self):
        self.fp.close()

    def test_isEmpty(self):
        try:
            s = stack.Stack()
            # 确保函数返回结果为True
            self.assertTrue(s.isEmpty())
            self.fp.write('isEmpty passed\n')
        except Exception as e:
            self.fp.write('isEmpty failed\n')

    def test_empty(self):
        try:
            s = stack.Stack(5)
            for i in ['a', 'b', 'c']:
                s.push(i)
            # 测试清空栈操作是否工作正常
            s.empty()
            self.assertTrue(s.isEmpty())
            self.fp.write('empty passed\n')
        except Exception as e:
            self.fp.write('empty failed\n')

    def test_isFull(self):
        try:
            s = stack.Stack(3)
            s.push(1)
            s.push(2)
            s.push(3)
            self.assertTrue(s.isFull())
            self.fp.write('isFull passed\n')
        except Exception as e:
            self.fp.write('isFull failed\n')

    def test_pushpop(self):
        try:
            s = stack.Stack()
            s.push(3)
            # 确保入栈后立刻出栈得到原来的元素
            self.assertEqual(s.pop(), 3)
            s.push('a')
            self.assertEqual(s.pop(), 'a')
            self.fp.write('push and pop passed\n')
        except Exception as e:
            self.fp.write('push or pop failed\n')

    def test_setSize(self):
        try:
            s = stack.Stack(8)
            for i in range(8):
                s.push(i)
            self.assertTrue(s.isFull())
            # 测试扩大栈空间是否正常工作
            s.setSize(9)
            s.push(8)
            self.assertTrue(s.isFull())
            self.assertEqual(s.pop(), 8)
            # 测试缩小栈空间是否正常工作
            s.setSize(4)
            self.assertTrue(s.isFull())
            self.assertEqual(s.pop(), 3)
            self.fp.write('setSize passed\n')
        except Exception as e:
            self.fp.write('setSize failed\n')