class Logger:

    def __init__(self):
        self.next = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.next:
            #print(f"{message} in hash")
            if timestamp < self.next[message]:
                return False
        #print(f"{message} inserted at {timestamp}.")
        self.next[message] = timestamp + 10
        #print(f"  -hash of {message} is {self.next[message]}.")
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)