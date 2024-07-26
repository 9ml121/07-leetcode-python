"""
题目描述：现在有一个CPU和一些任务需要处理，已提前获知每个任务的任务ID、优先级、所需执行时间和到达时间。
CPU同时只能运行一个任务，请编写一个任务调度程序，采用“可抢占优先权调度”调度算法进行任务调度，规则如下：

如果一个任务到来时，CPU是空闲的，则CPU可以运行该任务直到任务执行完毕。但是如果运行中有一个更高优先级的任务到来，则CPU必须暂停当前任务去运行这个优先级更高的任务；
如果一个任务到来时，CPU正在运行一个比它优先级更高的任务时，新到达的任务必须等待；
当CPU空闲时，如果还有任务在等待，CPU会从这些任务中选择一个优先级最高的任务执行，相同优先级的任务选择到达时间最早的任务。
输入描述：

输入有若干行，每一行有四个数字（均小于108），分别为任务ID，任务优先级，执行时间和到达时间。每个任务的任务ID不同，优先级数字越大优先级越高，并且相同优先级的任务不会同时到达。
输入的任务已按照到达时间从小到达排列，并且保证在任何时间，处于等待的任务不超过10000个。

输出描述：

按照任务执行结束的顺序，输出每个任务的任务ID和对应的结束时间。

补充说明：



示例1

输入：

1 3 5 1
2 1 5 10
3 2 7 12
4 3 2 20
5 4 9 21
6 4 2 22
输出：

1 6
3 19
5 30
6 32
4 33
2 35
说明：
"""

import queue

'''
Python算法源码
Python可以基于queue.PriorityQueue来实现优先队列，但是queue.PriorityQueue的自定义排序不支持函数参数传入，
而是只能基于queue.PriorityQueue加入的元素的自身比较器（如__lt__和__gt__）来排序
'''


class Task:
    def __init__(self, taskId, priority, need, arrived):
        self.taskId = taskId
        self.priority = priority
        self.need = need
        self.arrived = arrived

    def __gt__(self, other):
        if self.priority != other.priority:
            return other.priority > self.priority
        else:
            return self.arrived > other.arrived


# 算法入口
def getResult(tasks):
    pq = queue.PriorityQueue()

    pq.put(tasks.pop(0))
    curTime = pq.queue[0].arrived  # curTime记录当前时刻

    while len(tasks) > 0:
        curtTask = pq.queue[0]  # 当前正在运行的任务curtTask
        nextTask = tasks.pop(0)  # 下一个任务nextTask

        curTask_endTime = curTime + curtTask.need  # 当前正在运行任务的“理想”结束时间

        # 如果当前正在运行任务的理想结束时间  超过了  下一个任务的开始时间
        if curTask_endTime > nextTask.arrived:
            curtTask.need -= nextTask.arrived - curTime  # 先不看优先级，先将当前任务可以运行的时间减去
            curTime = nextTask.arrived
        # 如果当前正在运行任务的理想结束时间  没有超过  下一个任务的开始时间，则当前任务可以执行完
        else:
            pq.get()
            print(f"{curtTask.taskId} {curTask_endTime}")  # 打印执行完的任务的id和结束时间
            curTime = curTask_endTime

            # 如果当前任务结束时，下一次任务还没有达到，那么存在CPU空转(即idle)
            if nextTask.arrived > curTask_endTime:
                # 此时，我们应该从优先队列中取出最优先的任务出来执行，逻辑同上
                while pq.qsize() > 0:
                    idleTask = pq.queue[0]
                    idleTask_endTime = curTime + idleTask.need

                    if idleTask_endTime > nextTask.arrived:
                        idleTask.need -= nextTask.arrived - curTime
                        break
                    else:
                        pq.get()
                        print(f"{idleTask.taskId} {idleTask_endTime}")
                        curTime = idleTask_endTime

                curTime = nextTask.arrived

        pq.put(nextTask)

    # 所有任务都加入优先队列后，我们就可以按照优先队列的安排，顺序取出任务来执行了
    while pq.qsize() > 0:
        pollTask = pq.get()
        pollTask_endTime = curTime + pollTask.need
        print(f"{pollTask.taskId} {pollTask_endTime}")
        curTime = pollTask_endTime


# 输入获取
tasks = []
while True:
    task = input()
    if task == "":
        getResult(tasks)
        break
    else:
        tmp = list(map(int, task.split()))
        task = Task(tmp[0], tmp[1], tmp[2], tmp[3])
        tasks.append(task)
