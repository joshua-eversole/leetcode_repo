class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result = ""
        i = 0
        while i < len(num) - 2:
            if num[i] == num[i+1] and num[i] == num[i+2]:
                if result == "" or int(num[i]) > int(result[0]):
                    result = num[i:i+3]
            i+=1
        return result
