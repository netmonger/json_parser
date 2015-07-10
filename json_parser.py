import json
import pprint

with open('ning-discussions.json') as data_file:    
	    data = json.load(data_file)
	    # pprint(data)

entry1 = data[0]

topicID = entry1["id"]
contributorName = entry1["contributorName"]
title = entry1["title"]
description = entry1["description"]
createdDate = entry1["createdDate"]
updatedDate = entry1["updatedDate"]
comments = entry1["comments"]

print "Title: %s" % title
print "Author: %s" % contributorName
print "Date: %s" % createdDate
print 
print description
