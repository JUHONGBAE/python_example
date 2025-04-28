
# 정수
a = 10
b = 20
c = 0
d = -40
print(type(a), type(b), type(c),type(d))
print(int(9.3333))
# 실수
number1 = 3.12
nubmer2 = -0.12
print(type(number1), type(nubmer2))
print(float(3))
## 무한대
x = float("inf")
y = float("-inf")

# 문자열
str1 = "abcd"
str2 = 'abcd'

str3 = '''
오늘은 4월 28일 입니다.

5월이 멀지 않았네요.

'''
str4 = '오늘은 4월 28일 입니다. \n\n5월이 멀지 않았네요.'
print((type(str3)))
print(str3)
print(str4)

# 문자열 이어붙이기

str6 = "modu"
str7 = "labs"

print(str6+str7)
str8 = str7+str6
print(str8)

# 개인정보 추력해보기
## 1. 성, 이름 변수를 따로 만들어서 + 로 합친 후 출력
## 2. 주민등록번호도 1번과 같이
## 3. 이메일 {아이디} {@} {메일}

str11 = "BAE"
str12 = "JUHONG"

str13 = "123456"
str14 = "7894561"

str15 = "qwer"
str16 = "asdf.com"
print(str11+str12)
print(str13+"-"+str14)
print(str15+"@"+str16)

str10 = str1 * 10

test2 = "30"

print(str10)

# print(str1 * test2) (x)
print(str10+"입니다" + "어쩌고 저쩌고")
# 오늘은 4월 28일 입니다.
a = "4"
b = "28"

# 기본방식
print("오늘은 "+a+"월 "+b+"일입니다.")
# f-string
# f""
print(f"오늘은 {a}월 {b}일 입니다.")

#문자열 인덱싱

s = "life is good"
print(s[0])
print(s[3])

# print(s[300]) IndexError: string index out of range
## 주민등록번호가 13자리
## print(s[13])

# 문자열 슬라이싱 [start:stop:step]

print(s[0:3]) #s[0:3:1]
print(s[0:4:2])

s = 'weniv CEO licat'
print(1, s[0:5]) # 출력 : weniv
print(2, s[6:]) # 출력 : CEO licat
print(3, s[:]) # 출력 : weniv CEO licat
print(4, s[::-1]) # 출력 : tacil OEC vinew
print(5, s[::2]) # 출력 : wnvCOlct

# 테스트
##ip address = 172.100.200.100
'''
1. ip address 문자열을 슬라이싱 기법을 활용해 변수에 담아 출력
2. a,b,c,d 라는 변수에 슬라이싱 기법을 통해 .을 기준으로 각각 담는다.
3. f-string을 사용해서 172100200100 문자 나오게 하기
'''

s = "ip address = 172.100.200.100"
print("1.", s[0:10])

a = s[13:16]
b = s[17:20]
c = s[21:24]
d = s[25:]
print("2.", a,b,c,d )

print(f"3. ip address = {a},{b},{c},{d}")