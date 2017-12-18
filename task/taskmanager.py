import random, time
import queue as Queue
from multiprocessing.managers import BaseManager

# 发送任务的队列:
task_queue = Queue.Queue()
# 接收结果的队列:
result_queue = Queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

# 把两个Queue都注册到网络上, callable参数关联了Queue对象:
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('0.0.0.0', 5000), authkey='abc'.encode("utf8"))
# 启动Queue:
manager.start()
# 获得通过网络访问的Queue对象:
task = manager.get_task_queue()
result = manager.get_result_queue()
# 放几个任务进去:
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# 从result队列读取结果:
print('Try get results...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()


# Put task 1454...
# Put task 4773...
# Put task 1220...
# Put task 6128...
# Put task 2354...
# Put task 2140...
# Put task 3686...
# Put task 4608...
# Put task 3870...
# Put task 5160...
# Try get results...
# Result: 1454 * 1454 = 2114116
# Result: 4773 * 4773 = 22781529
# Result: 1220 * 1220 = 1488400
# Result: 6128 * 6128 = 37552384
# Result: 2354 * 2354 = 5541316
# Result: 2140 * 2140 = 4579600
# Result: 3686 * 3686 = 13586596
# Result: 4608 * 4608 = 21233664
# Result: 3870 * 3870 = 14976900
# Result: 5160 * 5160 = 26625600