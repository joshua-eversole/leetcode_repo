class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        len_one, len_two = len(num1), len(num2)
        result = [0]* (len_one + len_two)

        for i_one in range(len_one - 1, -1, -1):
            dig_one = int(num1[i_one])
            # multiply dig_one digit by each digit in num2
            for i_two in range(len_two - 1, -1, -1):
                position = i_one + i_two
                dig_two = int(num2[i_two])

                product = dig_one * dig_two + result[position + 1]
                # Add the two possible digits to the result, adding the tens digit one position up
                result[position + 1] = product % 10
                result[position] += product//10
        
        i = 0
        while i < len(result) and result[i] == 0:
            i += 1
        result = result[i:]
        return "".join(map(str, result))


        

        