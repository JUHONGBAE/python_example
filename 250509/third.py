# 반복문
# s = 'hello'
# for i in s:
#     print(i)

# a = [1,2,3,4,5,6,"good"]
# for i in a:
#     print(i)

# range(숫자) 0부터 숫자 -1까지의 범위를 만든다.
# for i in range(5000): # 0부터 4999까지의 어떤 순회가능한 데이터를 만든다.
#     print(i)

# range(10,51) # 10부터 50까지의 범위를 만든다.
# for i in range(10,51):
#     print(i)

# range(1,11,2)
# for i in range(1,11,2): # 1부터 10까지 2계단씩 점프
#     print(i)

# range(5000) === range(0,5000,1)
# 내림차순
# for i in range(10,1,-1):
#     print(i)

"""
1 부터 100까지 출력
2 부터 50까지 짝수만 출력
10 부터 -1까지 출력력
"""
# #1
# for a in range(1,101):
#     print(a)
# #2
# for b in range(2,51,2):
#     print(b)
# #3
# for c in range(10,-2,-1):
#     print(c)

# for i in range(1,100):
#     if i % 3 == 0:
#         print(i)

# 2~9 구구단 만들기
# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} * {j} = {i*j}")
#     print("\n")

for i in range(2,10):
    for j in range(1,10):
        print(f"{i} * {j} = {i*j}")
        if i*j == 9:
            print(9)