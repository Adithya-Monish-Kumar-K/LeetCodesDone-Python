class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h=len(citations)
        citations.sort(reverse=True)
        for i in range(h):
            if citations[i] <i+1:
                return i
        return h