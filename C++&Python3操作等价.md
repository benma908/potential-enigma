
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
q = [1,2,3]
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
