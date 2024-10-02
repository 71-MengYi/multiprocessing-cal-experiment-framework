import multiprocessing


class task:
    name = "default task"
    args = None
    output = None

    def __init__(self, name: str, algo, repeat: int, call_back, cover=False):
        self.name = name
        self.algo = algo
        self.repeat = repeat
        self.cover = cover
        self.call_back = call_back

    def run(self):
        n_cpu = multiprocessing.cpu_count()
        with multiprocessing.Pool(processes=n_cpu) as pool:
            self.output = pool.map(self._map_args, [self.args for _ in range(self.repeat)])

    def get_task_result(self):
        for i in range(len(self.output)):
            self.output[i] = self.call_back(self.output[i])
        return self.output

    def _map_args(self, args: dict):
        return self.algo(**args)

    def set_args(self, args: dict):
        self.args = args

    def add_arg(self, arg_name: str, arg_value):
        self.args[arg_name] = arg_value
