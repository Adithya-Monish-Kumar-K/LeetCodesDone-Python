class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        bt = [
            "", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
            "Seventeen", "Eighteen", "Nineteen"
        ]
        tens = [
            "", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]
        thousands = ["", "Thousand", "Million", "Billion"]
        def func(n):
            if n == 0:
                return ""
            elif n < 20:
                return bt[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + func(n % 10)
            else:
                return bt[n // 100] + " Hundred " + func(n % 100)
        r = ""
        for i in range(len(thousands)):
            if num % 1000 != 0:
                r = func(num % 1000) + thousands[i] + " " + r
            num //= 1000
        return r.strip()