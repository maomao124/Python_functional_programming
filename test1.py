"""
 * Project name(项目名称)：Python函数式编程
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 15:00
 * Version(版本): 1.0
 * Description(描述)：
 所谓函数式编程，是指代码中每一块都是不可变的，都由纯函数的形式组成。这里的纯函数，是指函数本身相互独立、互不影响，对于相同的输入，总会有相同的输出。
除此之外，函数式编程还具有一个特点，即允许把函数本身作为参数传入另一个函数，还允许返回一个函数。
 """


def f1(list):
    for index in range(0, len(list)):
        list[index] *= 2
    return list


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print(f1(list1))
    print(f1(list1))
    print(f1(list1))
    print(f1(list1))
    print(f1(list1))
