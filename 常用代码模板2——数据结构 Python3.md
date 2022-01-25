### 单链表 —— 模板题 AcWing 826. 单链表

```python
# head存储链表头，e[]存储节点的值，ne[]存储节点的next指针，idx表示当前用到了哪个节点
head, e, ne, idx = -1, [0] * n, [0] * n, 0


# 初始化
def init():
    head = -1
    idx = 0


# 在链表头插入一个数a
def insert(a):
    global idx, head
    e[idx] = a
    ne[idx] = head
    head = idx
    idx += 1


# 将头结点删除，需要保证头结点存在
def remove():
    global head
    head = ne[head]
```

### 双链表 —— 模板题 AcWing 827. 双链表

```python
# e[]表示节点的值，l[]表示节点的左指针，r[]表示节点的右指针，idx表示当前用到了哪个节点

e, l, r, idx = [0] * n, [0] * n, [0] * n, 0


# 初始化
def init():
    # 0是左端点，1是右端点
    global idx
    r[0] = 1
    l[1] = 0
    idx = 2


# 在节点a的右边插入一个数x
def insert(a: int, x: int):
    global idx
    e[idx] = x
    l[idx] = a, r[idx] = r[a]
    l[r[a]] = idx
    r[a] = idx
    idx += 1


# 删除节点a
def remove(a: int):
    l[r[a]] = l[a]
    r[l[a]] = r[a]
```

### 栈 —— 模板题 AcWing 828. 模拟栈

#### tt表示栈顶

```python
stk, tt = [0] * n, 0
```

#### 向栈顶插入一个数

```python
tt += 1
stk[tt] = x
```

#### 从栈顶弹出一个数

```python
tt -= 1
```

#### 栈顶的值

```python
stk[tt]
```

#### 判断栈是否为空

```python
if tt > 0:
```

### 队列 —— 模板题 AcWing 829. 模拟队列

1. 普通队列：

#### hh 表示队头，tt表示队尾

```python
q = [0] * n
hh, tt = 0, -1
```

#### 向队尾插入一个数

```python
tt += 1
q[tt] = x
```

#### 从队头弹出一个数

```python
hh += 1
```

#### 队头的值

```python
q[hh]
```

#### 判断队列是否为空

```python
if hh <= tt:
```

2. 循环队列

#### hh 表示队头，tt表示队尾的后一个位置

```python
q = [0] * n
hh, tt = 0, 0
```

#### 向队尾插入一个数

```python
q[tt] = x
tt += 1
if tt == n:
    tt = 0
```

#### 从队头弹出一个数

```python
hh += 1
if hh == n:
    hh = 0
```

#### 队头的值

```python
q[hh]
```

#### 判断队列是否为空

```python
if hh != tt:
```

### 单调栈 —— 模板题 AcWing 830. 单调栈 常见模型：找出每个数左边离它最近的比它大/小的数 int tt = 0 for (int i = 1 i <= n i ++ )

```python
while tt and check(stk[tt], i):
    tt -= 1
tt += 1
stk[tt] = i
```

### 单调队列 —— 模板题 AcWing 154. 滑动窗口 常见模型：找出滑动窗口中的最大值/最小值 int hh = 0, tt = -1 for (int i = 0 i < n i ++ )

```python
while hh <= tt and check_out(q[hh]):
    hh += 1  # 判断队头是否滑出窗口
while hh <= tt and check(q[tt], i):
    tt -= 1
tt += 1
q[tt] = i
```

### KMP —— 模板题 AcWing 831. KMP字符串

#### s[]是长文本，p[]是模式串，n是s的长度，m是p的长度

#### 求模式串的Next数组

```python
j = 0
for i in range(2, m + 1):
    while j and p[i] != p[j + 1]:
        j = ne[j]
    if p[i] == p[j + 1]:
        j += 1
    ne[i] = j
```

#### 匹配

```python
j = 0
for i in range(1, n + 1):
    while j and s[i] != p[j + 1]:
        j = ne[j]
    if s[i] == p[j + 1]:
        j += 1
    if j == m:
        j = ne[j]
        # 匹配成功后的逻辑
```

### Trie树 —— 模板题 AcWing 835. Trie字符串统计

#### int son[N][26], cnt[N], idx

#### 0号点既是根节点，又是空节点

#### son[][]存储树中每个节点的子节点

#### cnt[]存储以每个节点结尾的单词数量

#### 插入一个字符串

```python
def insert(s):
    p = 0
    for i in range(len(s)):
        u = ord(s[i]) - ord('a')
        # 该节点没有存储过
        if not son[p][u]:
            idx += 1
            son[p][u] = idx
        p = son[p][u]
    # 最后的这个 s 字符串的数量
    cnt[p] += 1
```

#### 查询字符串出现的次数

```python

def query(s):
    p = 0
    for i in range(len(s)):
        u = ord(s[i]) - ord('a')
        if not son[p][u]:
            return 0
        p = son[p][u]
    return cnt[p]
```

### 并查集 —— 模板题 AcWing 836. 合并集合, AcWing 837. 连通块中点的数量

1. 朴素并查集：

```python
# 存储每个点的祖宗节点
p = [0] * n


# 返回x的祖宗节点
def find(x: int):
    if p[x] != x:
        # 将父节点的父节点也优化成根节点
        p[x] = find(p[x])
    return p[x]
```

#### 初始化，假定节点编号是 1 ~ n

```python
for i in range(1, n + 1):
    p[i] = i
```

#### 合并a和b所在的两个集合：

```python
p[find(a)] = find(b)
```

2. 维护size的并查集

```python
# p[]存储每个点的祖宗节点, size[]只有祖宗节点的有意义，表示祖宗节点所在集合中的点的数量
p, size = [0] * n, [0] * n


# 返回x的祖宗节点
def find(x: int):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


# 初始化，假定节点编号是1~n
for i in range(1, n + 1):
    p[i] = i
    size[i] = 1

# 合并a和b所在的两个集合
size[find(b)] += size[find(a)]
p[find(a)] = find(b)
```

3. 维护到祖宗节点距离的并查集

```python
# p[]存储每个点的祖宗节点, d[x]存储x到p[x]的距离
p, d = [0] * n, [0] * n


# 返回x的祖宗节点
def find(x: int):
    if p[x] != x:
        u = find(p[x])
        d[x] += d[p[x]]
        p[x] = u
    return p[x]


# 初始化，假定节点编号是1~n
for i in range(1, n + 1):
    p[i] = i
    d[i] = 0

# 合并a和b所在的两个集合：
p[find(a)] = find(b)
d[find(a)] = distance  # 根据具体问题，初始化find(a)的偏移量
```

### 堆 —— 模板题 AcWing 838. 堆排序, AcWing 839. 模拟堆

```python
# h[N]存储堆中的值, h[1]是堆顶，x的左儿子是2x, 右儿子是2x + 1
# ph[k]存储第k个插入的点在堆中的位置
# hp[k]存储堆中下标是k的点是第几个插入的
h, ph, hp, size = [0] * n, [0] * n, [0] * n, 0


# 交换两个点，及其映射关系

def heap_swap(a: int, b: int):
    ph[hp[a]], ph[hp[b]] = ph[hp[b]], ph[hp[a]]
    hp[a], hp[b] = hp[b], hp[a]
    h[a], h[b] = h[b], h[a]


def down(u: int):
    t = u
    if u * 2 <= size and h[u * 2] < h[t]:
        t = u * 2
    if u * 2 + 1 <= size and h[u * 2 + 1] < h[t]:
        t = u * 2 + 1
    if u != t:
        heap_swap(u, t)
        down(t)


def up(u: int):
    while u / 2 and h[u] < h[u // 2]:
        heap_swap(u, u // 2)
        u >>= 1


# O(n)建堆
for i in range(n // 2, -1, -1):
    down(i)
```

### 一般哈希 —— 模板题 AcWing 840. 模拟散列表

1. 拉链法

```python
h, e, ne, idx = [0] * n, [0] * n, [0] * n, 0


# 向哈希表中插入一个数
def insert(x: int):
    k = (x % n + n) % n
    e[idx] = x
    ne[idx] = h[k]
    h[k] = idx
    idx += 1


# 在哈希表中查询某个数是否存在
def find(x: int):
    k = (x % n + n) % n
    i = h[k]
    while i != -1:
        if e[i] == x:
            return True
        i = ne[i]
    return False
```

2. 开放寻址法

```python
h = [0] * n
null = -10 ** 9


# 如果x在哈希表中，返回x的下标；如果x不在哈希表中，返回x应该插入的位置
def find(x: int):
    t = (x % n + n) % n
    while h[t] != null and h[t] != x:
        t += 1
        if t == n:
            t = 0
    return t
```

### 字符串哈希 —— 模板题 AcWing 841. 字符串哈希

核心思想：将字符串看成P进制数，P的经验值是131或13331，取这两个值的冲突概率低 小技巧：取模的数用2^64。

~~long存储，溢出的结果就是取模的结果~~，**Python 不考虑溢出，需要取模**。

```python
# h[k]存储字符串前k个字母的哈希值, p[k]存储 P^k mod 2^64
h, p, ma = [0] * n, [0] * n, 2 ** 64
# 初始化
p[0] = 1
for i in range(1, n + 1):
    h[i] = (h[i - 1] * P + str[i]) % ma
    p[i] = (p[i - 1] * P) % ma


# 计算子串 str[l ~ r] 的哈希值
def get(l, r):
    return h[r] - h[l - 1] * p[r - l + 1]  # 左移
```