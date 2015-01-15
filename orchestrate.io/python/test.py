#!/usr/bin/python
# -*- coding: utf-8 -*-

from porc import Client

YOUR_API_KEY = "ce17e2a6-eaa3-47a7-bd16-8a84a7535cf7"

# create a client using the default AWS US East host: https://api.orchestrate.io
client = Client(YOUR_API_KEY)

# create a client using the EU datacenter
host = "https://api.aws-us-east-1.orchestrate.io/"
#client = Client(YOUR_API_KEY, host)
client = Client(YOUR_API_KEY)

# make sure our API key works
client.ping().raise_for_status()

COLLECTION = "test"
KEY = "test1"
KEY_1 = "test2_1"
KEY_2 = "test2_2"

response = client.put('users', 'batman2', {
  "Name": "Bruce Wayne",
  "City": "Gotham City",
  "Cape": "true"
})


# get and update an item
item = client.get(COLLECTION, KEY)
item['was_modified'] = True
client.put(item.collection, item.key, item.json, item.ref).raise_for_status()

# asynchronously get two items
with client.async() as c:
    futures = [
        c.get(COLLECTION, KEY_1),
        c.get(COLLECTION, KEY_2)
    ]
    responses = [future.result() for future in futures]
    [response.raise_for_status() for response in responses]

# iterate through search results
pages = client.search(COLLECTION, QUERY)
for page in pages:
    # prints 200
    print page.status_code
    # prints number of items returned by page
    print page['count']

# get every item in a collection
items = client.list(COLLECTION).all()
# prints number of items in collection
print len(items)