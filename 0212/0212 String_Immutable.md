# 0212 문자열 수정

## Python

### 1. 5와 6의 차이 - 백준 2864

---

`문자열은 Immutable 이므로 리스트를 사용하자`

- 최솟값 : 5로 바꿔서 합치기
- 최댓값 : 6으로 바꿔서 합치기

```python
a, b = input().split()
a = list(a) #이 코드를 생략해서 immutable error 발생
b = list(b) #이 코드를 생략해서 immutable error 발생
ans_li = [0, 0]

# 1. 6을 모두 5로 변환
# 두 수의 합을 배열[0]에 저장
for i in range(len(a)):
    if a[i] == '6':
        a[i] = '5'

for i in range(len(b)):
    if b[i] == '6':
        b[i] = '5'

a = int(''.join(a))
b = int(''.join(b))
ans_li[0] = a + b
print(ans_li[0], end=' ')

#2. 6을 5로 변환
# 두 수의 합을 배열[1]에 저장
a = str(a)
b = str(b)

a = list(map(str, a))
b = list(map(str, b))

for i in range(len(a)):
    if a[i] == '5':
        a[i] = '6'

for i in range(len(b)):
    if b[i] == '5':
        b[i] = '6'

a = int(''.join(a))
b = int(''.join(b))
ans_li[1] = a + b
print(ans_li[1])
```