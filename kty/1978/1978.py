# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
import math

a = int(input())
a_nums = list(map(int, input().split()))
a_list = []
for i in a_nums:
    n = 0
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            n += 1
    if n == 0:
        a_list.append(i)

print(len(a_list))
