import numpy


def f1(a, b, c):
    ans1 = (a + b) % c
    ans2 = ((a % c) + (b % c)) % c
    ans3 = (a * b) % c
    ans4 = ((a % c) * (b % c)) % c
    print("{}\n{}\n{}\n{}\n".format(ans1, ans2, ans3, ans4))


if __name__ == "__main__":
    A, B, C = list(map(int, input().split(" ")))
    f1(A, B, C)
