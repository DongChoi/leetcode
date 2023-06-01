"""reverse the numbers but keep the - or +, if outside signed 32bit number, return 0"""


class Solution:
    def reverse(self, x: int) -> int:
        string = str(x)
        pos_neg = "neg" if string[0] == "-" else "pos"

        if pos_neg == "neg":
            string = string[1:]
            reversed_string = string[::-1]
            string = int(reversed_string) * -1
        else:
            reversed_string = string[::-1]
            string = int(reversed_string)
        if string < -2147483648 or string > 2147483647:
            return 0
        else:
            return string
