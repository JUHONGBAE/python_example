# c = [1, "2", "good", 4, [1, 2, 3, [123, "good"],31],2]
# # 1. good이라는 문자열을 인덱싱 기법으로 추출
# # 2. 슬라이싱 기법을 통해 [123,"good"] 을 추출

# print(c[2], c[4][3][1])
# print(c[4][3][0:2])

# li = []
# li.append(1)
# li.append(2)
# li.append([1,2,3])
# li.append([12])
# print(li)
# li[2].append("good")
# print(li)

# # 데이터 삭제 (리스트 안에 있는 데이터만 삭제)
# li.clear()
# print(li)

# b = [1,2,3]
# c = b
# # c.append(123)
# # print(b)
# c = b.copy()
# c.append(2)
# print(b)
# print(c)
# c.clear()
# print(c)

"""
빈리스트를 만든다.
append를 사용하여 이중 리스트를 만든다.
출력한다.
리스트의 데이터를 다 지운다.
출력한다.
copy를 활용한다.
카피를 활용한 리스트에 append를 사용하여 출력한다.
"""

# a = []
# a.append(1)
# a.append([1,2])
# print(a)
# a.clear()
# print(a)
# b=a.copy()
# b.append("hi")
# print(b)

# count
# a = [1, 2, 3, "okay", 1, 1, 1]
# print(a.count(1))  # 4

# b = [1, 2, 3, [1, 2, 3, 1]]
# print(b.count(1))  # 1
# # 3이 나오게 하려면?
# print(b[3].count(1))
# sum = b.count(1) + b[3].count(1)
# print(sum)

# 자동정렬: shift + alt + f

# extend
# a = [1, 2, 3, 4]
# b = [5, 6, 7, 8]
# # [1,2,3,4,5,6,7,8]
# a.extend(b)
# print(a)
# c = "good"
# b.extend(c)
# print(b)

# a = ["good", "okay"]
# b = a.index("good")
# print(b)

c = "h, a, b, c"
d = c.find("a")
print(d)