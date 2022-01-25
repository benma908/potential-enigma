### 快速排序算法模板 —— 模板题 AcWing 785. 快速排序
```python
def quick_sort(q:[], l:int, r:int)->None:
    if l>=r:
        return
    p, i, j = q[l + r>>1], l -1, r + 1
    while i < j:
        while 1:
            i += 1
            if q[i] >= p:
                break
        while 1:
            j -= 1
            if q[j] <= p:
                break
        if i < j:
            q[i], q[j] = q[j], q[i]
    quick_sort(q, l, j)
    quick_sort(q, j + 1, r)
```

###  归并排序算法模板 —— 模板题 AcWing 787. 归并排序
```python
def merge_sort(q, l, r):
    if l >= r:
        return
    mid = l + r >> 1
    merge_sort(q, l, mid)
    merge_sort(q, mid + 1, r)
    i, j = 0, mid + 1
    tmp = list()
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            tmp.append(q[i])
            i += 1
        else:
            tmp.append(q[j])
            j += 1
    while i <= mid:
        tmp.append(q[i])
        i += 1
    while j <= r:
        tmp.append(q[j])
        j += 1
    k = 0
    for i in range(l, r+1):
        q[i] = tmp[k]
        k += 1
```
### 整数二分算法模板 —— 模板题 AcWing 789. 数的范围
区间[l, r]被划分成[l, mid]和[mid + 1, r]时使用：

```python
def check(x:int)->bool: ###  检查x是否满足某种性质
    return False
def bsearch_1(l:int, r:int)->int:
    while l < r:
        mid = l + r >> 1
        if check(mid): ### check()判断mid是否满足性质
            r = mid
        else:
            l = mid + 1
    return l
```
区间[l, r]被划分成[l, mid - 1]和[mid, r]时使用：
```python
def check(x:int)->bool: ###  检查x是否满足某种性质
    return False
def bsearch_2(l:int ,  r:int) ->int:
    while l < r:
        mid = l + r + 1 >> 1
        if check(mid):
            l = mid
        else:
            r = mid - 1
    return l
```
### 浮点数二分算法模板 —— 模板题 AcWing 790. 数的三次方根
```python
def  check(x:float)->bool: ### 检查x是否满足某种性质
    return False

def bsearch_3( l:float,  r:float)-> float:
    eps = 1e-6   ### eps 表示精度，取决于题目对精度的要求
    while r - l > eps:
        mid = (l + r) / 2
        if check(mid):
            r = mid
        else:
            l = mid
    return l
```

### 一维前缀和 —— 模板题 AcWing 795. 前缀和
```cpp
 S[i] = a[1] + a[2] + ... a[i]
 a[l] + ... + a[r] = S[r] - S[l - 1]
```

### 二维前缀和 —— 模板题 AcWing 796. 子矩阵的和
S[i, j] = 第i行j列格子左上部分所有元素的和
以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵的和为：
```cpp
S[x2, y2] - S[x1 - 1, y2] - S[x2, y1 - 1] + S[x1 - 1, y1 - 1]
```

### 一维差分 —— 模板题 AcWing 797. 差分
给区间[l, r]中的每个数加上c：
```cpp
B[l] += c, B[r + 1] -= c
```

### 二维差分 —— 模板题 AcWing 798. 差分矩阵
给以(x1, y1)为左上角，(x2, y2)为右下角的子矩阵中的所有元素加上c：
```cpp
S[x1, y1] += c, S[x2 + 1, y1] -= c, S[x1, y2 + 1] -= c, S[x2 + 1, y2 + 1] += c
```

### 位运算 —— 模板题 AcWing 801. 二进制中1的个数
求n的第k位数字： 
```cpp
n >> k & 1
```

返回n的最后一位1：
```cpp
lowbit(n) = n & -n
```

### 双指针算法 —— 模板题 AcWIng 799. 最长连续不重复子序列, AcWing 800. 数组元素的目标和
```python
j = 0
for i in range(n):
    while (j < i and check(i, j)):
        j += 1
    ### 具体问题的逻辑
```

常见问题分类：
1. 对于一个序列，用两个指针维护一段区间 
2. 对于两个序列，维护某种次序，比如归并排序中合并两个有序序列的操作

### 离散化 —— 模板题 AcWing 802. 区间和
存储所有待离散化的值：
```python
alls = list()
### 将所有值排序：
alls.sort()
### 去掉重复元素：
alls = list(dict.fromkeys(alls)) 
### 二分求出x对应的离散化的值
def find(x):
    l, r = 0, len(alls) - 1
    while l < r:
        mid = l + r >> 1
        if alls[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return r + 1   ### 映射到1, 2, ...n
```

### 区间合并 —— 模板题 AcWing 803. 区间合并
```python
### 将所有存在交集的区间合并
def merge(a: [(int, int)]):
    res = list()
    a.sort(key=lambda x:x[0])

    cur_st, cur_ed = -10 ** 9, -10 ** 9
    for st, ed in a:
        if cur_ed < st:
            if cur_st != -10 ** 9:
                res.append((cur_st, cur_ed))
            cur_st, cur_ed = st, ed
        else:
            cur_ed = max(cur_ed, ed)

    if cur_st != -10 ** 9:
        res.append((cur_st, cur_ed))
    segs = res
```
