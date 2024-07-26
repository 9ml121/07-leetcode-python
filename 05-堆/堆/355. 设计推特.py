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
import heapq
import collections
from typing import List

"""
链表 + 优先队列的多路合并问题

这里「推特」，可以理解为中国的「微博」、「朋友圈」、「力扣」，真正的数据数需要存在数据库里的，并且还要加上一些非关系型的数据库（redis 等），不能是放在内存里的，这里只是简化了需求。

分析：

- 这是一类系统设计问题（上周我们做过的 LFU 缓存也是属于这一类问题），通常简化了很多需求，只要题目意思理解清楚，一般情况下不难写出，难在编码的细节和调试；
- 这里需求 3 和需求 4，只需要维护「我关注的人的 id 列表」 即可，不需要维护「谁关注了我」，由于不需要维护有序性，为了删除和添加方便， 
    「我关注的人的 id 列表」需要设计成哈希表（HashSet），而每一个人的和对应的他关注的列表存在一个哈希映射（HashMap）里；
- 最复杂的是需求 2 getNewsFeed(userId):
    - 每一个人的推文和他的 id 的关系，依然是存放在一个哈希表里；
    - 对于每一个人的推文，只有顺序添加的需求，没有查找、修改、删除操作，因此可以使用线性数据结构，链表或者数组均可；
        - 使用数组就需要在尾部添加元素，还需要考虑扩容的问题（使用动态数组）；
        - 使用链表就得在头部添加元素，由于链表本身就是动态的，无需考虑扩容；
    - 检索最近的十条推文，需要先把这个用户关注的人的列表拿出来（实际上不是这么做的，请看具体代码，或者是「多路归并」的过程），然后再合并，排序以后选出 Top10，
        这其实是非常经典的「多路归并」的问题（「力扣」第 23 题：合并K个排序链表），这里需要使用的数据结构是优先队列，
        所以在上一步在存储推文列表的时候使用单链表是合理的，并且应该存储一个时间戳字段，用于比较哪一队的队头元素先出列。
- 剩下的就是一些细节问题了，例如需要查询关注人（包括自己）的最近十条推文，所以要把自己的推文也放进优先队列里。在出队（优先队列）、入队的时候需要考虑是否为空。

编写对这一类问题，需要仔细调试，并且养成良好的编码习惯，是很不错的编程练习问题。

总结：

1.如果需要维护数据的时间有序性，链表在特殊场景下可以胜任。因为时间属性通常来说是相对固定的，而不必去维护顺序性；
2.如果需要动态维护数据有序性，「优先队列」（堆）是可以胜任的，「力扣」上搜索「堆」（heap）标签，可以查看类似的问题；
3.设计类问题也是一类算法和数据结构的问题，并且做这一类问题有助于我们了解一些数据结构的大致思想和细节，「力扣」上搜索「设计」标签，可以查看类似的问题；
4.做完这个问题，不妨仔细思考一下这里使用链表存储推文的原因。!!!

"""
# 方法1：动态数组实现推文信息流
class Twitter1:

    def __init__(self):
        #  用户 id 和推文（单链表）的对应关系 
        self.twitter = collections.defaultdict(list)
        # 用户 id 和他关注的用户列表的对应关系 
        self.followings = collections.defaultdict(set)
        # 全局使用的时间戳字段，用户每发布一条推文之前 + 1 
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """Compose a new tweet. """
        self.timestamp += 1
        self.twitter[userId].append((-self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        """ Retrieve the 10 most recent tweet ids in the user's news feed. 
        Each item in the news feed must be posted by users who the user followed or by the user herself. 
        Tweets must be ordered from most recent to least recent. 
        """
        # 合并 k 组推文使用的数据结构（可以在方法里创建使用），声明成全局变量非必需，视个人情况使用 
        min_heap = []
        # 如果自己发了推文也要算上 
        tweets = self.twitter[userId][-10:]
        for t in tweets:
            heapq.heappush(min_heap, t)
        # 获取我自己的关注列表
        followingSet = self.followings[userId]
        if followingSet:
            for followeeId in followingSet:
                tweets = self.twitter[followeeId][-10:]
                for t in tweets:
                    heapq.heappush(min_heap, t)

        res = []
        count = 0
        while min_heap and count < 10:
            res.append(heapq.heappop(min_heap)[1])
            count += 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followings[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


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


# 版本3
# 基于链表的方式实现,另外一种写法
class Tweet2:

    def __init__(self, tweetId, timestamp):
        self.id = tweetId
        self.timestamp = timestamp
        self.next = None

    def __lt__(self, other):
        return self.timestamp > other.timestamp


class Twitter2:

    def __init__(self):
        self.followings = collections.defaultdict(set)
        self.tweets = collections.defaultdict(lambda: None)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        tweet = Tweet(tweetId, self.timestamp)
        tweet.next = self.tweets[userId]
        self.tweets[userId] = tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        heap = []

        tweet = self.tweets[userId]
        if tweet:
            heap.append(tweet)

        for user in self.followings[userId]:
            tweet = self.tweets[user]
            if tweet:
                heap.append(tweet)
        heapq.heapify(heap)

        while heap and len(tweets) < 10:
            head = heapq.heappop(heap)
            tweets.append(head.id)

            if head.next:
                heapq.heappush(heap, head.next)
        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followings[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followings[followerId].discard(followeeId)


if __name__ == '__main__':
    twitter = Twitter()
    twitter.postTweet(1, 1)
    res1 = twitter.getNewsFeed(1)
    print(res1)
    twitter.follow(2, 1)
    res2 = twitter.getNewsFeed(2)
    print(res2)
    twitter.unfollow(2, 1)
    res3 = twitter.getNewsFeed(2)
    print(res3)
