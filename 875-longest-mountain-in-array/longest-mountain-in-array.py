class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans = 0

        for i in range(1, n - 1):
            # check peak
            if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
                l = i
                r = i

                # move left (increasing)
                while l > 0 and arr[l - 1] < arr[l]:
                    l -= 1

                # move right (decreasing)
                while r < n - 1 and arr[r] > arr[r + 1]:
                    r += 1

                ans = max(ans, r - l + 1)

        return ans
