from typing import List

class Solution:
    def __init__(self):
        # Keep track of visited courses and courses in current path
        self.visited = set()
        self.path = set()
        self.graph = {}

    def dfs(self, course: int) -> bool:
        # Base case: If it's in our path, we hit a cycle. Return false
        if course in self.path:
            return False 
        
        # If we've already visited this, we know there's no cycle. Return true
        if course in self.visited:
            return True 
        
        self.path.add(course)

        # Run through every prereq and check to make sure they're good
        for prereq in self.graph[course]:
            if not self.dfs(prereq):
                return False
            
        # Remove the course from the path and add it to the visited
        self.path.remove(course)
        self.visited.add(course)

        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list with all courses initialized
        self.graph = {i: [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            self.graph[course].append(prereq)
        
        # Check each course
        for course in range(numCourses):
            if not self.dfs(course):
                return False

        return True
