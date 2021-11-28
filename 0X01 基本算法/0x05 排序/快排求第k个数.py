# 快排求解第 k 个次序数 https://www.acwing.com/activity/content/problem/content/820/
def quick(a, l, r, k):
    if l >= r: return a[l]
    x, i, j = a[(l + r) >> 1], l - 1, r + 1
    while i < j:
        while True:
            i += 1
            if a[i] >= x:
                break
        while True:
            j -= 1
            if a[j] <= x:
                break
        if i < j:
            a[i], a[j] = a[j], a[i]
    sl = j - l + 1
    if sl >= k:
        return quick(a, l, j, k)
    return quick(a, j + 1, r, k - sl)


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    num = quick(a, 0, len(a) - 1, k)
    print(num)
