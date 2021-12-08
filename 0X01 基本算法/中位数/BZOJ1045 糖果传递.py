n = int(input())
nums = [0] * n
for i in range(n):
    nums[i] = int(input())
avg = sum(nums) // n
c = [0] * (n + 1)
c[0] = 0
for i in range(1, n + 1):
    c[i] = c[i - 1] + nums[i - 1] - avg
c[1:] = sorted(c[1:])
b1 = c[n + 1 >> 1]
ans = 0
for i in range(1, n + 1):
    if (b1 - c[i]) > 0:
        ans += b1 - c[i]
    else:
        ans += c[i] - b1
print(ans)
