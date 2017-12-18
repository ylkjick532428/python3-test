import cProfile, random

def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

if __name__ == '__main__':
    lIn = [random.random() for i in range(100000)]
    cProfile.run("f1(lIn)")
    cProfile.run("f2(lIn)")
    cProfile.run("f3(lIn)")
    
    
#          7 function calls in 0.077 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.002    0.002    0.077    0.077 <string>:1(<module>)
#         1    0.000    0.000    0.075    0.075 test4.py:3(f1)
#         1    0.009    0.009    0.009    0.009 test4.py:5(<listcomp>)
#         1    0.014    0.014    0.014    0.014 test4.py:6(<listcomp>)
#         1    0.000    0.000    0.077    0.077 {built-in method builtins.exec}
#         1    0.052    0.052    0.052    0.052 {built-in method builtins.sorted}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 
# 
#          7 function calls in 0.045 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.045    0.045 <string>:1(<module>)
#         1    0.009    0.009    0.009    0.009 test4.py:11(<listcomp>)
#         1    0.000    0.000    0.044    0.044 test4.py:8(f2)
#         1    0.008    0.008    0.008    0.008 test4.py:9(<listcomp>)
#         1    0.000    0.000    0.045    0.045 {built-in method builtins.exec}
#         1    0.027    0.027    0.027    0.027 {built-in method builtins.sorted}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
# 
# 
#          7 function calls in 0.084 seconds
# 
#    Ordered by: standard name
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.003    0.003    0.084    0.084 <string>:1(<module>)
#         1    0.000    0.000    0.081    0.081 test4.py:13(f3)
#         1    0.010    0.010    0.010    0.010 test4.py:14(<listcomp>)
#         1    0.008    0.008    0.008    0.008 test4.py:16(<listcomp>)
#         1    0.000    0.000    0.084    0.084 {built-in method builtins.exec}
#         1    0.063    0.063    0.063    0.063 {built-in method builtins.sorted}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
