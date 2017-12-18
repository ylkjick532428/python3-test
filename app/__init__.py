from functools import reduce 

def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print (sChildPath)
            
def test2():
    A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
    print ("A0", A0)
    A1 = list(range(10))
    print ("A1", A1)
    A2 = [i for i in A1 if i in A0]
    print ("A2", A2)
    A3 = [A0[s] for s in A0]
    print ("A3", A3)
    A4 = [i for i in A1 if i in A3]
    print ("A4", A4)
    A5 = {i:i*i for i in A1}
    print ("A5", A5)
    A6 = [[i,i*i] for i in A1]
    print ("A6", A6)

def test3(): 
    def f(x,l=[]):
        for i in range(x):
            l.append(i*i)
        print (l)
    
    f(2)
    f(3,[3,2,1])
    f(3, [3,2,1, 4])
    f(3)
    f(3)

def test4():
    def f(*args,**kwargs): print (args, kwargs)

    l = [1,2,3]
    t = (4,5,6)
    d = {'a':7,'b':8,'c':9}
    
    f()
    f(1,2,3)                    # (1, 2, 3) {}
    f(1,2,3,"groovy")           # (1, 2, 3, 'groovy') {}
    f(a=1,b=2,c=3)              # () {'a': 1, 'c': 3, 'b': 2}
    f(a=1,b=2,c=3,zzz="hi")     # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
    f(1,2,3,a=1,b=2,c=3)        # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}
    
    f(*l,**d)                   # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
    f(*t,**d)                   # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
    f(1,2,*t)                   # (1, 2, 4, 5, 6) {}
    f(q="winning",**d)          # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    f(1,2,*t,q="winning",**d) 

def test5():    
    def f2(arg1,arg2,*args,**kwargs): print (arg1,arg2, args, kwargs)
    l = [1,2,3]
    t = (4,5,6)
    d = {'a':7,'b':8,'c':9}
    
    f2(1,2,3)                       # 1 2 (3,) {}
    f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
    f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
    f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
    f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}
    
    f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
    f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
    f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
    f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
    f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

def test6():
    f = lambda x, y : {x:y}
    print(f(1,2))
    
    l1 = [ 0, 1, 2, 3, 4, 5, 6 ]  
    l2 = [ 'Sun', 'M', 'T', 'W', 'T', 'F', 'S' ]   
    m = list(map(f, l1, l2))
    for i in m:
        print (i)
    
def test7():
    def f1(x): return True if x > 20 else False
    l2 = filter(f1, range(30))
    for l in l2:
        print (l)

#===============================================================================
# test8 : reduce 
#===============================================================================
def test8():
    f = lambda x, y : "%s%s" % (x,y)
    l1 = [ 0, 1, 2, 3, 4, 5, 6 ] 
    tmp = reduce(f, l1)
    print (tmp)
    
if __name__ == '__main__':
#     print_directory_contents("./")
#     test2()
#     test3()
#     test4()
#     test5()
#     test6()
#     test7()
    test8()
