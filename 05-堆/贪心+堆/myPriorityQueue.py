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

