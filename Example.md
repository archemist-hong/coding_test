# A + B
- 문제링크 (https://www.acmicpc.net/problem/1000)
- 풀이자: 홍주영
- 풀이일자: 2022-11-12(토)

## 알고리즘
없음

## 시간복잡도
O(n) 
- 참조: https://stackoverflow.com/questions/20135093/what-is-the-time-complexity-of-sum-in-python
- 실제 소요 시간
    - 92 ms
- 실제 소요 메모리
    - 30840 KB

## 해설
인풋을 받아 int형으로 변환한뒤, 더하기 연산하여 결과를 출력한다.

## 중요 포인트
string형 input을 int로 변환이 필요하다.

## 코드
``` python
A, B = [int(inp) for inp in input().split()] # string -> int
print(A + B)
```