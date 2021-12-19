from threading import Thread, current_thread
from time import sleep

def count_down(x):
    while x > 0:
        print('count down ' + str(x) + ' ' + str(current_thread().name) + '\n', end = '')
        x -= 1
        sleep(0.1)
    print('Ending: ' + str(current_thread().name))

def count_up(x):
    while x < 40:
        print('count up ' + str(x) + ' ' + str(current_thread().name) + '\n', end = '')
        x += 1
        sleep(0.2)
    print('Ending: ' + str(current_thread().name))
    
print('begining current thread', current_thread().name)
t1 = Thread(target = count_down, args = (40,), name = 'thread 1')
t2 = Thread(target = count_up, args = (0,), name = 'thread 2')
t1.start()
t2.start()
t1.join()
t2.join()

print('ending current thread', current_thread().name)