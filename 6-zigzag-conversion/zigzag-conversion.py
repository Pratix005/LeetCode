class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [""] * numRows
        row = 0
        down = True

        for ch in s:
            rows[row] += ch

            if row == numRows - 1:
                down = False
            elif row == 0:
                down = True

            if down:
                row += 1
            else:
                row -= 1

        return "".join(rows)