class Solution:
    # 4/16
    def compress(self, chars: List[str]) -> int:
        # Two pointers, one follows where I'm putting the values, and two follows where I'm tracking
        i, j = 0, 0
        while i < len(chars):
            char = chars[i]
            print(f"new char: {char}")
            char_count = 0
            while i < len(chars) and char == chars[i]:
                i += 1
                char_count += 1
            print(f"char {char} was found {char_count} times")
            chars[j] = char
            # Now we have i at the end of the repeating chars. move j up by one
            j += 1
            if char_count > 1:
                # NOTE: I didn't think of converting it into a string first, that was definitely the easiest way to do this part of the question. 
                for digit in str(char_count):
                    chars[j] = digit 
                    j += 1
        return j

