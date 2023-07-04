class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # backtracking?

        res = []
        num_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def back_track(i, cur_str):
            if len(cur_str) == len(digits):
                res.append(cur_str)
                return
            # digits = "123"
            for letter in num_letters[digits[i]]:
                back_track(i + 1, cur_str + letter)

        if digits:
            back_track(0, "")

        return res
