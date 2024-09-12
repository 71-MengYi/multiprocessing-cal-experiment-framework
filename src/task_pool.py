import multiprocessing


class task_pool:
    def __init__(self):
        self.pool = []
        self.output = {}

    def push(self, task):
        self.pool.append(task)

    def run(self):
        n_cpu = multiprocessing.cpu_count()
        with multiprocessing.Pool(processes=n_cpu) as pool:
            for i in range(len(self.pool)):
                self.pool[i].output = pool.map(self._map_args, [self.pool[i] for _ in range(self.pool[i].repeat)])

    @staticmethod
    def _map_args(task):
        return task.algo(**task.args)

    def get_result(self):
        for task in self.pool:
            self.output[task.name] = task.output
        return self.output

