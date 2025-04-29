# age = 20
# height = 180
# if age > 18 and height >= 150:
#     print("성인입니다.")

# print("END")

'''
pw1 = input("비밀번호: ")
pw2 = input("비밀번호 확인: ")
if pw1 != pw2:
    print("회원가입 거부")
'''

# if ~ else 구문 if가 참이 아니면 else 구문을 실행

# age = 20
# if age >= 30:
#     print("30대 이상")
# else:
#     print("30대 x")

# if ~ elif ~ else 구문


# age = int(input("나이 입력: "))
# if age <= 19:
#     print("청소년")
# elif age < 30:
#     print("20대")
# else:
#     print("30대 이상")

'''
한줄에 생년월일(yyyy) 월(mm) 일(dd) 가 공백을 기준으로 입력된다.
년도가 짝수라면 "짝수 년도에 태어났습니다." 아니라면 "홀수 년도에 태어났습니다 를 출력)
'''

'''
y, m, d = input("생년월일 입력: ").split()
y = int(y)
m = int(m)
d = int(d)
if y % 2 == 0:
    print("짝수 년도에 태어났습니다.")
else:
    print("홀수 년도에 태어났습니다.")
'''

y, m, d = input("생년월일 입력: ").split("-")
y = int(y)
m = int(m)
d = int(d)
if y % 2 == 0:
    print("짝수 년도에 태어났습니다.")
else:
    print("홀수 년도에 태어났습니다.")