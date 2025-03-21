class Solution:
    # 3/21: 
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        supplies_set = set(supplies) # Change it into a set for faster lookup
        visited = {} # Key: recipe name, value: can we make it
        all_recipes = [] # Final result
        
        # Make a hash and fill it with recipies and their ingredients
        recipe_hash = {}
        for i, recipe in enumerate(recipes):
            recipe_hash[recipe] = ingredients[i]

        # Inputs recipie name, returns bool of whether we can make the recipe currently
        def canMakeRecipe(recipe):
            # Base case: If we've already visited it, return the pre-found value

            if recipe in supplies_set:
                return True
            if recipe in visited:
                return visited[recipe]
            visited[recipe] = False
            
            if recipe not in recipe_hash:
                return False  # Recipe not found
            # 
            for ingredient in recipe_hash[recipe]:
                if ingredient not in supplies_set:
                    # If we can make the ingredient, then add it to the supply set
                    if canMakeRecipe(ingredient):
                        supplies_set.add(ingredient)
                    else:
                        return False

            # If we can make all ingredients, add it to the result
            visited[recipe] = True
            all_recipes.append(recipe)
            return visited[recipe]
            
        # Run through each recipe to try it
        for recipe in recipes:
            dummy_var = canMakeRecipe(recipe)
        
        return all_recipes


            

            
        







        