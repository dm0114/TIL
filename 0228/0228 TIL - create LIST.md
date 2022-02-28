# 0228 TIL - List create

```python
# 입력받은 수로 배열 생성
a, b = map(int, input().split())
li1 = [a for _ in range(5)]
li2 = [b for _ in range(5)]

# 입력받아서 2차원 배열 생성
N = int(input())
li3 = [[int(num) for num in input().split()] for _ in range(N)]

```