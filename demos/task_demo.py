from src.task import task


def cal(x, y):
    return [x + y, x - y]


if __name__ == "__main__":
    t = task("default task")
    t.algo = cal
    t.repeat = 2
    t.args = {'x': 1, 'y': 5}
    t.run()
    print(t.get_result())