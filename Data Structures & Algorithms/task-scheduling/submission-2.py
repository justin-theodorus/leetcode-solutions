class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxHeap = [-cnt for cnt in taskCount.values()]
        heapq.heapify(maxHeap)
        t = 0

        # cooldown queue
        q = deque() # [count, idleTime]
        while maxHeap or q:
            t += 1

            if not maxHeap:
                # fast forward
                t = q[0][1]
            else:
                # decrease cnt by 1
                cnt = 1 + heapq.heappop(maxHeap)
                # put to cooldown queue if cnt not 0
                if cnt:
                    q.append([cnt, t + n])
            
            if q and q[0][1] == t:
                # push tasks from queue that is no longer in cooldown
                heapq.heappush(maxHeap, q.popleft()[0])
        return t

"""
[A,A,B], n = 2

A B Idle A

[A,A,A], n = 1 -> 5
[A,A,A], n = 2 -> 7
[A,A,A], n = 3 -> 9

We can track time for a single character using a PQ
We can only use that character once the cooldown reaches 0
We remove from the PQ once there are no more characters left

t = 6
n = 2
A: 0
B: 0
[]
A B Idle A B Idle A

["A","A","A","A","A","A","B","C","D","E","F","G"]
n=1

"""