# a = 10
# b = 21

# if a> 10:
#     print("Good")
# elif b == 20:
#     print("20입니다.")
# elif a == 10:
#     print("10입니다.")
# else:
#     print("이도저도")

'''
split() 활용

a,b 변수를 활용,
키,몸무게를 입력받는다.

키와 몸무게를 나눈 나머지를 출력한다.

조건문을 활용해서

키(a)가 130 이상이면 a, 150이상이면 b, 170 이상이면 c 180 이상면이면 d를 출력하세요요 
'''



# info = input("키, 몸무게 입력: ")
# a,b = info.split()
# a = float(a)
# b = float(b)
# a ,b = map(float, input("키, 몸무게 입력: ").split()) <- map 사용법

# print(f"키/몸무게 나머지 값: {a%b}")

# if a >= 180:
#     print("d")
# elif a >= 170:
#     print("c")
# elif a >= 150:
#     print("b")
# elif a >= 130:
#     print("a")

# score = input("시험점수: ")
# score = int(score)
# if 90 <= score <= 100:
#     print("A")
# elif 80<= score <= 89:
#     print("B")
# elif 70<= score <= 79:
#     print("C")
# elif 60<= score <= 69:
#     print("D")
# else:
#     print("F")

## and, or 연산활용
# a = 10
# b = 20
# if a == 10 and b == 20:
#     print("Good")
# else:
#     print("no")

'''
a,b,c 를 입력받는다.
a가 100이고 b가 200이상이면 "a"를 출력
b가 1이면 "b"를 출력
이도저도 아니면 c를 출력
'''
# a,b,c = input("숫자 입력: ").split()
# a,b,c = int(a),int(b),int(c)
# if a == 100 and b >= 200:
#     print("a")
# elif b == 1:
#     print("b")
# else:
#     print("이도저도 c")

# a,b,c = input("주사위 눈: ").split()
# a,b,c = int(a), int(b), int(c)
# if a == b== c:
#     print(10000 + a *1000)
# elif a==b or a==c:
#     print(1000 + a * 100)
# elif b==c:
#     print(1000 + b * 100)
# else:
#     print(max(a,b,c)*100)

# # 최대값 코드
# temp = 0
# if a > temp:
#     temp = a
# if b > temp:
#     temp = b
# if c > temp:
#     temp = c
# price = temp * 100

# a = "Good"
# b = "a" in a
# print(b)
# print(len(a))

# x = [1, 2, 3] #CSV 파일과 비슷 ,
# y = ['apple', 'banana', 'cherry']
# z = [1, [2], 3] in [2]

# test = 2 in [[2], 3, [4, 5], [[6, [7]]]]
# print(test)

# test1 = [2] in [[2], [4, 5], [[6, [7]]]]
# print(test1)

# test2 = [[6,[7]]] in [[4, 5], [[6, [7]]]]
# print(test2)

# t = [[2], 3, [4, 5], [[6, [7]]]]
# print(len(t))

# t2 = [1,2,3,[4,5,[2,31]],1]
# print(t2[3][2][0])
# # print(t2[1000])

# # 수정
# t2[0] = 5
# print(t2)

# t3 = [5, 4, 3, [2, 1]] # [1,2,3,[4,5]] 순서로 변경
# t3[0] = 1
# t3[1] = 2
# t3[3][0] = 4
# t3[3][1] = 5
# print(t3)

# t4 = [3]
# t4.append(1)
# print(t4)
# t4.append(2) # append는 리스트 뒤에 붙인다.
# print(t4)
# t4.clear() # 리스트 안 데이터 삭제
# t4.remove(3) # 리스트 안 3값을 지움

# t4 = [5, 4, 3, 2, 1] # 오름차순 정렬
# t4.sort()
# print(t4)

# # 리스트 만들때 방법
# a = []
# b = list()

# t4.pop()