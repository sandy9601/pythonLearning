import time
import threading as tr

start= time.perf_counter()

def do_something():
    print('sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


def done_something():
    print('sleeping 2nd funtion')
    time.sleep(1)
    print("done sleeping")


t1=tr.Thread(target=do_something)
t2=tr.Thread(target=done_something)

t1.start()
t2.start()
t1.join()
t2.join()


finish=time.perf_counter()

print(f'finished in {round(finish-start,2)} second(s)')