import os
import json

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
postreqdata['code'] = os.environ['req_query_code']
response.write(json.dumps(postreqdata))
response.close()
