class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()

                if not len(stack):
                    break

                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]-height[top])

                volum += distance * waters

            stack.append(i)

        return 0