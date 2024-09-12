from src.task import task


def cal(x, y):
    ans = 0
    for i in range(x*x*y*y):
        ans+=1
    return ans


if __name__ == "__main__":
    t = task("default task", cal, 200)
    t.args = {'x': 50, 'y': 50}
    t.run()
    print(t.get_task_result())
