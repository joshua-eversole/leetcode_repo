class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        hash_map = {} # key: character from pattern, value: part of s we're trying to match it to
        reverse_hash = {} # key and value are reversed from hash_map

        def backtracking(pattern_index, s_index):

            # Base case: if we've processed the entire pattern, check if we solved it
            if pattern_index == len(pattern):
                if s_index == len(s):
                    return True
                else:
                    return False

            # Get the character we're working with
            char = pattern[pattern_index]

            # If the character from the pattern is already in the hash map
            if char in hash_map:
                map_str = hash_map[char]
                str_len = len(map_str)

                # Check if the current part of s matches the mapped string
                if (s_index + str_len) <= len(s) and s[s_index:s_index + str_len] == map_str:
                    if backtracking(pattern_index + 1, s_index + str_len):
                        return True
                        
                else:
                    return False

            # Otherwise, we have to find a suitible camp
            else:
                for i in range(s_index, len(s)):
                    substring = s[s_index:i + 1]

                    # Check if this substring is already mapped to another pattern character
                    if substring in reverse_hash:
                        continue
                    hash_map[char] = substring
                    reverse_hash[substring] = char

                    # It's recursion
                    if backtracking(pattern_index + 1, s_index + len(substring)):
                        return True

                    # If i didn't find a solution, backtrack and remove it
                    del hash_map[char]
                    del reverse_hash[substring]

            return False

        return backtracking(0, 0)