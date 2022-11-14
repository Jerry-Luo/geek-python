import unittest


class Testing(unittest.TestCase):
    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)


# 命令行执行 python3 -m unittest -v testing.py 看效果
if __name__ == '__main__':
    unittest.main()
