# .sort() = 오름차순
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort()

print(nums)

# .sort(reverse = True) = 내림차순
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.sort(reverse=True)

print(nums)

# .reverse()
nums = [33, 22, 11, 77, 55, 66, 99, 88]
nums.reverse()

print(nums)

# .remove(value) // del x[]
nums = [33, 22, 11, 77, 55, 66, 99, 88, 11]
nums.remove(11)

print(nums)

# .index(value) = 값위치
nums = [33, 22, 11, 77, 55, 66, 99, 88]
print(nums.index(11))

# .extend(value)
nums1 = [33, 22, 11, 77]
nums2 = [55, 66, 99, 88]
nums1.extend(nums2)
print(nums1)

# .count(value)
nums = [33, 22, 11, 77, 55, 66, 99, 88, 11]
print(nums.count(11))

# .pop(i), .pop()
nums = [33, 22, 11, 77, 55, 66, 99, 88, 11]
nums.pop(0)
print(nums)

# len()
nums = [33, 22, 11, 77, 55, 66, 99, 88, 11]
print(len(nums))

# sorted(value), sorted(value, reverse = True)
nums = [33, 22, 11, 77, 55, 66, 99, 88, 11]
print(sorted(nums))