class Solution:
    def calculate(self, s: str) -> int:
        st = []
        cn = 0
        cs = 1
        result = 0
        for c in s:
            if c.isdigit():
                cn = cn * 10 + int(c)
            elif c == "+":
                result += cs * cn
                cn = 0
                cs = 1
            elif c == "-":
                result += cs * cn
                cn = 0
                cs = -1
            elif c == "(":
                st.append(result)
                st.append(cs)
                result = 0
                cs = 1
            elif c == ")":
                result += cs * cn
                result *= st.pop()
                result += st.pop()
                cn = 0

        return result + cs * cn