# there is no multi threading in python because Global Interpruer Lock
# whenever we dealing multi proccessing we have to passs if __name__= __main__ 

from multiprocessing import Process 
import math
import time

result_a=[]
result_b=[]
result_c=[]

def make_caluculations_one(numbers):
    for number in numbers:
        result_a.append(math.sqrt(number**5))
        
def make_caluculations_two(numbers):
    for number in numbers:
        result_b.append(math.sqrt(number**5))

def make_caluculations_three(numbers):
    for number in numbers:
        result_c.append(math.sqrt(number**5))


if __name__=='__main__':

    numbers=list(range(100000))


    p1=Process(target=make_caluculations_one,args=(numbers,))
    p2=Process(target=make_caluculations_two,args=(numbers,))
    p3=Process(target=make_caluculations_three,args=(numbers,))

    start=time.time()

    p1.start()
    p2.start()
    p3.start()

    end=time.time()

    print(end-start)

    start=time.time()

    make_caluculations_one(numbers)
    make_caluculations_two(numbers)
    make_caluculations_three(numbers)

    end=time.time()

    timeafter=end-start

    print(timeafter)
