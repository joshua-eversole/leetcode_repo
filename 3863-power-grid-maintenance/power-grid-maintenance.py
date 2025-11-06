class Solution:
    # First thoughts: depth first search 
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # connections have two stations, if they're connected they form a power grid
        # query [1,x] return x if its online, smallest id in power grid if offline but reachable, and -1 if unreachable
        # IMPORTANT: it's not 0-based indexing
        res = []

        size = c+1

        parent = list(range(size)) # 2d list of all parents and children, used to create the connections. We start by making each parent equal to itself (important for Union Finda)

        # Union-Find method to see if we can get the correct path
        def find(x):
            # If we can, compress the path to make it easier in the future
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x
        
        # use union find on connected station to set id numbers for each station and connect them all in the parent map
        for a, b in connections:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
        
        next_node = [0]*size # c+1 array of the next station in sorted order
        comp_min = [0]*size # c+1 array of the smallest online station for each component

        last = {} # Tracks the last inserted node for each component

        for i in range(1, size):
            # use the find method to get the root of the component
            r = find(i)
            # if the parent doesn't exist, set it equal to i
            if comp_min[r] == 0:
                comp_min[r] = i
            # if it does exist, we have the parent (or -1)
            else:
                next_node[last[r]] = i
            last[r] = i
        
        offline = [False] * size # checks whether each station is still offline

        # Run through each query
        for t, x in queries:
            # Query 1
            if t == 1:
                if not offline[x]: 
                    res.append(x) # if it's online, no need to find the closest online value
                else:
                    r = find(x)
                    if comp_min[r]:  # Use the smallest online station (or -1 if there isn't one)
                        res.append(comp_min[r])
                    else:
                        res.append(-1)
            #Query 2
            else:
                if not offline[x]:
                    offline[x] = True
                    r = find(x)
                    if comp_min[r] == x: # If it was the smallest offline station, we need to update the grid
                        y = next_node[x] # move to the next smallest station
                        while y and offline[y]: #keep going until we have an online node
                            y = next_node[y]
                        comp_min[r] = y if y else 0 #update the smallest online station
        return res
                

            


