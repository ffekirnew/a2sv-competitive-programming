class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        for i, items in enumerate(ingredients):
            for item in items:
                graph[item].append(recipes[i])
                in_degree[recipes[i]] += 1
        
        
        answer = []
        recipes = set(recipes)
        # use supplies for the bfs
        while supplies:
            curr_supply = supplies.pop()
            
            if curr_supply in recipes:
                answer.append(curr_supply)
            
            for output in graph[curr_supply]:
                in_degree[output] -= 1
                
                if not in_degree[output]:
                    supplies.append(output)
        
        return answer
                
        