from src.task import task
from src.task_pool import task_pool, load_task_pool


def cal(x, y):
    ans = 0
    for i in range(x*x*y*y):
        ans+=1
    return ans


if __name__ == "__main__":
    t = task("default task1", cal, 2)
    t.args = {'x': 50, 'y': 50}
    t2 = task("default task2", cal, 2)
    t2.args = {'x': 40, 'y': 50}
    pool = task_pool()
    pool.push(t)
    pool.push(t2)
    print(len(pool.pool))
    pool.run()
    print(pool.get_result())

    # save
    path = '/Users/dayiyi/Downloads/test_pool'
    pool.save(path)

    # load
    pool = load_task_pool(path)
    print(pool.get_result())
