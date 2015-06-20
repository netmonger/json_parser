import json
from pprint import pprint

with open('ning-discussions.json') as data_file:    
	    data = json.load(data_file)
	    pprint(data)
