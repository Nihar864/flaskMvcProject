import time


def timestamp():
    seconds_since_epoch = time.time()
    return int(seconds_since_epoch)


def timestring(seconds):
    local_time_tuple = time.localtime(seconds)
    print(local_time_tuple)
