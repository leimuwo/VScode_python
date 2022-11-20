from math import sqrt
# 求最小公倍数，最大公约数

# 子最大公约数
def gcd(num1,num2):
    if(num1>num2):
        temp = num1
        num1 = num2
        num2 = temp
    while(num1<=num2):
        temp = num2 % num1
        num2 = num1
        num1 = temp
        if(temp==0):
            return num2

# 最小公倍数
def lcm(x,y):
    return x*y // gcd(x,y)  

# 判断回文数
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total *10 + temp %10
        temp //= 10
    return total == num

# 练习三：判断是不是素数
def is_prime(num):
    for i in range(2,int(sqrt(num))):
        if num % i ==0:
            return False
    return True if num !=1 else False

if __name__ == '__main__':
    num = int(input("请输入正整整："))
    if is_palindrome(num) and is_prime(num):
        print("%d是回文素数"%num)
           
    