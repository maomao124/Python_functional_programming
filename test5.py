"""
 * Project name(项目名称)：Python函数式编程
 * Package(包名): 
 * File(文件名): test5
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 15:12
 * Version(版本): 1.0
 * Description(描述)： Python reduce()函数
reduce() 函数通常用来对一个集合做一些累积操作
reduce(function, iterable)
其中，function 规定必须是一个包含 2 个参数的函数；iterable 表示可迭代对象。
 """
import functools

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    product = functools.reduce(lambda x, y: x * y, list1)
    print(product)
    product = functools.reduce(lambda x, y: x + y, list1)
    print(product)
    product = functools.reduce(lambda x, y: x - y, list1)
    print(product)
    product = functools.reduce(lambda x, y: x / y, list1)
    print(product)
