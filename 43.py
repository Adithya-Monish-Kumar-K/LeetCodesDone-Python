class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        len1, len2 = len(num1), len(num2)
        result = [0] * (len1 + len2)
        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                s= mul + result[i + j + 1]
                result[i + j + 1] = s% 10
                result[i + j] += s// 10
        start_index = 0
        while start_index < len(result) and result[start_index] == 0:
            start_index += 1
        return ''.join(map(str, result[start_index:])) if start_index < len(result) else '0'