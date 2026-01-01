class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = len(digits) - 1
        while plus >= 0:
            if digits[plus] >= 9:
                digits[plus] = 0
                plus -= 1
            else:
                digits[plus] += 1
                return digits

        return [1] + digits
            