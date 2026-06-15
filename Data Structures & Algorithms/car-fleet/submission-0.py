class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))
        pos_speed.sort(key = lambda x: x[0])
        time = []
        for pos, s in pos_speed:
            time.append((target - pos) / s)
        ans = []
        for t in time:
            while ans and t >= ans[-1]:
                ans.pop()
            ans.append(t)
        return len(ans)
"""
target = 10, position = [1,4], speed = [3,2]

time taken for car 1 = 3 hours (10 - 1 / 3)
time taken for car 2 = 3 hours (10 - 4 / 2)

target = 10, position = [4,1,0,7,8,5], speed = [2,2,1,1,1,5]
time taken for car 1 = 3 hours (10 - 4 / 2)
time taken for car 2 = 4.5 hours (10 - 1 / 2)
time taken for car 3 = 10 hours (10 - 0 / 1)
time taken for car 4 = 3 hours (10 - 7 / 1)
time taken for car 5 = 2 hours (10 - 8 / 1)
time taken for car 6 = 3 hours (stuck behind car 3, should've been 1 hour)

[(0,1), (1,2), (4,2), (5,5), (7,1), (8,1)]
[10, 4.5, 3, 1, 3, 2] -> [10, 4.5, 3, 2] 
time must be decreasing, can merge once we see increasing time
"""