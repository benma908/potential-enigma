# 归并求逆序对， https://www.acwing.com/activity/content/problem/content/822/
n = int(input())
a = list(map(int, input().split()))
tmp = [0] * len(a)


def merge_sort(q, l, r):
    if l >= r: return 0
    mid = l + r >> 1
    res = merge_sort(q, l, mid) + merge_sort(q, mid + 1, r)
    k, i, j = 0, l, mid + 1
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            tmp[k] = q[i]
            i += 1
        else:
            tmp[k] = q[j]
            j += 1
            res += mid - i + 1
        k += 1
    # tmp[k:] = q[i:mid+ 1]
    while i <= mid:
        tmp[k] = q[i]
        k += 1
        i += 1
    # print(tmp)
    # tmp[k+mid-i+1:] = q[j:r+ 1]
    # print(tmp)
    while j <= r:
        tmp[k] = q[j]
        k += 1
        j += 1
    j = 0
    for i in range(l, r + 1):
        # print(j, len(tmp))
        q[i] = tmp[j]
        j += 1
    return res


if __name__ == '__main__':
    print(merge_sort(a, 0, n - 1))
