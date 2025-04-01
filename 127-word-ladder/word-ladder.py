from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Initialize variables and make the word set for O(1) lookup
        all_letters = "abcdefghijklmnopqrstuvwxyz"
        word_set = set(wordList)

        # If endWord is not in wordlist, automatically return 0
        if endWord not in word_set:
            return 0

        # Create the queue for BFS and add beginword to it
        queue = deque()
        queue.append((beginWord, 1))

        while queue:
            word, step = queue.popleft() 
            
            # Run through every character in the word
            for i, char in enumerate(word):
                # Run through every replacement character
                for letter in range(26):
                    new_letter = all_letters[letter]
                    
                    # If it's the same letter, skip
                    if new_letter == char:
                        continue
                    
                    # Make the new word and check its validity
                    new_word = word[:i] + new_letter + word[i+1:]
                    if new_word in word_set:
                        
                        # If we found the endWord, return the step count
                        if new_word == endWord:
                            return step + 1
                        
                        # If it's a word, add it to the queue
                        queue.append((new_word, step + 1))
                        
                        # Remove the old word from word_set to avoid looping
                        word_set.remove(new_word)

        # If there's no way to get to the endWord, return 0
        return 0
