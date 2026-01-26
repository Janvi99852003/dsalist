class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #all subarrays of size k
        

        dq = deque()
        res = []

        for i in range(len(nums)):
            # remove out-of-window index
            if dq and dq[0] == i - k:
                dq.popleft()

            # remove smaller elements
            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            # window formed
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
