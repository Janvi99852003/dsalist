class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = arr[1] - arr[0]
        ans = []

        for i in range(1, len(arr)):
            diff = arr[i] - arr[i - 1]

            if diff < res:
                res = diff
                ans = [[arr[i - 1], arr[i]]]
            elif diff == res:
                ans.append([arr[i - 1], arr[i]])

        return ans
