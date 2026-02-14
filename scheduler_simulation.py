import random
from priority_queue import PriorityQueue, Task

def generate_tasks(num_tasks):
    tasks = []
    for i in range(num_tasks):
        priority = random.randint(1, 100)
        tasks.append(Task(f"T{i+1}", priority))
    return tasks

def simulate_scheduler(num_tasks):
    pq = PriorityQueue()
    tasks = generate_tasks(num_tasks)

    for task in tasks:
        pq.insert(task)

    print("Processing Tasks by Priority:")
    while not pq.is_empty():
        print(pq.extract_max())

if __name__ == "__main__":
    simulate_scheduler(10)
