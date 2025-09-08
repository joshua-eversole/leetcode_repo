class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        def hasZero(num):
            while num >= 10:
                if num % 10 == 0:
                    return True
                num = num//10
            return False

        a = n//2
        b = n - a
        while hasZero(a) or hasZero(b):
            a -= 1
            b += 1
        return [a,b]


    