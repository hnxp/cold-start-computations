import time
import json


def handler(event, context):
    
    start = time.time()

    t0 = 0
    t1 = 1
    n = int(event['iteration'])
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
    diff = round(end-start, 4)
    response = {
        "computation_time": diff
    }
    return response

