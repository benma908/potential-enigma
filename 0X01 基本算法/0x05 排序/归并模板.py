# 模板 https://www.acwing.com/problem/content/787/
n = int(input())
a = list(map(int, input().split()))
tmp = [0] * len(a)


def merge_sort(a, l, r):
    if l >= r:
        return

    mid = (l + r) >> 1
    k, i, j = 0, l, mid + 1
    merge_sort(a, l, mid)
    merge_sort(a, mid + 1, r)
    while i <= mid and j <= r:
        if a[i] <= a[j]:
            tmp[k] = a[i]
            i += 1
        else:
            tmp[k] = a[j]
            j += 1
        k += 1
    while i <= mid:
        tmp[k] = a[i]
        k += 1
        i += 1
    while j <= r:
        tmp[k] = a[j]
        k += 1
        j += 1
    j = 0
    for i in range(l, r + 1):
        a[i] = tmp[j]
        j += 1


if __name__ == '__main__':
    merge_sort(a, 0, len(a) - 1)
    print(' '.join(map(str, a)))
