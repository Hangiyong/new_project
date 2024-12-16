# list slice -> 비파괴적
nums = [33, 22, 11, 77, 55, 66, 99, 88]
print(nums[2:6])

print(nums[-2:-6])
print(nums[-6:-2])

print(nums[::1])

print(nums[::-1])