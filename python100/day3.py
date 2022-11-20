# # 练习一：英尺和厘米转换单位
# value = float(input("请输入长度；"))

# unit = input("请输入单位: ")

# if unit == "cm" or unit == "厘米":
#     print("%f英尺 = %f厘米 " % (value , value * 2.54))
# elif unit =='inch' or unit == "英尺":
#     print("%f厘米 = %f英尺 " % (value , value / 2.54))
# else:
#     print("不好意思，输入单位有误")

# # 练习二： 百分制成绩转换为等级制成绩
# score = float(input('请输入成绩： '))
# # 90以上输出A， 80-90输出B, 70-80分输出C, 60-70分输出D, 60分以下输出E
# if score >= 90 and score <=100:
#     print("A")
# elif score >= 80 and score < 90:
#     print("B")
# elif score >= 70 and score <80:
#     print("C")
# elif score >= 60 and score <70:
#     print("D")
# elif score <60 and score >= 0:
#     print("E")
# else: 
#     print('成绩输入错误')

# 练习三： 输入三条边长，如果构成三角形就计算周长和面积：
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        perimeter = lambda a,b,c:  a+b+c
        p = (a+b+c)/2
        print("三角形周长为%f "%perimeter)
        area = (p*(p - a)(p - b)(p - c)) ** 0.5
        print("三角形的面积为%f "%area)
    else:
        print("不能构成三角形")
else :
    print("边输入错误")