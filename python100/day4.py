# # 练习1: 输入一个整数判断是不是素数
# from math import sqrt # 用啥import啥

# num = int(input("请输入整数："))
# end = int(sqrt(num))
# is_prime = True
# '''没有考虑num = 1的情况'''
# # for x in range(2,end+1):
# #     if(num%x==0):
# #         print('%d不是素数'%num)
# #         break
    
# #     if (x==end):
# #         print("%d是素数"%num)

# for x in range(2,end+1):
#     if(num%x==0):
#         is_prime = False
#         break
# if is_prime and num !=1:
#     print("%d是素数" % num)
# else:
#     print('%d不是素数' % num)

# # 练习2: 输入两个正整数，计算他们的最大公约数和最小公倍数

# x = int(input('x = '))
# y = int(input('y = '))

# a = x
# b = y

# common_divisor = 0
# common_multiple = 0

# if(x < y):
#     while(x!=0):
#         temp = y % x 
#         y = x
#         if (temp==0):
#             common_divisor = x
#         x = temp       
# elif(y < x):
#     while(y!=0):
#         temp = x % y 
#         x = y
#         if (temp==0):
#             common_divisor = y
#         y = temp
        
# else:
#     common_divisor = x

# common_multiple = a * b / common_divisor

# print("%d和%d之间的最大公约数为：%d "%(a,b,common_divisor))
# print("%d和%d之间的最小公倍数为：%d "%(a,b,common_multiple))

# 练习3：打印三角形图案
 
'''局限性：只能输出固定的行数'''
# for i in range(1,6):
#     x = '*'
#     print(i*x)

# for i in range(1,6):
#     x = '*'
#     print((5-i)*' '+i*x)

# for i in range(1,6):
#     x = '*'
#     print((5-i)*' '+(2*i-1)*x+(5-i)*' ')

row = int(input("请输入要输出的行数："))
for i in range(row+1):
    x = '*'
    print(i*x)

for i in range(row+1):
    x = '*'
    print((row-i)*' '+i*x)

for i in range(row+1):
    x = '*'
    print((row-i)*' '+(2*i-1)*x+(row-i)*' ')