import os
import json

postreqdata = json.loads(open(os.environ['req']).read())
response = open(os.environ['res'], 'w')
response.write("Hello"+postreqdata['name'])
response.close()
