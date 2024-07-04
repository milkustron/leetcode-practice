class Solution:
    def searchInsert(nums, target) -> int:
        if len(nums) == 1:
            if target <= nums[0]:
                return 0  
            else: return 1

        nums_test = nums
        index_start = 0
        index_stop = len(nums_test)-1
        while index_stop - index_start != 1:
            if target < nums_test[int(len(nums_test)/2)]:
                nums_test = nums_test[:int(len(nums_test)/2)]
                index_stop = int(index_stop - (index_stop-index_start)/2)
            else: 
                nums_test = nums_test[int(len(nums_test)/2):]
                index_start = int(index_start + (index_stop-index_start)/2)


        if target > nums[index_stop]:
            return index_stop + 1
        elif target <= nums[index_start]:
            return index_start
        else: return index_stop