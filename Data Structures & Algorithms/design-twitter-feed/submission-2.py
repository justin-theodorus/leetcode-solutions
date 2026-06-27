from collections import deque

class Twitter:

    def __init__(self):
        self.userPosts = defaultdict(list)
        # user -> (time, tweetId)
        self.adjList = defaultdict(set) 
        # to model connectivity between users, followers
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        # tweetId is unique
        # order posts
        self.userPosts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # get 10 MOST recent tweets by the user and all its followers
        # BFS
        q = deque([userId]) # userId
        minHeap = []
        visited = set()
        visited.add(userId)

        while q:
            for i in range(len(q)):
                uid = q.popleft()
                # process posts
                for time, tweetId in self.userPosts[uid]:
                    heapq.heappush(minHeap, (time, tweetId))

                    if len(minHeap) > 10:
                        heapq.heappop(minHeap)
                # process followers
                for neighId in list(self.adjList[uid]):
                    if neighId not in visited:
                        visited.add(neighId)
                        q.append(neighId)

        ans = []
        while minHeap:
            ans.append(heapq.heappop(minHeap)[1])
        return ans[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        # followerId follows followeeId
        self.adjList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # followerId unfollows followeeId
        self.adjList[followerId].discard(followeeId)
"""
- post tweets
- follow
- unfollow
- view 10 MOST recent

Use a graph to model relationships between users
Traverse the graph when getNewsFeed is called
    Maintaining a min heap of size 10 at most (ordered by time added)
    If size > 10, we pop from the min heap
"""