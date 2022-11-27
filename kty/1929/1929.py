# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
import math

a_nums = list(map(int, input().split()))
n_min = min(a_nums)
n_max = max(a_nums)

array = [True for i in range(n_max + 1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n_max)) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인하며

    if array[i] == True:  # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n_max:
            array[i * j] = False
            j += 1
# print(array)
# 모든 소수 출력
for i in range(n_min, n_max + 1):
    if i == 1:
        continue
    if array[i]:
        print(i, end="\n")
