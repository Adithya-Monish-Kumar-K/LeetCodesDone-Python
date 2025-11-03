class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        prev_sequence = self.countAndSay(n - 1)
        result = []
        count = 1
        for i in range(1, len(prev_sequence)):
            if prev_sequence[i] == prev_sequence[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(prev_sequence[i - 1])
                count = 1
        result.append(str(count))
        result.append(prev_sequence[-1])
        return ''.join(result)