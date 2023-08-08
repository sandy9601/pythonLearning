import multiprocessing as mp
import time



start= time.perf_counter()

def do_something():
    print('sleeping 1 second...')
    time.sleep(1)
    print('Done sleeping...')


def done_something():
    print('sleeping 2nd funtion')
    time.sleep(1)
    print("done sleeping")

# p1=mp.Process(target=do_something)
# p2=mp.Process(target=done_something)

# p1.start()
# p2.start()
# p1.join()
# p2.join()

done_something()  
do_something()




finish=time.perf_counter()

print(f'finished in {round(finish-start,2)} second(s)')