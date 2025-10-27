class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beam_count = 0
        last_row = 0
        for i in range(len(bank)):
            line = bank[i]
            devices = 0
            for i in range(len(line)):
                if line[i] == '1':
                    devices += 1
            if devices != 0:
                beam_count += devices * last_row
                last_row = devices
                print(f"devices is now {last_row}")
        
        return beam_count



        