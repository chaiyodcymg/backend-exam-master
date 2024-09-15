"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number == 0 or number > 3999:
            return "roman number rang from 1 to 3999"
        roman_num = ""
        digits_arr = [ 
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        roman_arr = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        for index in range(len(digits_arr)):
            while number >= digits_arr[index]:
                roman_num += roman_arr[index]
                number -= digits_arr[index]
        return roman_num