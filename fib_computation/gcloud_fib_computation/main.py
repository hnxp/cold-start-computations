import functions_framework
import bcrypt
import time
import json


@functions_framework.http
def compute_hash(request):

    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'

    start = time.time()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(name.encode(), salt)
    end = time.time()
    diff = round(end-start, 4)
    message = "Input hashed. Took " + \
        str(diff) + "s to compute hash. Hash: "+str(hashed)
    return str(diff)


@functions_framework.http
def get_fib_sequence(request):
    start = time.time()
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'iteration' in request_json:
        iteration = request_json['iteration']
    elif request_args and 'iteration' in request_args:
        iteration = request_args['iteration']
    else:
        iteration = 1

    t0 = 0
    t1 = 1
    n = int(iteration)
    count = 0
    seq = [t0, t1]

    if(n < 1):
        end = time.time()
        diff = round(end-start, 4)
        response = {
            "computation_time": diff
        }
        return json.dumps(response)
    elif(n == 1):
        end = time.time()
        diff = round(end-start, 4)
        response = {
            "computation_time": diff
        }
        return json.dumps(response)
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
    return json.dumps(response)
