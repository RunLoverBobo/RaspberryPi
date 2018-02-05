from time import time, sleep, localtime


if(localtime().tm_hour<7 or localtime().tm_hour>23):
    print('a')

