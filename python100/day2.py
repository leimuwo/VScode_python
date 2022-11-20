# # 第一个作业
# # 提示：华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$。
# F = int(input("请输入华氏温度"))
# C = (F-32)/1.8
# #  .1f表示保留一位小数的浮点型数
# print("华氏温度是%.1f，摄氏温度是%.1f"%(F,C))

# # 第二个作业
# # 输入圆的半径得到圆的周长和面积
# radius = float(input("请输入圆的半径"))
# preimeter = 2*3.1416*radius 
# area = radius**2*3.1416
# print("半径为%.1f的圆周长为%.1f " % (radius,preimeter))
# print("半径为%.1f的圆面积为%.1f " % (radius,area))

# 练习三： 输入年份判断是不是闰年

year = int(input('请输入年份'))

is_laep = year %4 == 0 

print(is_laep)                                      