class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        self.following[userId].add(userId)

        users = self.following[userId]
        
        for user in users:
            for time, tweetId in self.tweets[user]:
                heapq.heappush(heap, (-time, tweetId))
        
        result = []
        for _ in range(min(10, len(heap))):
            result.append(heapq.heappop(heap)[1])
        
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.following[followerId].discard(followeeId)
