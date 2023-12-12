import random


class MemberInQueue:
    def __init__(self, name):
        self.name = name
        self.weight = random.randint(1, 100)


class PriorityQueue:
    def __init__(self):
        self.pqueue = list()

    def enqueue(self, name):
        member = MemberInQueue(name)
        self.pqueue.append(member)
        self.pqueue.sort(key=lambda x: x.weight, reverse=True)

    def dequeue(self):
        return self.pqueue[0] if len(self.pqueue) > 0 else None

    def trace_overall(self):
        print([(member.name, member.weight) for member in self.pqueue])


if __name__ == "__main__":
    member_priority_queue = PriorityQueue()
    member_priority_queue.enqueue("Peter")
    member_priority_queue.trace_overall()
    member_priority_queue.enqueue("Machi")
    member_priority_queue.trace_overall()
    member_priority_queue.enqueue("Jayce")
    member_priority_queue.trace_overall()

    # thread-safe
