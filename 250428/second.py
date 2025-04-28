# 입력 구현
# 파이썬에서 input은 숫자를 입력해도 무조건 문자


'''
입력을 몇 가지 변수에 담아서
f-string, 문자붙이기, 문자반복하기 등 여러 기술을 활용해 출력하세요.
'''

'''
a = input("아무거나 입력해주세요: ")
b = f"f-string {a}"
c = a + a
d = a * 3

print(f"{a}는 한글입니다.")
print(c)
print(d)

## 형변환
print(type(a))
b = int(a) #문자를 숫자로
print(type(b))
'''

'''
a = input()
print(type(int(a)))
print(a)'''

# # 문자열 고유 기능
# s = 'weniv CEO licat'
# print(s.lower())
# print(s.upper())

# print(s.find("good"))
# # print(s.index("good")) #ValueError: substring not found

# print(s.find("weniv"))
# print(s.find("licat"))

# print(s.index("weniv"))
# print(s.index("licat"))

# print(s.count("i"))

# s2 = s.replace("CEO","CTO")
# print(s2)

# s3 = "weniv-corp"
# s4,s5 = s3.split("-")
# print(s4,s5)

'''
입력이 들어온다. 키 몸무게 성별 나이 이름
예시 180 60 남 25 김아무개
이것을 공백을 기준으로 쪼개어 각 변수에 담아 출력한다.
이름을 f-string을 통해 세 번 반복해서 출력한다.
'''

# a = input("키 몸무게 성별 나이 이름을 입력하세요: ")
# s1,s2,s3,s4,s5 = a.split()
# print("키:",s1)
# print("몸무게:",s2)
# print("성별:",s3)
# print("나이:",s4)
# print("이름:",s5)

# print(f"{s5} " * 3)

# s20 = ["modu","labs","good"]
# print("-".join(s20))

# name = 'licat'
# age = 29

# print('제 이름은 {}이고, 나이는 {}살입니다.'.format(name, age))
# print(f"제 이름은 {name}이고, 나이는 {age}살입니다.")

# print("Hello\nWorld!") # Hello와 World! 사이에 줄바꿈이 일어납니다.
# print("Hello\tWorld!") # Hello와 World! 사이에 탭 간격이 생깁니다.
# print("She said, \"Hello World!\"") # 큰따옴표 내부에 문자열을 출력합니다.
# print('She said, \'Hello World!\'') # 작은따옴표 내부에 문자열을 출력합니다.
# print("Backslash: \\") # 백슬래시를 출력합니다.

# bool 타입
# a = 10 > 3
# b = True
# c = False
# print(type(a))
# print(a)

## 형변환
# a = 1
# b = 0
# c = -1
# d = "okay"
# e = ""

# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(d))
# print(bool(e))

# print(a==b)

# x = None

# result = 5 + 3
# print(result)

# result = 3 + 2.5
# print(result)

# print(11/2)
# print(10/2)
# print(type(10/2))
# print(11//2)

print(10**5) # 제곱

 