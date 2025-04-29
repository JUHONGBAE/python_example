# # 비교연산

# x, y = 10, 100

# print(x==y)

# x,y = 10, 11
# print(x>y) #초과
# print(x>=y)

# print(x<y)
# print(x<=y)

# print('apple'<'banana') # 결과: True

# print(5<x<15) #결과: Ture

'''
input() 으로 키와 몸무게를 입력받는다. (숫자형으로 변환)
키가 130 이하이면 "키 미만"을 출력하고, 몸무게가 10 이상이면 "정상"을 출력하세요
'''

# height = int(input("키: "))
# weight = int(input("몸무게: "))

# (height<=130 and print("키 미만"))
# (weight>=10 and print("정상"))

# a = "good"
# print(len(a)) # len(변수)는 변수의 문자 수를 가져온다.

"""
input() 두 번을 사용하여, 두개의 변수의 임의의 문자열을 넣고,
len() 을 사용하여 문자의 수를 변수에 넣는다.

'첫번째 변수의 문자 수는 {문자의 수} 입니다.'
'두두번째 변수의 문자 수는 {문자의 수} 입니다.'
"""

# a = input("첫 번째 문자: ")
# b = input("두 번째 문자: ")
# lena = len(a)
# lenb = len(b)
# print(f"첫번째 변수의 문자 수는 {lena} 입니다.")
# print(f"두번째 변수의 문자 수는 {lenb} 입니다.")

# i = 10
# j = 10.5222222222

# print(f"j의 값은 {j:.2f}") # 소수점 둘째자리까지 표현

# money = 10000000000000
# print(f"{money:,}") # 3자리수로 콤마(,) 찍어서 출력

a = float(input("숫자 입력: "))
b = float(input("숫자 입력: "))
c = (f"{a:.2f}") == (f"{b:.2f}")
print(f"두 숫자가 같을까요?? {c}")