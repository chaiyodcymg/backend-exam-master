"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number can not less than 0"
        if number > 10000000:
            return " positive number rang from 0 to 10_000_000"
        if number == 0:
            return "ศูนย์"
        thai_digits = ['', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
        thai_units = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน' ]
        thai_units_length = len(thai_units) - 1
        words = []
        unit = 0
        while number > 0:
            digit = number % 10
            if digit != 0:
                if digit%6 == 1 and unit == 0 and number > 1 and digit != 7:
                    words.append("เอ็ด")
                elif digit%6 == 2 and unit == 1:
                    words.append("ยี่" + thai_units[unit])
                elif digit%6 == 1 and unit == 1:
                    words.append("สิบ")
                elif digit%6 == 1 and unit == 7 and unit > thai_units_length:
                    words.append("สิบ"+ thai_units[thai_units_length])
                else:
                    if unit > thai_units_length:
                        unit = 1
                    words.append(thai_digits[digit] + thai_units[unit])
            number //= 10
            unit += 1
        words.reverse()
        return ''.join(words)
