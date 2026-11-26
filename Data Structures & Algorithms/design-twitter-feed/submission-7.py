class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.recentTweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        newTweet = (self.timestamp, tweetId)
        self.tweets[userId].append(newTweet)
        heapq.heappush(self.recentTweets[userId], newTweet)
        if len(self.recentTweets[userId]) > 10:
            heapq.heappop(self.recentTweets[userId])

    def getNewsFeed(self, userId: int) -> List[int]:
        userTweets = self.recentTweets[userId]
        tweets = userTweets[:]
        for followee in self.followers[userId]:
            for tweet in self.recentTweets[followee]:
                heapq.heappush(tweets, tweet)
                if len(tweets) > 10:
                    heapq.heappop(tweets)

        res = []
        while tweets:
            res.append(heapq.heappop(tweets)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
