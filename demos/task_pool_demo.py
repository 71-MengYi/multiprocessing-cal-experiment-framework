from src.task import task
from src.task_pool import task_pool


def cal(x, y):
    ans = 0
    for i in range(x*x*y*y):
        ans+=1
    return ans


if __name__ == "__main__":
    t = task("default task1", cal, 2)
    t.args = {'x': 50, 'y': 500}
    t2 = task("default task2", cal, 2)
    t2.args = {'x': 40, 'y': 500}
    pool = task_pool()
    pool.push(t)
    pool.push(t2)
    print(len(pool.pool))
    pool.run()
    print(pool.get_result())

