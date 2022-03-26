"""
 * Project name(项目名称)：Python函数式编程
 * Package(包名): 
 * File(文件名): test4
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 15:09
 * Version(版本): 1.0
 * Description(描述)： Python filter()函数
filter()函数
filter(function, iterable)
此格式中，funcition 参数表示要传入一个函数，iterable 表示一个可迭代对象。
filter() 函数的功能是对 iterable 中的每个元素，都使用 function 函数判断，并返回 True 或者 False，
最后将返回 True 的元素组成一个新的可遍历的集合。
 """

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6]
    new_list = filter(lambda x: x % 2 == 0, list1)
    print(list(new_list))

    new_list = map(lambda x, y: x - y > 0, [3, 5, 6], [1, 5, 8])
    print(list(new_list))
