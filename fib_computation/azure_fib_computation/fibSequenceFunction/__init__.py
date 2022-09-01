import logging
import time
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    start = time.time()

    logging.info('Python HTTP trigger function processed a request.')
    
    if(req.method=='POST'):
        # setup
        iteration = req.params.get('iteration')

        if not iteration:
            try:
                req_body = req.get_json()
                logging.info('req body:' + req_body)
            except ValueError:
                pass
            else:
                iteration = req_body.get('iteration')

        logging.info("Is a POST request: "+str(req.method=='POST'))
        logging.info(type(int(iteration)))

        t0 = 0
        t1 = 1
        n = int(iteration)
        count = 0
        seq = [t0, t1]

        if iteration:
            if(n>2):
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

            
            return func.HttpResponse(        
            json.dumps(response),
            mimetype="application/json")
       
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Not a POST request.",
             status_code=200
        )



