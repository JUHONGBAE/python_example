# insert
# a = [1, 2, 3, 4, 5]

# # insert(인덱스, 값)
# a.insert(0, 0)
# print(a)
# # 0,1,2,3,4,5

# # pop() 제일 끝에 있는 값 추출
# # 리스트 값이 비어있으면 IndexError: pop from empty lise
# b = a.pop()
# print(a)
# print(b)
# # 미연에 방지하려면
# if len(a) >= 1:  # 리스트 내부의 데이터 갯수가 1개 이상이라면?
#     a.pop()  # 추출
# else:
#     print("리스트가 비어있습니다.")

# # remove(값)
# c = [1, 2, 3, 1, 1]
# c.remove(1)
# print(c) # [2, 3, 1, 1]
# c.remove(1)
# print(c) # [2, 3, 1]
# c.remove(50)
# print(c) # ValueError: list.remove(x): x not in list

# 기존에 데이터가 있는 리스트를 만든다.
# insert를 활용해서 데이터를 넣는다.
# pop을 사용하여 꺼낸 데이터를 출력한다. pop(3): 3번째 위치 값 삭제
# remove를 사용하여 특정 데이터를 제거해본다. remove(3): 데이터 3값 삭제

"""python
w = [60.5, 75.2, 89, 100.0]
print(w)
w.insert(3, 95.7)
print(w)
w.pop()
print(w)
w.remove(60.5)
print(w)
"""

# a = [1, 2, 3, 4, 5]
# a.reverse() # [5, 4, 3, 2, 1]
# print(a)
# b=a.append(1)
# print(a) # [5, 4, 3, 2, 1, 1]
# print(b) # None 행위는 하는데 결과값 반영x  '-> None' 표시뜸

# a = [1, 2, 3, 4, 5]
# print(reversed(a)) # <list_reverseiterator object at 0x0000015B4CDDAD40>
# print(list(reversed(a)))
# print(a)

# a = [1, 2, 3, 4, 5]
# b = list(reversed(a))
# print(a)
# print(b)

# a = [5, 4, 3, 2, 1]
# # a.sort() 원본데이터 자체를 변경
# b = list(sorted(a))
# print(a)
# print(b)

# c = [1, 2, 3, 4, 5]
# # sorted(리스트, reversed=bool)
# sorted(c, reverse=False) # sorted(a)
# d = list(sorted(c, reverse=True)) # 내림차순 정렬
# print(d)

#1
print("1번")
books = []
books.append("파이썬 기초")
books.append("데이터 과학 입문")
books.append("알고리즘의 이해")
books.append("머신러닝 실전")
books.append("파이썬 기초")
print(books,"\n")

#2
print("2번")
print(books.count("파이썬 기초"))
books.append("웹 개발의 시작")
books.insert(2,"데이터베이스 설계")
new_books = []
new_books.append("인공지능 개론")
new_books.append("클라우드 컴퓨팅")
books.extend(new_books)
print(books,"\n")

#3
print("3번")
books.remove("파이썬 기초")
last_book=books.pop()
print(last_book)
books.sort()
books.reverse()
print(books,"\n")

#4
print("4번")
top_books = books[0:3] # books[:3]
reversed_selection = list(reversed(books[1:5])) #books[1:5][::-1]
print(top_books)
print(reversed_selection)
books.clear()
print(books)