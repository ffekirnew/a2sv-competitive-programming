class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        
        stack = []
        
        for dir in path:
            if dir == "..":
                if stack:
                    stack.pop()
            elif dir != "." and dir != "":
                stack.append(dir)

        return "/" + "/".join(stack)
                
                
            
        