import time
import json

seq = []
n = 0


def handler(event, context):
    global seq
    global n
    start = time.time()
    iteration = int(event['iteration'])
    if(len(seq) == 0 | n != iteration):
        t0 = 0
        t1 = 1
        n = iteration
        count = 0
        seq = [t0, t1]

        if(n < 2):
            end = time.time()
        else:
            while(count < n):
                new = t0+t1
                seq.append(new)
                t0 = t1
                t1 = new
                count += 1
            end = time.time()
        diff = end-start
        response = {
            "computation_time": diff
        }
        return response
    else:
        start = time.time()
        end = time.time()
        diff = round(end-start, 4)
        response = {
            "computation_time": diff
        }
        return response
