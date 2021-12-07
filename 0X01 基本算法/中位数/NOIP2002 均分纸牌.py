n = int(input())
nums = list(map(int, input().split()))
run = sum(nums) // n
cnt = 0
for i in range(n - 1):
    if nums[i] != run:
        nums[i + 1] += nums[i] - run
        nums[i] = run
        cnt += 1
print(cnt)
