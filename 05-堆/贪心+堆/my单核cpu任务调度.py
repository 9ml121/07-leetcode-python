"""
输入有若干行，每一行有四个数字（均小于108），
分别为任务ID，任务优先级，执行时间和到达时间。
每个任务的任务ID不同，优先级数字越大优先级越高，并且相同优先级的任务不会同时到达。
输入的任务已按照到达时间从小到达排列，

输入：
1 3 5 1
2 1 5 10
3 2 7 12
4 3 2 20
5 4 9 21
6 4 2 22

输出：
按照任务执行结束的顺序，输出每个任务的任务ID和对应的结束时间。
1 6
3 19
5 30
6 32
4 33
2 35

如果一个任务到来时，CPU是空闲的，则CPU可以运行该任务直到任务执行完毕。但是如果运行中有一个更高优先级的任务到来，则CPU必须暂停当前任务去运行这个优先级更高的任务；
如果一个任务到来时，CPU正在运行一个比它优先级更高的任务时，新到达的任务必须等待；
当CPU空闲时，如果还有任务在等待，CPU会从这些任务中选择一个优先级最高的任务执行，相同优先级的任务选择到达时间最早的任务。
"""
from queue import PriorityQueue


# 任务类
class Task:
    def __init__(self, tid, p, ptime, atime):
        self.tid = tid
        self.p = p
        self.ptime = ptime
        self.atime = atime

    def __lt__(self, other):
        if self.p == other.p:
            return self.atime < other.atime
        else:
            return self.p > other.p


# 算法逻辑
def getResult(tasks: list):
    pq = PriorityQueue()
    is_free = True

    # 记录当前时间
    curTime = tasks[0].atime
    # print(curTime)  # 1
    # pq先放入第一条任务
    pq.put(tasks.pop(0))

    # 按照任务一条一条从tasks弹出，放进pq这样遍历
    while len(tasks) > 0:
        curTask = pq.queue[0]  # 每次都是先取出pq当前优先级最高的
        nextTask = tasks.pop(0)

        endTime = curTime + curTask.ptime

        if endTime > nextTask.atime:
            # 如果当前正在运行任务的理想结束时间,超过了下一个任务的开始时间
            # 先不看优先级，先将当前任务可以运行的时间减去
            curTask.ptime -= (nextTask.atime - curTime)
            curTime = nextTask.atime
        else:
            # 如果当前正在运行任务的理想结束时间, 没有超过了下一个任务的开始时间
            # 可以结束这条任务，并打印
            pq.get()
            print(f'{curTask.tid} {endTime}')

            # 接下来cpu空闲，如果还有任务等待，会取出pq里面优先级最高的,逻辑同上
            while pq.qsize() != 0:
                idleTask = pq.queue[0]
                idleTask_endTime = curTime + idleTask.ptime

                if idleTask_endTime > nextTask.atime:
                    idleTask.ptime -= nextTask.atime - curTime
                    break
                else:
                    pq.get()
                    print(f"{idleTask.tid} {idleTask_endTime}")
                    curTime = idleTask_endTime

        pq.put(nextTask)

        # 所有任务都加入优先队列后，我们就可以按照优先队列的安排，顺序取出任务来执行了
        while pq.qsize() > 0:
            pollTask = pq.get()
            pollTask_endTime = curTime + pollTask.ptime
            print(f"{pollTask.tid} {pollTask_endTime}")
            curTime = pollTask_endTime


# 处理输入
tasks = []
while True:
    line = input()
    if line == '':
        getResult(tasks)
        break
    else:
        seq = list(map(int, line.split()))
        tid, p, ptime, atime = seq
        task = Task(tid, p, ptime, atime)
        tasks.append(task)
