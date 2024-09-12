import multiprocessing


class task:
    name = "default task"
    args = None
    algo = None
    repeat = None
    output = None

    def __init__(self, name: str, algo, repeat: int):
        self.name = name
        self.algo = algo
        self.repeat = repeat

    def run(self):
        n_cpu = multiprocessing.cpu_count()
        with multiprocessing.Pool(processes=n_cpu) as pool:
            self.output = pool.map(self._map_args, [self.args for _ in range(self.repeat)])

    def get_task_result(self):
        return self.output

    def _map_args(self, args: dict):
        return self.algo(**args)

    def set_args(self, args: dict):
        self.args = args

    def add_arg(self, arg_name: str, arg_value):
        self.args[arg_name] = arg_value
