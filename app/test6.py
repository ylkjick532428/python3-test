#coding=utf8

import queue
import threading
import time

exitsingle = 0

class myThread(threading.Thread):
    def __init__(self, threadname, queuelist):
        threading.Thread.__init__(self)
        self.threadname = threadname
        self.queuelist = queuelist

    def run(self):
        print ("Starting queue %s"%self.threadname)
        queue_enter(self.threadname, self.queuelist)
        time.sleep(1)
        print ("close  " + self.threadname)

def queue_enter(threadname, queuelist):
    while not exitsingle:
        queueLock.acquire()
        if not workQueue.empty():
            data = queuelist.get()
            queueLock.release()
            print ("%s check ticket %s" % (threadname, data))
        else:
            queueLock.release()
        time.sleep(1)


threadList = ["list-1", "list-2", "list-3"]
queueLock = threading.Lock()
workQueue = queue.Queue()
threads = []

queueLock.acquire()
for num in range(100001,100020):
    workQueue.put(num)

queueLock.release()
print ("start ..")

for name in threadList:
    thread = myThread( name, workQueue)
    thread.start()
    threads.append(thread)

while not workQueue.empty():
    pass

exitsingle = 1

for t in threads:
    t.join()
print ("stop enter..")


# start ..
# Starting queue list-1
# list-1 check ticket 100001
# Starting queue list-2
# list-2 check ticket 100002
# Starting queue list-3
# list-3 check ticket 100003
# list-2 check ticket 100004
# list-1 check ticket 100005
# list-3 check ticket 100006
# list-2 check ticket 100007
# list-1 check ticket 100008
# list-3 check ticket 100009
# list-2 check ticket 100010
# list-1 check ticket 100011
# list-3 check ticket 100012
# list-2 check ticket 100013
# list-1 check ticket 100014
# list-3 check ticket 100015
# list-1 check ticket 100016
# list-2 check ticket 100017
# list-3 check ticket 100018
# list-2 check ticket 100019
# close  list-3
# close  list-1
# close  list-2
# stop enter..
