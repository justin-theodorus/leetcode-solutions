class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            stack.append(asteroid)
            while (len(stack) >= 2 and stack[-2] > 0 and stack[-1] < 0):
                if (abs(stack[-1]) == abs(stack[-2])):
                    stack.pop()
                    stack.pop()
                elif (abs(stack[-1]) > abs(stack[-2])):
                    last = stack.pop()
                    stack.pop()
                    stack.append(last)
                else:
                    stack.pop()
        return stack

