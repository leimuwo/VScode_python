# s1 = 'hello,world'
# s2 = "hello,world"
# 三引号可以换行输出
# s3 = """
# hello,
# world!
# """
# print(s1,s2,s3,end="")


# 转义
# a = ord('旺')
# b = ord('仔')
# c = chr(26106)
# d = chr(20180)
# s1 = '\'hello,world\''
# s2 = c+d
# print(s1,s2)

# # r解除转义
# s1 = r'\'hello,world\''
# s2 = r'\n\hello,world!\\\n'
# print(s1,s2,end='')

'''字符串的运算处理'''
# # 字符串的*和+运算
# s1 = '旺仔'*3
# s2 = '我是'+'旺仔'
# s3 = 'abc123456'
# print(s1,s2)

# # 判断某字符串时候在另外一个字符串中,返回True或False
# print(s1 in s2)

# # 取出特定位置的字符,从0开始
# print(s1[0])

# # 字符串切片
# print(s3[3:]) # 123456
# print(s3[:3]) # abc
# print(s3[:-3]) # abc123
# print(s3[::2])# ac246 间隔为2
# print(s3[1:6:2]) # b13
# print(s3[::-3]) # 63c 反向+间隔为3


'''通过方法来完成对字符串的处理'''
# str1 = 'hello, world!'
# # 内置len()函数
# print(len(str1)) #13

# # 获得字符串首字母大写的拷贝
# print(str1.capitalize()) # Hello, world!

# # 获得每个单词首字母大写的拷贝
# print(str1.title()) # Hello, World!

# # 获得字符串大写后的拷贝
# print(str1.upper()) # HELLO, WORLD!

# # 从字符串查找字串的位置
# print(str1.find('or')) # 8
# print(str1.find('shit')) # -1字符串没有返回-1

# # 也是查找，但会找不到会返回异常
# # print(str1.index('or'))
# # print(str1.index('shit'))

# # 检查字符串是否以指定的字符串开头
# print(str1.startswith('He')) #False
# print(str1.startswith('hell')) # True

# # 检查字符串时候以指定的字符串结尾
# print(str1.endswith('ld!')) # True

# # 检查字符串以指定的宽度居中并在两边填充指定的字符
# print(str1.center(50, '*'))

# # 将字符串以指定的长度靠右放置左侧填充指定的字符
# print(str1.rjust(50, '*'))

# str2 = 'abc123456'
# # 检查字符串是否有数字构成
# print(str2.isdigit()) # False

# # 检查字符串时候由字母构成
# print(str2.isalpha()) # False

# # 检查字符串是否以数字和字母构成
# print(str2.isalnum()) # True

# str3 = '      abc      '
# # 获得减去两侧空格的拷贝
# print(str3.strip())


# '''格式化输出'''
# # c风格
# a,b = 5,10
# print('%d * %d = %d'%(a, b, a*b))

# # 字符串提供的方法
# print('{0} * {1} = {2}'.format(a, b, a*b))
# # 更简化的方法
# print(f'{a} * {b} = {a*b}')


# 练习一： 在屏幕上设计跑马灯文字




from random import randint
import os
import time

def main():
    content = '北京欢迎你为你开天劈地……'
    while True:
        os.system('cls')
        print(content)
        # 休息0.2s
        time.sleep(0.2)
        content = content[1:] + content[0]


# 练习二：随机生成含有数字和字母的验证码


def generate_code(code_len=4):

    all_chars = "1234567890qwertyuiopasdfghjklzxcvbnm"
    last_pos = len(all_chars) - 1
    code = ''
    for _ in range(code_len):
        index = randint(0, last_pos)
        code += all_chars[index]
    return code

# 练习三：设计一个函数返回给定文件名的后缀名


def get_suffix(filename, has_dot=False):
    pos = filename.rfind('.')
    # 考虑如果只有一个点的情况
    if(has_dot is True):
        return filename[pos:]
    else:
        return filename[pos+1:]

# 练习四：设计一个函数返回传入列表中最大的和第二大的元素的值


def max2(x):
    """
    
    """
    if(x[0] > x[1]):
        m1, m2 = x[0], x[1]
    else:
        m1, m2 = x[1], x[0]
    for index in enumerate(x):
        if(x[index] > m1):
            m2 = m1
            m1 = x[index]
        elif(x[index] > m2):
            m2 = x[index]
        return m1, m2

# 练习无：计算指定的年月日是这一年的第几天


def is_leap_year(year):
    """
    lainx
    """
    if year % 4 == 0:
        return True
    else:
        return False


def which_day(year, month, date):
    """
    d
    """
    days_of_month = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 12],
                     [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 12]]
    if(is_leap_year(year) is True):
        for i in range(0, month-1):
            date += days_of_month[1][i]
        return date
    else:
        for i in range(0, month-1):
            date += days_of_month[0][i]
        return date


def triangle():
    """
    sow
    """
    num = int(input("Number of rows:"))
    a = []
    for i in range(0, num):
        a.append([])
        # print(i)
        for j in range(0, i+1):
            # print(j,end =' ')
            if j == 0 or j == i:
                a[i].append(1)
            else:
                a[i].append(a[i-1][j-1]+a[i-1][j])
    print(a)


if __name__ == '__main__':
    # main()
    # print(generate_code())
    # print(get_suffix("."))
    # a = []
    # for i in range(10):
    #     a.append(randint(1,10))
    # print(max2(a))
    # print(which_day(2004,12,20))
    triangle()
