from os import system
from time import sleep

system('clear')
stop = False
i = 0
sleep_time = 0
while stop == False:
    print(i,sleep_time)
    if i > 10:
        stop = True
    i = i+1
    sleep_time = i/max(i-i/2,1)
    sleep(sleep_time)
