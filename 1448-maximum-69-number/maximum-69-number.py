class Solution:
    def maximum69Number (self, num: int) -> int:
        # First thoughts, num is only positive, so just replace the first 6 we see with a 9
        num_str = str(num)
        result = ""
        seen_six = False
        for i, digit in enumerate(num_str):
            if not seen_six and digit == '6':
                result += '9'
                seen_six = True
            else:
                result += digit 
        
        return int(result)