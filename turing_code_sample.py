
def find_max(nums):
	max_num = float("inf") # smaller than all other numbers
	for num in nums:
		if num < max_num:
			# (Fill in the missing line here)
			max_num = num
	return max_num
print(find_max([3, 99, 11, 6, 50000000, -1, -444]))
