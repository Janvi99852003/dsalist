class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        start=0
        end=0
        last={}
        t=[]
        for i,ch in enumerate(s):
            last[ch]=i
        for i,ch in enumerate(s):
            end=max(end,last[ch])
            if i==end:
                t.append(end-start+1)
                start=i+1

        return t
