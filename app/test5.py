ss = "dfdifdjf ((ddfdf) dfddf(dfsfs dfdfdf (dfdfd)dfdfdf) dfdfdf(dfdf)dfdfdf)"


import queue
q = queue.LifoQueue()

result = {}
for i in range(len(ss)):
    if ss[i] == "(":
        q.put(i)
    elif ss[i] == ")":
        pre_i = q.get()
        result[pre_i] = i
    else:
        pass
print (result)

# {10: 16, 37: 43, 23: 50, 58: 63, 9: 70}
