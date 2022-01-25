## C++ 二分查找 <=> Python3 bisect

### 操作：查找 lower_bound

- C++

```cpp
set<int> s2 {1,2,3};
x = 2
auto it = s2.lower_bound(x);
```

- Python3

```python
import bisect

q = [1, 2, 3]
x = 2
# n: 1
n = bisect.bisect_left(q, x)
```

## C++ vector <=> Python3 list

### 操作：初始化容量，然后递增 size 扩展

- C++

```cpp
vector<int> t1{0}, t2{0};
t1.reserve(1 << (n / 2 + 1));
t2.reserve(1 << (n / 2 + 1));
for (int i = 0; i < n / 2; ++i)
  for (int j = t1.size() - 1; j >= 0; --j)
    t1.push_back(t1[j] + nums[i]);
for (int i = n / 2; i < n; ++i)
  for (int j = t2.size() - 1; j >= 0; --j)
    t2.push_back(t2[j] + nums[i]);
```

- Python3

```python
nums = [5, -7, 3, 5]
n = len(nums)
a = [0]
for i in range(n >> 1):
    tmp = []
    for j in range(len(a) - 1, -1, -1):
        tmp.append(a[j] + nums[i])
    a.extend(tmp)
```

## C++ 读取输入列表 <=> Python3 input()

- C++

```cpp
int n,a[101],run=0;
    
scanf("%d",&n);

for(int i=1;i<=n;i++){
    scanf("%d",&a[i]);
    run+=a[i];
}
```

- Python3

```python
n = int(input())
a = list(map(int, input().split()))
run = sum(a) // n 
```

## C++ 最小堆 <=> Python3 heapq

- C++

```cpp
priority_queue<PII, vector<PII>, greater<PII>> heap;
heap.push(stall);
heap.top();
heap.pop();
```

- Python3

```python
from heapq import heappush, heappop, heapreplace, heapify

item, x = 1, [1]
heap = []  # creates an empty heap
heappush(heap, item)  # pushes a new item on the heap
item = heappop(heap)  # pops the smallest item from the heap
item = heap[0]  # smallest item on the heap without popping it
heapify(x)  # transforms list into a heap, in-place, in linear time
item = heapreplace(heap, item)  # pops and returns smallest item, and adds
# new item; the heap size is unchanged
```
