class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # dfs to find smallest lex character for each character

        # Start by building the connecting graph
        adj = defaultdict(list)

        for a, b in zip(s1, s2):
            # Have them both list each other as a node
            adj[a].append(b)
            adj[b].append(a)
        
        # DFS: input the char and the visited graph, output the min char
        def dfs(char, visited):
            visited.add(char)
            min_char = char
            for neighbor in adj[char]:
                if neighbor not in visited:
                    candidate = dfs(neighbor, visited)
                    min_char = min(min_char, candidate)
            return min_char
        
        result = []
        for char in baseStr:
            visited = set()
            result.append(dfs(char, visited))
        
        return ''.join(result)