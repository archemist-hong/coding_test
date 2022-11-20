# 1. 규칙성 찾기 ex) 1111 / 3 = 37 1
# 2. 문자열 활용

# onelist = list(map(int,input().split()))
while True:  # 들어오는 입력값 받기 위한 반복문
    try:  # 입력값이 더이상 들어오지 않을때 예외처리
        a = int(input())  # a : 입력값
    except:
        break
    n = 1  # n = 나머지 , 1 % a 로 나타내는게 훨씬 가독성 좋을듯
    while int("1" * n) % a:  # 나머지가 0일 될때 멈춤
        n += 1  # 자리수 증가
    print(n)
