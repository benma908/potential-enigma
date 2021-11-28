# 模板 https://www.acwing.com/problem/content/785/
def quick_sort(a, l, r):
    if l >= r:
        return
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
    quick_sort(a, l, j)
    quick_sort(a, j + 1, r)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    quick_sort(a, 0, len(a) - 1)
    print(' '.join(map(str, a)))
