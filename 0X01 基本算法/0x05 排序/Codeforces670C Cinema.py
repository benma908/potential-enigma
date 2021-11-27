# 离散化 https://codeforces.com/problemset/problem/670/C
import bisect


def discrete(a):
    a.sort()
    res = [0] * len(a)
    j = 1
    for i in range(1, len(a)):
        if i == 1 or a[i] != a[i - 1]:
            res[j] = a[i]
            j += 1
    return [x for x in res if x]


def find(a, x):
    return bisect.bisect_left(a, x)


if __name__ == '__main__':
    n = int(input())
    ppl = [0] + [int(x) for x in input().split(" ")]

    m = int(input())
    lan = [0] + [int(x) for x in input().split(" ")]
    subs = [0] + [int(x) for x in input().split(" ")]
    a = [0] + ppl[1:] + lan[1:] + subs[1:]
    s = discrete(a)

    ans = [0] * len(s)
    for i in range(1, n + 1):
        ans[find(s, ppl[i])] += 1
    res, tmp1, tmp2 = -1, -1, -1
    for i in range(1, m + 1):
        l, su = ans[find(s, lan[i])], ans[find(s, subs[i])]
        if (l > tmp1) or (l == tmp1 and su > tmp2):
            res, tmp1, tmp2 = i, l, su
    print(res)
