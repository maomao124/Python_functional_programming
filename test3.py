"""
 * Project name(项目名称)：Python函数式编程
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 15:03
 * Version(版本): 1.0
 * Description(描述)： Python map()函数
 map(function, iterable)
其中，function 参数表示要传入一个函数，其可以是内置函数、自定义函数或者 lambda 匿名函数；iterable 表示一个或多个可迭代对象，可以是列表、字符串等。
map() 函数的功能是对可迭代对象中的每个元素，都调用指定的函数，并返回一个 map 对象。
 """

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    new_list = map(lambda x: x * 2, list1)
    print(list(new_list))
    print(list(new_list))
    print(list(new_list))

    list2 = [1, 2, 3, 4, 5]
    list3 = [3, 4, 5, 6, 7]
    print(list2)
    print(list3)
    new_list = map(lambda x, y: x + y, list2, list3)
    print(list(new_list))
