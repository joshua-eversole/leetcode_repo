class Solution:
    def maximum69Number (self, num: int) -> int:
        # First thoughts, num is only positive, so just replace the first 6 we see with a 9
        num_str = str(num) # Convert num to a string (so we can look at each digit individually)
        result = "" # Make a new empty string
        seen_six = False # Make a new true/false value to keep track of if we've already changed a six to a nine
        for i, digit in enumerate(num_str): # Go through each digit in the string (i is the order of the digit, digit is the actual number (in string form))
            if not seen_six and digit == '6': # If the number is a six and we haven't changed a six yet
                result += '9' # Add a 9 instead of the 6 digit
                seen_six = True # set seen_six to true so we don't do this multiple times
            else: #if the number isn't a six or if we have already changed a 6
                result += digit # just add the normal digit
        
        return int(result) #Now convert the result back to a digit and return it