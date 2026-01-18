class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        c=0
        lmax,rmax=0,0
        while l<r:
            lmax=max(lmax,height[l])
            rmax=max(rmax,height[r])
            if lmax<rmax: #lmax is boundary
               c=c+(lmax-height[l])
               l+=1
            else:
                c=c+(rmax-height[r])
                r-=1
        return c
