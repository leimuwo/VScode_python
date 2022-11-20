# def main():
#     f = None
#     try:
#         f = open("book.txt","w", encoding ='utf-8')
#     except FileNotFoundError:
#         print('无法打开指定的文件！')
#     except LookupError:
#         print('指定了未知的编码！')
#     except UnicodeDecodeError:
#         print("读取文件时解码错误！")
#     finally:
#         if f:
#             f.close()

# if __name__ == "__main__":
#     main()

# import time 

# def main():
#     # 一次性读取整个文件内容
#     with open("book.txt", 'r', encoding='utf-8') as f:
#         print(f.read())

#     # 通过for_in循环逐行读取
#     with open("C:\\VScode_python\\python100\\book.txt", 'r', encoding='utf-8') as f:
#         for line in f:
#             print(line, end= '')
#             time.sleep(0.5)
#     print()

#     # 读取文件按行读取到列表中
#     with open("C:\\VScode_python\\python100\\book.txt", 'r', encoding='utf-8') as f:
#         lines = f.readlines()
#     print(lines)
#     # 输出结果是以列表的形式，按行输出而且会包括换行符

# if __name__ == "__main__":
#     main()

from math import sqrt

def is_prime(num):
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True if num != 1 else False

def round(num):
    if num >= 1 and num <= 99:
        name = 'a.txt'
        write_in(num, name)
    elif num >=100 and num <= 999:
        name = 'b.txt'
        write_in(num, name)
    elif num >1000 and num <= 9999:
        name = 'c.txt '
        write_in(num, name)


def write_in(num, name):
    with open('%s' % name , 'w', encoding='utf-8') as f:
        f.write('%d'%num)

if __name__ == "__main__":
    for num in range(1,10000):
        if is_prime(num):
            round(num)
        