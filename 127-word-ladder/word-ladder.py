from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Initialize variables and make the word set for O(1) lookup
        all_letters = "abcdefghijklmnopqrstuvwxyz"
        word_set = set(wordList)

        # If endWord is not in wordlist, automatically return 0
        if endWord not in word_set:
            print(f"{endWord} not in word list. Returning 0.")
            return 0

        # Create the queue for BFS and add beginword to it
        queue = deque()
        queue.append((beginWord, 1))
        print(f"Starting BFS with: {beginWord}")

        while queue:
            word, step = queue.popleft()  # Changed pop() to popleft() for correct BFS
            print(f"Current word: {word}, Steps: {step}")
            
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
                        print(f"Found valid transformation: {word} -> {new_word}")
                        
                        # If we found the endWord, return the step count
                        if new_word == endWord:
                            print(f"Reached endWord {endWord} in {step + 1} steps.")
                            return step + 1
                        
                        # If it's a word, add it to the queue
                        queue.append((new_word, step + 1))
                        
                        # Remove the old word from word_set to avoid looping
                        word_set.remove(new_word)
                        print(f"Removed {new_word} from word set")

        # If there's no way to get to the endWord, return 0
        print("No transformation found. Returning 0.")
        return 0
