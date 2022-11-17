# 2와 5로 나누어 떨어지지 않는 정수 n(1 ≤ n ≤ 10000)가 주어졌을 때, 
# 1로만 이루어진 n의 배수를 찾는 프로그램을 작성 

# 1. 규칙성 찾기 ex) 1111 / 3 = 37 1 
# 2. 문자열 활용

# onelist = list(map(int,input().split()))
# while True:
#     try:
#         a = int(input())
#     except:
#         break
#     n=2
#     while int('1'*n) % a:
#         n+=1
#     print(n)
while True: # 계속 들어오는 테스트 케이스 입력을 받기 위한 반복문
    try: # 계속 들어오는 테스트 케이스 입력을 받기 위한 예외처리
        N = int(input())
    except:
        break
    # 여기부터 본 코드
    remains = 1 % N # N으로 나눈 나머지
    digits = 1 # 자리수
    while remains: # 나머지가 0이 아닌동안 반복
        remains = (remains * 10 + 1) % N # (이전의 나머지 * 10 + 1)을 다시 N으로 나눈 나머지
        digits += 1 # 자리수 증가
    print(digits)
# def onef(number):
#     if int('1'*n) % number == 0:
#         print(n)
#     else:
#         n+=1
#         onef(number)
