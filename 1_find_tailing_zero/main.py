"""
เขียนโปรแกรมหาจำนวนเลข 0 ที่ออยู่ติดกันหลังสุดของค่า factorial โดยห้ามใช้ function from math

[Input]
number: as an integer

[Output]
count: count of tailing zero as an integer

[Example 1]
input = 7
output = 1

[Example 2]
input = -10
output = number can not be negative
"""


class Solution:

    def find_tailing_zeroes(self, number: int) -> int | str:
        if number < 0:
            return "number can not be negative"
        fac = 1
        result = 0
        for index in range(2, number+1 , 1):
             fac *= index
        fac = str(fac)
        for index in range(len(fac)- 1, -1, -1):
            if result > 0 and fac[index] != "0":
                return result
            if (fac[index] == "0" and index == len(fac)-1) or (fac[index] == "0" and index != len(fac)-1):
                result += 1
        return result