a, b, c = list(map(int, input().split(" ")))

ans1 = (a + b) % c
ans2 = ((a % c) + (b % c)) % c
ans3 = (a * b) % c
ans4 = ((a % c) * (b % c)) % c
print("{}\n{}\n{}\n{}\n".format(ans1, ans2, ans3, ans4))
