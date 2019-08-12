import unittest
import function
from unittest.mock import patch


class MyTestCase(unittest.TestCase):
    """
    @patch("function.multiply")
    patch 装饰/上下文管理器可以很容易模拟类或对象在模块测试
    测试过程中指定的对象将被替换为一个模拟（或者其他对象），并在测试结束时还原
    这里模拟function.py文件中multiply()函数
    def test_add_and_multiply2(self,mock_multiply):
    定义测试用例中，将mock的multiply()函数（对象)重命名为mock_multiply对象
    """
    @patch("function.multiply")
    # 这个是装饰器，其作用了解下
    def test_add_and_multiply2(self,mock_multiply):
        x = 3
        y = 5
        # 比test_func多一行
        # 设定mock_multiply对象的返回值为固定的15
        mock_multiply.return_value = 15
        addition,multiple = function.add_and_multiply(x,y)
        # 检查mock_multiply方法的参数是否正确
        mock_multiply.assert_called_once_with(3,5)

        self.assertEqual(8,addition)
        self.assertEqual(15,multiple)


if __name__ == "__main__":
    unittest.main()
