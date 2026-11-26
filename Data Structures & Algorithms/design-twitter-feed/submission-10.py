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

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        self.followers[userId].add(userId)
        for followee in self.followers[userId]:
            followeeTweets = self.tweets[followee]
            for i in range(len(followeeTweets) -1, max(-1, len(followeeTweets) - 1 - 10), -1):
                tweets.append(followeeTweets[i])

        return [tweetId for time, tweetId in heapq.nlargest(10, tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)
