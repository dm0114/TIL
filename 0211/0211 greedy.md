# 0211 그리디

> 그리디
> 

```python
while change != 0:                 # 거슬러 줄 돈이 0이 될때까지
    for i in li:                   # 리스트에 있는 큰 수 부터 순회 [500, 100, 50, 10]
        if change - i >= 0:        # 거슬러줄 수 있다면 거슬러 준 후 카운팅
            change = change - i
            count += 1
			break                  # 실행 됐다면, 큰 수 부터 다시 순회 li[0]
                                   # 그렇지 않다면 그 다음 큰 수 선택   li[1], [2], ... [-1]
```