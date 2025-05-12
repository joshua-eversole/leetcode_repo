class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digit_set = set(digits)
        freq = Counter(digits)
        print(freq)
        results = []

        #The first number can't be 0
        #The third number must be even
        # You can't repeat numbers
        # Because they are 3-digit numbers, we can go through 100 - 998 and check
        for one in range(1, 10):
            if one in digit_set:
                freq[one] -= 1
                for two in range(0, 10):
                    if two in digit_set and freq[two] > 0:
                        freq[two] -= 1
                        for three in range(0, 10, 2):
                            if one == 2 and two == 9 and three == 0:
                                print("290")
                            if three in digit_set and freq[three] > 0:
                                num = one * 100 + two * 10 + three
                                results.append(num)
                        freq[two] += 1
                freq[one] += 1
        
        return results


