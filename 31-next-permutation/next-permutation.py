class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        ind1 = -1

        # Step 1: find first decreasing index from right
        for i in range(n - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                ind1 = i - 1
                break

        # Step 2: if no such index, reverse whole array
        if ind1 == -1:
            nums.reverse()
            return

        # Step 3: find element just larger than nums[ind1]
        for i in range(n - 1, ind1, -1):
            if nums[i] > nums[ind1]:
                nums[i], nums[ind1] = nums[ind1], nums[i]
                break

        # Step 4: reverse remaining part
        nums[ind1 + 1:] = reversed(nums[ind1 + 1:])
