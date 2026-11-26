class Twitter:

    def __init__(self):
        self.followers = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp -= 1
        newTweet = (self.timestamp, tweetId)
        self.tweets[userId].append(newTweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        self.followers[userId].add(userId)
        for followee in self.followers[userId]:
            followeeTweets = self.tweets[followee]
            if followeeTweets:
                idx = len(followeeTweets) - 1
                time, tweetId = followeeTweets[idx]
                mostRecentTweet = (time, tweetId, followee, idx)
                heapq.heappush(tweets, mostRecentTweet)

        res = []
        while tweets and len(res) < 10:
            _, tweetId, followee, idx = heapq.heappop(tweets)
            res.append(tweetId)

            if idx > 0:
                nextRecentTweet = self.tweets[followee][idx - 1]
                time, next_tweetId = nextRecentTweet
                nextTweet = (time, next_tweetId, followee, idx - 1)
                heapq.heappush(tweets, nextTweet)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
