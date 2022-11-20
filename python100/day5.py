# # 水仙花数：每个位上的数字的立方和为数字本身,三位数
# l = []

# for a in range(1,10):
#     for b in range(10):
#         for c in range(10):
#             num = a*100+b*10+c
#             if num == a**3 + b**3 +c**3:
#                 print(num)

"""tips:正整数的反转"""

# num = int(input('num = '))
# reversed_num = 0
# while num > 0:
#     reversed_num = reversed_num * 10 + num % 10
#     num //=10
# print(reversed_num) 

# # 百鸡百钱

# for i in range(20):
#     for j in range(33):
#         z = 100-i-j
#         if 5 * i + 3 * j + z/3 == 100:
#             print("公鸡： %d只, 母鸡: %d只, 小鸡：%d只"%(i,j,z))


# # 花旗骰

# from random import randint

# num = randint(2,12)
# i = 1

# if(num == 7 or num ==11):
#     print("骰子数为%d第一轮玩家胜利！"%num)
# elif(num == 2 or num == 3 or num ==12):
#     print("骰子数为%d第一轮庄家胜利！"%num)
# else:
#     while(i!=0):
#         sec = randint(2,12)
#         i+=1
#         if sec == 7:
#             print("第%d轮骰子数为%d,庄家胜！ "%(i,num))
#             i = 0
#         elif sec == num:
#             print("第%d轮骰子数为%d,玩家胜! "%(i,num))
#             i = 0
        

# # 练习1：生成斐波那契数列的前20个数

# num1 = 1
# num2 = 2
# temp = 0
# for i in range(3,21):
#     temp = num1 + num2
#     print("第%d个斐波那契数为%d"%(i,temp))
#     num1 = num2
#     num2 = temp 

# # 练习2：完美数，所有的真因子的和恰等于其本身
# from math import sqrt


# for num in range(2,10000):
#     sum = 0
#     for i in range(1,num):
#         if (num % i == 0):
#             sum +=i
#     if(sum == num):
#         print("%d是完美数"%num)      

# 输出100以内的素数

from math import sqrt


for num in range(2,100):
    sum = 0
    for i in range(2,num):
        if(num  % i == 0):
           sum+=1
    if(sum == 0):
        print("%d是质数"%num)
     
