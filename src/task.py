class task:
    name = "default task"
    dataset = {}  # 多组不同参数数据集
    args = {}  # 多组不同算法参数
    repeat = None
    output = None

    def __init__(self, name):
        self.name = name

    def run(self):
        for arg in self.args:
            for dataset in self.dataset:
                res = None
                self.output[dataset][arg] = res

    def get_arg_result(self, arg):
        output_by_arg = {}
        for dataset in self.output:
            output_by_arg[dataset] = self.output[dataset][arg]
        return output_by_arg

    def get_dataset_result(self, dataset):
        return self.output[dataset]

    def get_all_result(self):
        return self.output
