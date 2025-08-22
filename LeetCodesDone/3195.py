class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        srow = 1000
        erow = 0
        scolumn = 1000
        ecolumn = 0
        temp=0
        for i in grid:
            temp2 = 0
            temp+=1
            for j in i:
                temp2+=1
                if (j == 1):
                    scolumn = min(temp2, scolumn)
                    ecolumn = max(temp2, ecolumn)
                    srow = min(temp, srow)
                    erow = max(temp, erow)
        c = ecolumn - scolumn + 1
        r = erow - srow + 1
        if (ecolumn == scolumn):
            c = 1
        if (erow == srow):
            r = 1
        size = c*r
        return size