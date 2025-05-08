# 1번
# a = input("이름: ")
# print(f"안녕하세요,{a}!")

# 2번
# a = input("입력: ")
# print(a * 3)

# 3번
# a = int(input("출생연도: "))
# print(f"당신의 나이는 {2025-a}세입니다.")

# 4번
# r = int(input("반지름: "))
# p = 3.14
# print(f"반지름이 {r}인 원의 넓이: {p*r**2}")

# 5번
# v, t = input("속력 시간: ").split()
# v, t = int(v), int(t)
# s = v*t
# print(f"총 이동 거리: {s}")

# 6번
# a = input("첫번째 문장: ")
# b = input("두번째 문장: ")
# print(a+b)

# 7번
# a = float(input("인치 값: "))
# b = a*2.54
# print(f"{a}인치는 {b}센티미터입니다.")

# 8번
# a = float(input("식사 금액: "))
# b = float(input("팁 비율: "))
# c = a*(b/100)
# print(f"팁 금액: {c}원")
# print(f"총 지불 금액: {a+c}원")

# 9번
# a = float(input("키 입력: "))
# b = float(input("몸무게 입력: "))
# a = a/100
# c = b/(a**2)
# print(f"BMI: {c:.2f}")
# print(f"BMI: {round(c,2)}")


# 10번
# data = input("숫자(공백으로 입력): ").split()
# print(f"첫 번째 숫자: {data[0]}")
# print(f"마지막 숫자: {data[-1]}")

# 11번
# a = int(input())
# b = int(input())
# print(f"교환 전: a={a}, b={b}")
# a,b = b,a
# print(f"교환 후: a={a}, b={b}")

# 12번
# a = input("문자열 입력: ")
# print(f"문자열 길이: {len(a)}")
# print(f"첫 글자: {a[0]}")
# print(f"마지막 글자: {a[-1]}")

# 13번
# a, b = input("성과 이름(공백으로 구분): ").split()
# print(f"이니셜: {a[0].upper()}.{b[0].upper()}")

# 14번
# a = float(input("실수 입력: "))
# print(f"{a:.2f}")

# 15번
# a = int(input("나이 입력: "))
# if a >= 65:
#     print("노년")
# elif a >=35:
#     print("중장년")
# elif a >=19:
#     print("청년")
# else:
#     print("19세 미만")

# 16번 (인터넷 도움)
# text = input("문자열 입력: ")
# space = 0
# digit = 0
# char = 0
# for a in text:
#     if a == ' ':
#         space += 1
#     elif '0' <= a <= '9':
#         digit += 1
#     else:
#         char += 1
# print(f"공백 수: {space}")
# print(f"숫자 수: {digit}")
# print(f"문자 수: {char}")

# 17번
# a = (input("값 입력: "))
# b = bool(a)
# print(f"{a} -> {b}")

# 18번
# a = int(input("숫자 입력: "))
# if a % 2 ==0:
#     print(f"{a}은(는) 짝수")
# else:
#     print(f"{a}은(는) 홀수")

# 19번
# a,b,c,d = input("문자 입력: ").split()
# # print(a,b,c,d, sep=",")
# print(",".join([a,b,c,d])) -> 리스트로 묶어야함
# a = input("문자 입력: ").split()
# print(",".join(a))

# 20번
# a = float(input("온도: "))
# b = input("온도 단위(C,F만 입력): ")
# if b == "C":
#     print(f"{a}{b}는 {a*9/5+32}F입니다.")
# else:
#     print(f"{a}{b}는 {(a-32)*5/9}C입니다.")

# 21번
# a = input("문자열 입력: ")
# u = a.upper()
# l = a.lower()
# t = a.title()
# print(f"대문자: {u}")
# print(f"소문자: {l}")
# print(f"첫 글자만 대문자: {t}")

# 22번
# a = input("문자열 입력: ")
# f = a[0:3]
# l = a[-3:]
# r = a[::-1]
# print(f"앞 3글자: {f}")
# print(f"뒤 3글자: {l}")
# print(f"거꾸로: {r}")

# 23번
# a = input("문장 입력: ")
# b = input("찾을 단어: ")
# c = a.find(b)
# if c != -1:  # -> find() 함수 찾고자 하는게 없으면 -1 출력
#     print(f"단어 '{b}'의 위치: {c}")
# else:
#     print(f"단어 없음")

# 24번
# a = input("문장 입력: ")
# b = input("교체할 문자: ")
# c = input("새 문자: ")
# d = a.replace(b,c)
# print(d)

# 25번
# a = input("문장 입력: ")
# b = input("찾을 문자: ")
# c = a.count(b)
# print(f"문자 '{b}'의 출현 횟수: {c}")

# 26번
# a = input("이메일 입력: ")
# if "@" in a:
#     print("유효한 이메일 주소입니다.")
# else:
#     print("유효하지 않은 이메일 주소입니다.")

# 27번
# a = input("문자열 입력: ")
# b = int(input("길이 입력: "))
# if len(a) <= b:
#     print(a+"*"*(b-len(a)))
# else:
#     print(a)

# 28번
# a = input("문자열 입력: ")
# b = int((len(a)))
# if b % 2 == 1: 
#     print(f"중앙 문자: {a[b//2]}")    -> // 정수 나눗셈
# else:
#     print(f"중앙 문자: {a[b//2-1]},{a[b//2]}")

# 29번
# a = input("문자열 입력: ")
# a = a.replace(",","")
# a = a.replace("!","")
# a = a.replace("?","")
# print(a)

# 30번
# print("그녀가 말했다: \"안녕하세요!\"")
# print("이름\t나이\t직업")
# print("홍길동\t30\t개발자")
# print("안녕!\n반가워요!")

# 31번
# a = float(input("수 입력: "))
# b = float(input("수 입력: "))
# c = input("연산자 입력: ")
# if c == "+":
#     print(f"{a} + {b} = {a + b}")
# elif c == "-":
#     print(f"{a} - {b} = {a - b}")
# elif c == "*":
#     print(f"{a} * {b} = {a * b}")
# elif c == "/":
#     print(f"{a} / {b} = {a / b}")
# else:
#     print("오류")

# 32번
# a = float(input("금액 입력: "))
# b = float(input("세율 입력: "))
# c = a*(b/100)
# d = a - c
# print(f"세금: {c}원")
# print(f"세후 금액: {d}원")

# 33번
# a = input("1.불리언 값: ") True
# b = input("2.불리언 값: ") Flase
# print(f"{a} AND {b} => {a and b}") -> 결과 False 
# print(f"{a} OR {b} => {a or b}") -> 결과 True 
# print(f"NOT {a} => {not a}") -> 결과 False 
# print(f"NOT {b} => {not b}") -> 결과 False: 빈 문자열만 False
'''
a = input("첫 번째 불리언 입력 (True 또는 False): ")
b = input("두 번째 불리언 입력 (True 또는 False): ")

# 문자열을 실제 Boolean 타입으로 변환
a_bool = True if a == "True" else False
b_bool = True if b == "True" else False
if a == "True":
    a_bool = True
else:
    a_bool = False
if b == "True":
    b_bool = True
else:
    b_bool = False

# 논리 연산 출력
print(f"{a_bool} AND {b_bool} => {a_bool and b_bool}")
print(f"{a_bool} OR {b_bool} => {a_bool or b_bool}")
print(f"NOT {a_bool} => {not a_bool}")
print(f"NOT {b_bool} => {not b_bool}")
'''

# 34번
# a = float(input("원래가격: "))
# b = float(input("할인율: "))
# print(f"할인 금액: {a*(b/100)}원")
# print(f"최종 가격: {a-(a*(b/100))}원")

# 35번
# a = float(input("첫 번째 수: "))
# b = float(input("두 번째 수: "))
# c = float(input("세 번째 수: "))
# #print(f"가장 큰 수: {max(a,b,c)}")
# if a >= b and a >= c:
#     max_num = a
# elif b >= a and b >= c:
#     max_num = b
# else:
#     max_num = c
# print("가장 큰 수:", max_num)

# 36번
# a = int(input("연도: "))
# if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
#     print(f"{a}년은 윤년입니다.")
# else:
#     print(f"{a}년은 윤년이 아닙니다.")

# 37번
# a = input("첫 번째 문자열 입력: ")
# b = input("두 번째 문자열 입력: ")
# if b in a:
#     print(f"{a}에 {b}이(가) 포함되어 있습니다.")
# else:
#     print(f"{a}에 {b}이(가) 포함되어 있지 않습니다.")

# 38번
# a =  int(input("점수 입력: "))
# if a >= 90:
#     r = "A"
# elif a >= 80:
#     r = "B"
# elif a >= 70:
#     r = "C"
# elif a >= 60:
#     r = "D"
# else:
#     r = "F"
# print(f"학점: {r}")

# 39번
# a = (input("양의 정수 입력: "))
# sum = int(a[0]) + int(a[1]) + int(a[2]) + int(a[3])
# print(f"자릿수 합계: {sum}")
'''
map 함수 사용
s = sum(map(int, a))
print(f"자릿수 합계: {s}")
'''
'''
for문 사용
sum = 0
for s in a:
    sum += int(s)
print(f"자릿수 합계: {sum}")
'''

# 40번
# a = int(input("나이: "))
# b = input("회원 여부(Y/N) ")
# if a >= 19 and b == "N":
#     s = 10000
# elif a >= 19 and b == "Y":
#     s = 8000
# else:
#     s = 5000
# print(f"입장료: {s}원")
    
# 41번
# a = input("비밀번호 입력: ")
# b = (len(a))
# if b >= 8 and a[0] != "":
#     print("안전한 비밀번호입니다.")
# else:
#     print("잘못된 비밀번호입니다.")
'''
if b >= 8:
    letter = False
    digit = False
    for char in a:
        if char.isdigit():
            digit = True
        elif char.isalpha():
            letter = True
    if letter and digit:
        print("안전한 비밀번호")
    else:
        print("문자, 숫자 모두 포함되어야함")
else:
    print("8자 이상")
'''

# 42번
# a,b,c = input("문자열 입력: ").split()
# a = a[::-1]
# b = b[::-1]
# c = c[::-1]
# print(a+" "+b+" "+c)
# print(f"{a} {b} {c}")

# 43번
# a = input("문장 입력: ").lower()
# b = "aeiou"
# b_count = 0
# c_count = 0
# for ch in a:
#     if ch in b:
#         b_count += 1
#     elif ch.isalpha():
#         c_count += 1
# print("모음 개수:", b_count)
# print("자음 개수:", c_count)

# 44번
# a = float(input("실수 입력: "))
# b = round(a)
# print(f"가장 가까운 정수: {b}")

# 45번
# a,b,c = input("연월일 입력: ").split("-")
# a,b,c = int(a),int(b),int(c)
# d = (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0)
# if b<1 or b>12:
#     print("유효하지 않은 날짜입니다.")
# else:
#     if b ==2:
#         if d:
#             day = 29
#         else:
#             day = 28
#     elif b in [4, 6, 9, 11]:
#         day = 30
#     else:
#         day = 31

#     if 1 <= c <= day:
#         print("유효한 날짜입니다.")
#     else:
#         print("유효하지 않은 날짜입니다.")

# 46번
# a,b = input("파일명 입력: ").split(".")
# print(f"확장자: {b}")

# 47번
# 문자열 입력 받기
# s = input("문자열 입력: ")
# # 압축된 결과를 저장할 변수
# compressed = ""
# # 첫 번째 문자와 그 개수를 추적
# count = 1
# # 문자열을 순회하면서 연속된 문자 수 세기
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         count += 1  # 문자가 같으면 개수 증가
#     else:
#         compressed += s[i - 1] + str(count)  # 문자가 다르면 이전 문자와 개수 추가
#         count = 1  # 새 문자의 개수는 1로 초기화
# # 마지막 문자 처리
# compressed += s[-1] + str(count)
# # 결과 출력
# print("압축된 문자열:", compressed)

# 48번
# a = input("문자열 입력: ")
# b = a[::-1]
# if a==b:
#     print(f"{a}은 팰린드롬입니다.")
# else:
#     print("팰린드롬아닙니다.")

# 49번 아스키코드..
'''
# 문자열 입력 받기
text = input("문자열 입력: ")

# 암호화된 결과를 저장할 변수
encrypted_text = ""

# 각 문자를 순차적으로 처리
for char in text:
    # 알파벳 대문자일 때만 처리
    if 'A' <= char <= 'Z':
        # 각 문자의 아스키 코드 값
        new_char = chr(((ord(char) - ord('A') + 3) % 26) + ord('A'))
        encrypted_text += new_char
    else:
        # 알파벳 외의 문자는 그대로 추가
        encrypted_text += char

# 결과 출력
print("암호화:", encrypted_text)
'''

# 50번
# a,b,c,d = map(int,input("IP입력: ").split("."))
# e = [a,b,c,d]
# if len(e) == 4:
#     if 0<=a<=255 and 0<=b<=255 and 0<=c<=255 and 0<=d<=255:
#         print("유효한 IP 주소입니다.")
#     else:
#         print("유효하지 않은 IP 주소입니다.")
# else:
#         print("유효하지 않은 IP 주소입니다.")

'''
all 함수
a, b, c, d = map(int, input("IP입력: ").split("."))
e = [a, b, c, d]

if len(e) == 4 and all(0 <= x <= 255 for x in e):
    print("유효한 IP 주소입니다.")
else:
    print("유효하지 않은 IP 주소입니다.")
'''