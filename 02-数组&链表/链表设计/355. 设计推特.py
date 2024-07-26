"""
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 条推文。10

实现 类：Twitter

Twitter() 初始化简易版推特对象
void postTweet(int userId, int tweetId) 根据给定的 和 创建一条新推文。每次调用此函数都会使用一个不同的 。tweetIduserIdtweetId
List<Integer> getNewsFeed(int userId) 检索当前用户新闻推送中最近  条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 按照时间顺序由最近到最远排序 。10
void follow(int followerId, int followeeId) ID 为 的用户开始关注 ID 为 的用户。followerIdfolloweeId
void unfollow(int followerId, int followeeId) ID 为 的用户不再关注 ID 为 的用户。followerIdfolloweeId


示例：

输入
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
输出
[null, null, [5], null, null, [6, 5], null, [5]]

解释
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
twitter.follow(1, 2);    // 用户 1 关注了用户 2
twitter.postTweet(2, 6); // 用户 2 发送了一个新推文 (推文 id = 6)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
twitter.unfollow(1, 2);  // 用户 1 取消关注了用户 2
twitter.getNewsFeed(1);  // 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2


提示：

1 <= userId, followerId, followeeId <= 500
0 <= tweetId <= 104
所有推特的 ID 都互不相同
postTweet、、 和 方法最多调用 次getNewsFeedfollowunfollow3 * 104
"""
import collections
import heapq


# 方法2：单链表实现推文信息流
class Tweet:
    def __init__(self, id, timestamp):
        self.id = id
        self.timestamp = timestamp
        self.next = None


class Twitter:
    def __init__(self):
        self.twitter = {}
        self.followings = collections.defaultdict(set)
        self.timestamp = 0
        self.minHeap = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if userId in self.twitter:
            oldHead = self.twitter[userId]
            newHead = Tweet(tweetId, self.timestamp)
            newHead.next = oldHead
            self.twitter[userId] = newHead
        else:
            self.twitter[userId] = Tweet(tweetId, self.timestamp)

    def getNewsFeed(self, userId: int):
        self.minHeap.clear()
        if userId in self.twitter:
            heapq.heappush(self.minHeap, (-self.twitter[userId].timestamp, self.twitter[userId]))
        for followingId in self.followings[userId]:
            tweet = self.twitter.get(followingId)
            if tweet is not None:
                heapq.heappush(self.minHeap, (-tweet.timestamp, tweet))

        res = []
        count = 0
        while self.minHeap and count < 10:
            _, head = heapq.heappop(self.minHeap)
            res.append(head.id)
            if head.next is not None:
                heapq.heappush(self.minHeap, (-head.next.timestamp, head.next))
            count += 1

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId == followerId:
            return
        self.followings[followerId].discard(followeeId)
