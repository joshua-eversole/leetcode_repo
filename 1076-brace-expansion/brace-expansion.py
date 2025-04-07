from typing import List

class Solution:
    def expand(self, s: str) -> List[str]:
        # Init variables
        parts = []
        current_part = ""
        in_bracket = False
        current_options = []

        # First, we break s into a variable type we can work with
        for char in s:
            if char == '{':
                in_bracket = True
                if current_part:
                    parts.append(current_part)
                    current_part = ""
                current_options = []
            elif char == '}':
                in_bracket = False
                if current_part:
                    current_options.append(current_part)
                    current_part = ""
                if current_options:
                    parts.append(sorted(current_options))
                current_options = []
            elif char == ',':
                if in_bracket:
                    if current_part:
                        current_options.append(current_part)
                        current_part = ""
            else:
                if not in_bracket:
                    current_part += char
                else:
                    current_part += char

        # If there's still something left, add it
        if current_part:
            parts.append(current_part)

        result = []

        # Now we backtyrack
        def backtrack(index, current_string):
            if index == len(parts):
                result.append(current_string)
                return

            options = parts[index]
            # If options is a list, then we run through it and backtrack
            if isinstance(options, list):
                for option in options:
                    backtrack(index + 1, current_string + option)
            # If it's a string, just add that shit and keep going
            else:
                backtrack(index + 1, current_string + options)

        backtrack(0, "")
        # Sort it, since it's not going to increase the runtime at all
        return sorted(result)