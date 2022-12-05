# 골드바흐의 추측
# 1742년, 독일의 아마추어 수학가 크리스티안 골드바흐는 레온하르트 오일러에게 다음과 같은 추측을 제안하는 편지를 보냈다.

# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 예를 들어 8은 3 + 5로 나타낼 수 있고, 3과 5는 모두 홀수인 소수이다. 또, 20 = 3 + 17 = 7 + 13, 42 = 5 + 37 = 11 + 31 = 13 + 29 = 19 + 23 이다.

# 이 추측은 아직도 해결되지 않은 문제이다.

# 백만 이하의 모든 짝수에 대해서, 이 추측을 검증하는 프로그램을 작성하시오.
import math

# n = a + b
n_max = 1000000

array = [True for i in range(n_max + 1)]  # 처음엔 모든 수가 소수(True)인 것으로 초기화

# 에라토스테네스의 체 알고리즘
for i in range(
    3, int(math.sqrt(n_max)) + 1, 2
):  # 3부터 n의 제곱근까지의 홀수들만 확인 결국 확인하는 것은 홀수+홀수이므로

    if array[i] == True:  # i가 소수인 경우 (남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n_max:
            array[i * j] = False
            j += 1

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n_max + 1, 2):  # 홀수들만 확인(홀수 소수 찾기)
        if array[n - i] & array[i]:
            print("{} = {} + {}".format(n, i, n - i))
            break
