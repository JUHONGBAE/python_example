
# and 연산

## 다른 언어에서는 

# a && b
# a = True
# b = True
# c= a and b
# d = 10 > 5 and 10 < 5 # True and False
# e = 10 >= 10 or False
# print(e)
# f = False and True and True # 0 1 1 
# print(f)
# f2 = (False or True) and True
# print(f2)
# f3 = not (False or True) and True
# print(f3)

# a = 10
# b = 20
# c = a!=b #다르다 True
# d = not a!=b # False
# print(c,d)

# a = int(input())
# b = int(input())
# c = int(input())
# ### 항은 3개 이상 and, or는 마음대로 연결하여 결과 출력
# r = (a>=0 and b>0) or c!=0 and (a*b*c<0)
# print(r)

# a = 10
# a = a + 10 # == a+=10

# st = "modulabs is good"
# sta = "good" in st
# stb = "good" not in st
# print(sta, stb)

a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
d = a+b+c
e = d/3
print(f"합: {d}, 평균: {e:.3f})")