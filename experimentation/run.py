import os

response = open(os.environ['res'], 'w')
response.write(os.environ['req'])
response.close()