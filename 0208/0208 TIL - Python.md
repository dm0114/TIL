# 0208 TIL - Python

---

## Python

### 1. 백준 2563 색종이

---

`2차원 행열을 생성하여 0으로 초기화한 후 색종이 영역을 1로 만들기`

```python
loop = int(input())
li = [[0 for _ in range(101)]for _ in range(101)] # 100 * 100 좌표

for _ in range(loop):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            li[i][j] = 1

count = 0
for row in li:
    count += row.count(1)

print(count)
```

### 2. **나이순 정렬**

---

`user.sort(key=lambda a:int(a[0]))`

```python
n = int(input())

user = []

for _ in range(n):
    user.append((list(input().split())))

user.sort(key=lambda a:int(a[0]))

for i in range(n):
    print(user[i][0], user[i][1])
```

### **`sort`**(***, *key=None*, *reverse=False*)

---

이 메서드는 항목 간의 `<` 비교만 사용하여 리스트를 제자리에서 정렬합니다. 예외는 억제되지 않습니다 - 비교 연산이 실패하면 전체 정렬 연산이 실패합니다 (리스트는 부분적으로 수정된 상태로 남아있게 됩니다).

`[sort()](https://docs.python.org/ko/3/library/stdtypes.html?highlight=sort#list.sort)` 는 키워드로만 전달할 수 있는 두 개의 인자를 받아들입니다 ([키워드-전용 인자](https://docs.python.org/ko/3/glossary.html#keyword-only-parameter)):

- *key* 는 인자 하나를 받아들이는 함수를 지정하는데, 각 리스트 요소에서 비교 키를 추출하는 데 사용됩니다 (예들 들어, `key=str.lower`). 리스트의 각 항목에 해당하는 키는 한 번만 계산된 후 전체 정렬 프로세스에 사용됩니다. 기본 값 `None` 은 리스트 항목들이 별도의 키 값을 계산하지 않고 직접 정렬된다는 것을 의미합니다.
- *reverse* 는 논리값입니다. `True` 로 설정되면, 각 비교가 역전된 것처럼 리스트 요소들이 정렬됩니다.
이 메서드는 큰 시퀀스를 정렬할 때 공간 절약을 위해 시퀀스를 제자리에서 수정합니다. 부작용으로 작동한다는 것을 사용자에게 상기시키기 위해 정렬된 시퀀스를 돌려주지 않습니다 (새 정렬 된 리스트 인스턴스를 명시적으로 요청하려면 `[sorted()](https://docs.python.org/ko/3/library/functions.html#sorted)`를 사용하십시오).

`[sort()](https://docs.python.org/ko/3/library/stdtypes.html?highlight=sort#list.sort)` 메서드는 안정적임이 보장됩니다. 정렬은 같다고 비교되는 요소들의 상대적 순서를 변경하지 않으면 안정적입니다 — 이는 여러 번 정렬하는 데 유용합니다 (예를 들어, 부서별로 정렬한 후에 급여 등급으로 정렬).

> 출처 : [파이썬 자습서](https://docs.python.org/ko/3/library/stdtypes.html?highlight=sort#list.sort)
> 

### 3. 수 정렬 하기3 10989

---

```python
import sys

count = int(input())
numbers = [0] * 10001

for _ in range(count):
    numbers[int(sys.stdin.readline())] += 1

for n in range(10001):

    if numbers[n] != 0:

        for _ in range(numbers[n]):
            print(n)

# for문으로 받아서 정렬하면 메모리 초과
# 0으로 된 리스트를 제작 후
# input 대신 sys.stdin.readline()이 빠르다.
```

### 4. 피보나치 수 2

---

```python
n = int(input())
fibo = [0,1]
if n >= 2:
    for i in range(2,n+1):
        fibo.append(fibo[i-2]+fibo[i-1])

print(fibo[n])
```

### 5. 슈퍼마리오

---

`근사값 : abs 사용`

```python
mushroom = []

hp = 0

for _ in range(10):

    mushroom.append(int(input()))

for m in mushroom:

    hp += m

    if hp >= 100:

        if abs(100-hp) <= abs(100-(hp-m)):

            break

        else:

            hp -= m
            break

print(hp)
```

### 6. 탐색

---

`전화번호부 탐색 (반절 씩 줄어들게 찾기)`

```python
N = int(input())
num_list = list(map(int,input().split()))
M = int(input())
tf_list = list(map(int, input().split()))

num_list.sort()

def mid(tf,num_list,left,right):
    if left > right:
        return 0
    m = (left+right)//2
    if num_list[m] == tf:
        return 1
    elif num_list[m] > tf:
        return mid(tf,num_list,left,m-1)
    else:
        return mid(tf,num_list,m+1,right)

for tf in tf_list:
    print(mid(tf,num_list,0,len(num_list)-1))

# 세트 탐색이 더 빠름
# log2n
```