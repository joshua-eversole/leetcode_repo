class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map = {}
        reverse_hash_map = {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i, char in enumerate(pattern):
            word = words[i]

            # If it's in the hashmap, just make sure it matches
            if char in hash_map:
                mapped_word = hash_map[char]
                if word != mapped_word:
                    return False 

            # If it's not in the hashmap, make sure it isn't already used before adding it
            else:
                if word in reverse_hash_map:
                    mapped_char = reverse_hash_map[word]
                    if mapped_char != char:
                        return False  
                else:
                    hash_map[char] = word
                    reverse_hash_map[word] = char

        return True