
def find_min(nums):
	min_num = float("inf") # smaller than all other numbers
	for num in nums:
		if num < min_num:
			# (Fill in the missing line here)
			min_num = num
	return min_num
print(find_min([3, 99, 11, 6, 50000000, -1, -444]))
