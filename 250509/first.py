# # 튜플 복습
# a = (1, 10, 1, 2, 3)
# b = a[2:5]  # (1,2,3)
# c = a[1]
# c = a.count(1)  # 2
# d = a.index(1)  # 0

# # set 자료구조
# a = {1, 2, 3, 1}
# print(a) # {1, 2, 3}
# print(len(a)) # 3

# 형변환 list -> set
# a = [1,1,1,2,2,3]
# b = set(a)
# print(b)
# c = list(b)

# a = {1, 2, 3}
# print(a[0])  # set은 인덱싱 기능x TypeError: 'set' object is not subscriptable

# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# # print(f"합집합: {set1|set2}")
# # print(f"합집합: {set1|set2}")
# # print(f"차집합: {set1-set2}")
# # print(f"차집합: {set2-set1}")
# # print(f"차집합: {set2-set2}")
# print(f"대칭 차집합: {set1.symmetric_difference(set2)}")
# print(f"set1이 set2의 부분집합인가? {set1.issubset(set2)}")

# d = {"a", 1, 2, 3, 1, "a"}
# print(d)
# e = list(d)
# print(e)

# set 수정
# fruits = {'apple','banana','cherry'}
# fruits.add('orange')
# fruits.add('melon')
# print(fruits)
# fruits.remove('apple')
# print(fruits)
# fruits.remove('apple') # KeyError: 'apple'
