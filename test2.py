"""
 * Project name(项目名称)：Python函数式编程
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/26 
 * Time(创建时间)： 15:02
 * Version(版本): 1.0
 * Description(描述)： 
 """


def f1(list):
    new_list = []
    for item in list:
        new_list.append(item * 2)
    return new_list


if __name__ == '__main__':
    list1 = [1, 2, 3, 4]
    print(f1(list1))
    print(f1(list1))
    print(f1(list1))
    print(f1(list1))
    print(f1(list1))
