
def insert_array(nums, insert_num):
    nums_len = len(nums)
    mid = nums_len // 2
    new_list = nums[0: mid] + [insert_num] + nums[mid:]
    return new_list

