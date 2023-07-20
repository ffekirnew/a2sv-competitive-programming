class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        
        def sign(n: int) -> bool:
            """Return 'right' for positive, 'left' for negatives"""
            return 'right' if n > 0 else 'left'
        
        for asteroid in asteroids:
            while stack and sign(stack[-1]) == 'right' and sign(asteroid) == 'left' and abs(asteroid) > abs(stack[-1]):
                stack.pop()
            
            if stack and sign(stack[-1]) == 'right' and sign(asteroid) == 'left' and abs(asteroid) == abs(stack[-1]):
                stack.pop()
                continue
            
            if not stack or sign(stack[-1]) == sign(asteroid) or sign(stack[-1]) == 'left':
                stack.append(asteroid)
        
        return stack
                
        