class Task:
    def __init__(self, task_id, priority, arrival_time=None, deadline=None):
        self.task_id = task_id
        self.priority = priority
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __repr__(self):
        return f"Task(ID={self.task_id}, Priority={self.priority})"


class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)].priority < self.heap[i].priority:
            self.heap[i], self.heap[self.parent(i)] =                 self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_max(self):
        if self.is_empty():
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        largest = i
        left = self.left(i)
        right = self.right(i)

        if left < len(self.heap) and self.heap[left].priority > self.heap[largest].priority:
            largest = left

        if right < len(self.heap) and self.heap[right].priority > self.heap[largest].priority:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] =                 self.heap[largest], self.heap[i]
            self._heapify_down(largest)

    def increase_priority(self, index, new_priority):
        if new_priority < self.heap[index].priority:
            raise ValueError("New priority must be greater.")
        self.heap[index].priority = new_priority
        self._heapify_up(index)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.insert(Task("Task1", 4))
    pq.insert(Task("Task2", 10))
    pq.insert(Task("Task3", 2))

    while not pq.is_empty():
        print(pq.extract_max())
