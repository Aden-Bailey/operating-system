import threading
import time
import random

# Logging with timestamps
START = time.time()
PRINT_LOCK = threading.Lock()

def ts():
    s = int(time.time() - START)
    return f"[{s//60:02d}:{s%60:02d}]"

def log(msg):
    with PRINT_LOCK:
        print(f"{ts()} {msg}", flush=True)

# ---------- Model ----------
class Fork:
    def __init__(self, fork_id):
        self.id = fork_id

THINKING, HUNGRY, EATING = 0, 1, 2

class Table:
    """
    Monitor that controls fork access using classic philosopher states + condition variables.
    """
    def __init__(self, n):
        self.n = n
        self.lock = threading.Lock()
        self.state = [THINKING] * n
        self.cv = [threading.Condition(self.lock) for _ in range(n)]

    def left(self, i):   # left neighbor index
        return (i - 1) % self.n

    def right(self, i):  # right neighbor index
        return (i + 1) % self.n

    def _test(self, i):
        # i can eat if hungry and neighbors are not eating
        if (self.state[i] == HUNGRY and
            self.state[self.left(i)] != EATING and
            self.state[self.right(i)] != EATING):
            self.state[i] = EATING
            self.cv[i].notify()

    def pick_up(self, i):
        with self.lock:
            self.state[i] = HUNGRY
            self._test(i)
            while self.state[i] != EATING:
                self.cv[i].wait()

    def put_down(self, i):
        with self.lock:
            self.state[i] = THINKING
            # neighbors might be able to eat now
            self._test(self.left(i))
            self._test(self.right(i))

class Philosopher(threading.Thread):
    def __init__(self, pid, left_fork, right_fork, table, meals=5):
        super().__init__()
        self.pid = pid          # 1..n (for printing)
        self.i = pid - 1        # 0..n-1 (for indexing)
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.table = table
        self.meals = meals

    def run(self):
        for _ in range(self.meals):
            log(f"Philosopher {self.pid} is Thinking.")
            time.sleep(random.uniform(0.3, 1.2))

            self.table.pick_up(self.i)
            log(f"Philosopher {self.pid} picked up Left Fork.")
            log(f"Philosopher {self.pid} picked up Right Fork.")
            log(f"Philosopher {self.pid} is Eating.")
            time.sleep(random.uniform(0.3, 1.2))

            log(f"Philosopher {self.pid} put down Right Fork.")
            log(f"Philosopher {self.pid} put down Left Fork.")
            self.table.put_down(self.i)

def main():
    random.seed(0)
    n = 5
    forks = [Fork(i) for i in range(n)]
    table = Table(n)

    philosophers = []
    for i in range(n):
        left = forks[i]
        right = forks[(i + 1) % n]
        philosophers.append(Philosopher(i + 1, left, right, table, meals=5))

    for p in philosophers:
        p.start()
    for p in philosophers:
        p.join()

if __name__ == "__main__":
    main()