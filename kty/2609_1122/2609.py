# 두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.

a, b = list(map(int, input().split()))
n = a * b
while b != 0:
    r = a % b
    a = b
    b = r
print(a)
print(n // a)
