import time
import threading as tr
import multiprocessing as mp

start= time.perf_counter()

def do_something():
    print('sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


def done_something():
    print('sleeping 2nd funtion')
    time.sleep(1)
    print("done sleeping")


t1=mp.Process(target=do_something)
t2=mp.Process(target=done_something)

t1.start()
t2.start()
t1.join()    # if we dont use join here it will executes in background and move to next executable line
t2.join()


finish=time.perf_counter()

print(f'finished in {round(finish-start,2)} second(s)')