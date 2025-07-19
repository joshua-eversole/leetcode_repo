class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # Make a set of folder for quicker reads
        folder_set = set(folder)
        result = []

        # Run through each directory in the folder
        for directory in folder:
            # Add each directory to the result
            result.append(directory)
            # Run through the characters and check to see if substrings are in the set
            last_slash = 0
            for i, char in enumerate(directory):
                if char == '/':
                    # If it exists in the set, then pop it and move on to the next directory 
                    if directory[:i] in folder_set:
                        result.pop()
                        break
        
        return result


        