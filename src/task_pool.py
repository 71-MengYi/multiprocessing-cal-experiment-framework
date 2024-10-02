import json
import multiprocessing
import pickle


class task_pool:
    def __init__(self):
        self.pool = []
        self.output = {}
        self.size = 0

    def push(self, task):
        self.pool.append(task)
        self.size += 1

    def run(self):
        n_cpu = multiprocessing.cpu_count()
        with multiprocessing.Pool(processes=n_cpu) as pool:
            for i in range(self.size):
                task = self.pool[i]
                task.output = pool.map(task_pool._map_args, [task for _ in range(task.repeat)])

    @staticmethod
    def _map_args(task):
        return task.algo(**task.args)

    def get_result(self):
        for task in self.pool:
            self.output[task.name] = task.output
        return self.output

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)


def load_task_pool(path):
    with open(path, 'rb') as f:
        return pickle.load(f)
