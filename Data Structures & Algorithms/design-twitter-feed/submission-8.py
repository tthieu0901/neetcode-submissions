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
                tweets.append(tweet)

        return [tweetId for time, tweetId in heapq.nlargest(10, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
